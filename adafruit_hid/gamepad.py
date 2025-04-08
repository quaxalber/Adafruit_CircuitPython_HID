# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
# SPDX-FileCopyrightText: 2021 Dan Halbert for Adafruit Industries
# SPDX-FileCopyrightText: 2025 quaxalber
#
# SPDX-License-Identifier: MIT

"""
`adafruit_hid.generic_gamepad.GenericGamepad`
====================================================

HID Gamepad driver definition compatible with a generic descriptor
mimicking PS5-like features (Buttons, Hat, 6 Axes).


Implementation Notes
--------------------
**Hardware:**
* Any CircuitPython hardware with USB HID support.
**Software and Dependencies:**
* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
* Adafruit's HID library: https://github.com/adafruit/Adafruit_CircuitPython_HID
"""

from . import find_device


# pylint: disable=too-many-arguments, too-many-instance-attributes
class Gamepad:
    """Send Generic Gamepad HID reports."""

    # Report ID definition (must match the descriptor)
    _REPORT_ID = 4
    # Report length definition (must match the descriptor for the input report)
    _REPORT_LENGTH = 10  # 1 (Report ID) + 2 (buttons) + 1 (hat) + 6 (axes)

    # pylint: disable=invalid-name
    # Suggested Button mapping based on common layouts and PS controller
    # Bits 0-15 (corresponds to Button 1 to 16 in descriptor)
    BUTTON_1 = 1  # Usually Square / West
    BUTTON_2 = 2  # Usually Cross (X) / South
    BUTTON_3 = 3  # Usually Circle / East
    BUTTON_4 = 4  # Usually Triangle / North
    BUTTON_5 = 5  # L1 / Left Shoulder
    BUTTON_6 = 6  # R1 / Right Shoulder
    BUTTON_7 = 7  # L2 / Left Trigger Click/Button
    BUTTON_8 = 8  # R2 / Right Trigger Click/Button
    BUTTON_9 = 9  # Create / Share / Select
    BUTTON_10 = 10  # Options / Start
    BUTTON_11 = 11  # L3 / Left Stick Click
    BUTTON_12 = 12  # R3 / Right Stick Click
    BUTTON_13 = 13  # PS / Home / Guide
    BUTTON_14 = 14  # Touchpad Click
    BUTTON_15 = 15  # Unassigned
    BUTTON_16 = 16  # Unassigned

    # Hat switch directions (0-7 are active, 8 represents neutral/release)
    HAT_TOP = 0
    HAT_TOP_RIGHT = 1
    HAT_RIGHT = 2
    HAT_BOTTOM_RIGHT = 3
    HAT_BOTTOM = 4
    HAT_BOTTOM_LEFT = 5
    HAT_LEFT = 6
    HAT_TOP_LEFT = 7
    HAT_NEUTRAL = 8  # Value to send for neutral (outside 0-7 range)
    # pylint: enable=invalid-name

    def __init__(self, devices):
        """Create a GenericGamepad object that will send USB HID reports.

        :param devices: Sequence of devices supporting the Generic Gamepad HID descriptor.
                        Try ``usb_hid.devices``.
        """
        self._gamepad_device = find_device(devices, usage_page=0x1, usage=0x05)

        if not self._gamepad_device:
            raise ValueError("Could not find matching Generic Gamepad HID device.")

        # Report buffer: ID (1) + Buttons (2) + Hat (1) + Axes (6) = 10 bytes
        # Initialize to neutral state: ID=1, buttons=0, hat=neutral(8), axes=center(128)
        self._report = bytearray(self._REPORT_LENGTH)
        self._report[0] = self._REPORT_ID
        # Initialize buttons (bytes 1-2) to 0
        self._report[1] = 0x00
        self._report[2] = 0x00
        # Initialize hat (byte 3, lower nibble) to neutral (8). Upper nibble is padding.
        self._report[3] = self.HAT_NEUTRAL & 0x0F
        # Initialize axes (bytes 4-9) to center (128 for 0-255 range)
        for i in range(4, 10):
            self._report[i] = 128

        # Remember previous report state to avoid sending duplicates if desired
        # self._last_report = bytes(self._report) # Optional optimization

        # Send the initial neutral report
        self._send()

    def _send(self, report=None):
        """Send the report to the host.

        :param report: The report to send. If None, send the internal ``_report``.
                       Defaults to None.
        """
        if report is None:
            report = self._report

        # Optional optimization: only send if report changed
        # current_report_bytes = bytes(report)
        # if current_report_bytes == self._last_report:
        #    return
        # self._last_report = current_report_bytes

        self._gamepad_device.send_report(report)

    def press_buttons(self, *buttons):
        """Press the given buttons.

        :param buttons: Button numbers (like ``GenericGamepad.BUTTON_1``).
        """
        button_mask = 0
        for button in buttons:
            if not 1 <= button <= 16:
                raise ValueError("Button number must be 1-16.")
            button_mask |= 1 << (button - 1)

        # Update the button bytes in the report
        self._report[1] |= button_mask & 0xFF
        self._report[2] |= (button_mask >> 8) & 0xFF
        self._send()

    def release_buttons(self, *buttons):
        """Release the given buttons.

        :param buttons: Button numbers (like ``GenericGamepad.BUTTON_1``).
        """
        button_mask = 0
        for button in buttons:
            if not 1 <= button <= 16:
                raise ValueError("Button number must be 1-16.")
            button_mask |= 1 << (button - 1)

        # Update the button bytes in the report (clear the bits)
        self._report[1] &= ~(button_mask & 0xFF)
        self._report[2] &= ~((button_mask >> 8) & 0xFF)
        self._send()

    def release_all_buttons(self):
        """Release all buttons."""
        self._report[1] = 0x00
        self._report[2] = 0x00
        self._send()

    def move_hat(self, direction=HAT_NEUTRAL):
        """Move the hat switch to the specified direction or release it.

        :param direction: A direction constant like ``GenericGamepad.HAT_TOP``
                          or ``GenericGamepad.HAT_NEUTRAL`` to release.
        """
        if not 0 <= direction <= 8:
            raise ValueError("Hat direction must be 0-7 or HAT_NEUTRAL (8).")

        # Hat value is stored in the lower 4 bits of byte 3
        # Preserve the upper 4 bits (padding)
        self._report[3] = (self._report[3] & 0xF0) | (direction & 0x0F)
        self._send()

    # pylint: disable=too-many-locals
    def move_joysticks(self, x=None, y=None, rx=None, ry=None, l2=None, r2=None):
        """Set the joystick and trigger axis positions.
        Axes are specified as integers from -127 to 127 (inclusive).
        Trigger pressure (l2, r2) are specified from 0 to 127 (inclusive).
        ``None`` means leave the axis unchanged.

        :param int x: Left joystick X axis (-127 to 127).
        :param int y: Left joystick Y axis (-127 to 127).
        :param int rx: Right joystick X axis (-127 to 127).
        :param int ry: Right joystick Y axis (-127 to 127).
        :param int l2: Left trigger pressure (0 to 127). Maps to 0-255.
        :param int r2: Right trigger pressure (0 to 127). Maps to 0-255.
        """
        # Map joystick values (-127 to 127) to HID report range (0 to 255)
        # Map trigger values (0 to 127) to HID report range (0 to 255)
        # Axis order in report: X, Y, RX, RY, L2(Z), R2(Rz) -> Indices 4, 5, 6, 7, 8, 9

        changed = False
        if x is not None:
            if not -127 <= x <= 127:
                raise ValueError("Axis value must be -127 to 127.")
            val = x + 128  # Map to 1-255, center is 128
            if val == 256:
                val = 255  # Cap at 255 for 127 input
            if self._report[4] != val:
                self._report[4] = val
                changed = True
        if y is not None:
            if not -127 <= y <= 127:
                raise ValueError("Axis value must be -127 to 127.")
            val = y + 128  # Map to 1-255, center is 128
            if val == 256:
                val = 255
            if self._report[5] != val:
                self._report[5] = val
                changed = True
        if rx is not None:
            if not -127 <= rx <= 127:
                raise ValueError("Axis value must be -127 to 127.")
            val = rx + 128  # Map to 1-255, center is 128
            if val == 256:
                val = 255
            if self._report[6] != val:
                self._report[6] = val
                changed = True
        if ry is not None:
            if not -127 <= ry <= 127:
                raise ValueError("Axis value must be -127 to 127.")
            val = ry + 128  # Map to 1-255, center is 128
            if val == 256:
                val = 255
            if self._report[7] != val:
                self._report[7] = val
                changed = True
        if l2 is not None:
            if not 0 <= l2 <= 127:
                raise ValueError("Trigger value must be 0 to 127.")
            # Map 0-127 -> 0-255. Simple scaling: value * 255 / 127
            val = round(l2 * 255 / 127)
            if val > 255:
                val = 255  # Ensure bounds
            if self._report[8] != val:
                self._report[8] = val
                changed = True
        if r2 is not None:
            if not 0 <= r2 <= 127:
                raise ValueError("Trigger value must be 0 to 127.")
            val = round(r2 * 255 / 127)
            if val > 255:
                val = 255
            if self._report[9] != val:
                self._report[9] = val
                changed = True

        if changed:
            self._send()

    def reset_all(self):
        """Release all buttons, center joysticks and triggers, set hat to neutral."""
        self.release_all_buttons()
        self.move_joysticks(x=0, y=0, rx=0, ry=0, l2=0, r2=0)
        self.move_hat(self.HAT_NEUTRAL)
        # Note: move_joysticks already calls _send if changes were made.
        # We might need one final send if only hat/buttons changed,
        # but the individual methods handle sending. A final call doesn't hurt.
        self._send()

    # --- Handling Output Reports (Rumble) ---
    # This requires periodically checking the device for received reports.
    # The `adafruit_hid` library doesn't provide a direct callback mechanism.
    # You would typically poll `_gamepad_device.get_last_received_report(RUMBLE_REPORT_ID)`
    # in your main loop.

    def get_received_rumble_report(self):
        """Check for and return the last received rumble report (Output Report ID 2).

        Returns a bytearray containing the report (Report ID + Rumble Byte),
        or None if no report has been received since the last check.

        NOTE: This relies on underlying USB stack behavior and might need
              adjustments based on the specific CircuitPython port/version.
              The user needs to call this periodically in their main loop.
        """
        RUMBLE_REPORT_ID = 5  # As defined in descriptor
        try:
            # This method might not exist or work reliably on all ports.
            # It's an attempt to get the output report data.
            report = self._gamepad_device.get_last_received_report(RUMBLE_REPORT_ID)
            # report includes the report ID if received successfully.
            if report and len(report) == 2 and report[0] == RUMBLE_REPORT_ID:
                return report  # Return the full report [ID, Value]
            return None
        except (AttributeError, NotImplementedError, ConnectionError):
            # Method not available or device issue
            # print("WARN: get_last_received_report not available or failed.")
            return None
        except Exception as e:
            # Catch other potential low-level errors
            # print(f"WARN: Error checking for rumble report: {e}")
            return None

    def get_rumble_intensity(self):
        """Checks for and returns the latest rumble intensity (0-255) received from the host.

        Returns the intensity value (int 0-255) or None if no new report.
        """
        report = self.get_received_rumble_report()
        if report:
            return report[1]  # Return the second byte (the data)
        return None
