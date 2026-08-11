# SPDX-FileCopyrightText: 2017 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_hid.mouse.Mouse`
====================================================

* Author(s): Dan Halbert
"""

from .keycode import MouseButton
from . import find_device

try:
    from typing import Optional, Sequence

    import usb_hid
except ImportError:
    pass


class _MouseReportFormat:
    button_mask = MouseButton.LEFT | MouseButton.MIDDLE | MouseButton.RIGHT | MouseButton.SIDE | MouseButton.EXTRA
    report_length = 4
    report_id = None
    xy_limit = 127
    wheel_limit = 127
    pan_limit = 0

    def fill_movement_report(self, report: bytearray, x: int, y: int, wheel: int, pan: int) -> None:
        report[1] = x & 0xFF
        report[2] = y & 0xFF
        report[3] = wheel & 0xFF

    def clear_movement_report(self, report: bytearray) -> None:
        for index in range(1, self.report_length):
            report[index] = 0

    def fill_buttons(self, report: bytearray, buttons: int) -> bool:
        buttons &= self.button_mask
        if buttons == 0:
            return False
        report[0] |= buttons
        return True

    def clear_buttons(self, report: bytearray, buttons: int) -> bool:
        buttons &= self.button_mask
        if buttons == 0:
            return False
        report[0] &= ~buttons
        return True

    def clear_all_buttons(self, report: bytearray) -> None:
        report[0] = 0


class _BootMouseReportFormat(_MouseReportFormat):
    button_mask = MouseButton.LEFT | MouseButton.MIDDLE | MouseButton.RIGHT


class _MouseExReportFormat(_MouseReportFormat):
    button_mask = (
        MouseButton.LEFT
        | MouseButton.MIDDLE
        | MouseButton.RIGHT
        | MouseButton.SIDE
        | MouseButton.EXTRA
        | MouseButton.FORWARD
        | MouseButton.BACK
        | MouseButton.TASK
    )
    report_length = 7
    xy_limit = 32767
    pan_limit = 127

    def fill_movement_report(self, report: bytearray, x: int, y: int, wheel: int, pan: int) -> None:
        report[1] = x & 0xFF
        report[2] = (x >> 8) & 0xFF
        report[3] = y & 0xFF
        report[4] = (y >> 8) & 0xFF
        report[5] = wheel & 0xFF
        report[6] = pan & 0xFF


def _report_format_for_device(device: usb_hid.Device) -> _MouseReportFormat:
    descriptor = bytes(getattr(device, "descriptor", b""))
    known_formats = (
        (bytes(usb_hid.Device.BOOT_MOUSE.descriptor), _BootMouseReportFormat),
        (bytes(usb_hid.Device.MOUSE.descriptor), _MouseReportFormat),
        (bytes(usb_hid.Device.MOUSE_EX.descriptor), _MouseExReportFormat),
    )
    for known_descriptor, report_format_type in known_formats:
        if descriptor == known_descriptor:
            return report_format_type()
    raise ValueError("Unsupported mouse HID report descriptor.")


class Mouse:
    """Send USB HID mouse reports."""

    LEFT_BUTTON = MouseButton.LEFT
    """Left mouse button."""
    RIGHT_BUTTON = MouseButton.RIGHT
    """Right mouse button."""
    MIDDLE_BUTTON = MouseButton.MIDDLE
    """Middle mouse button."""
    SIDE_BUTTON = MouseButton.SIDE
    """Side button."""
    EXTRA_BUTTON = MouseButton.EXTRA
    """Extra button."""
    FORWARD_BUTTON = MouseButton.FORWARD
    """Forward mouse button."""
    BACK_BUTTON = MouseButton.BACK
    """Back mouse button."""
    TASK_BUTTON = MouseButton.TASK
    """Task button."""

    def __init__(self, devices: Sequence[usb_hid.Device], timeout: Optional[int] = None) -> None:
        """Create a Mouse object that will send USB mouse HID reports.

        :param timeout: Time in seconds to wait for USB to become ready before timing out.
          Defaults to None to wait indefinitely.

        Devices can be a sequence of devices that includes a keyboard device or a keyboard device
        itself. A device is any object that implements ``send_report()``, ``usage_page`` and
        ``usage``.
        """
        self._mouse_device = find_device(devices, usage_page=0x1, usage=0x02, timeout=timeout)
        self._report_format = _report_format_for_device(self._mouse_device)
        self.report = bytearray(self._report_format.report_length)

    def __str__(self):
        return str(self._mouse_device)

    def press(self, buttons: int) -> None:
        """Press the given mouse buttons.

        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.

        Examples::

            # Press the left button.
            m.press(Mouse.LEFT_BUTTON)

            # Press the left and right buttons simultaneously.
            m.press(Mouse.LEFT_BUTTON | Mouse.RIGHT_BUTTON)
        """
        if self._report_format.fill_buttons(self.report, buttons):
            self._send_no_move()

    def release(self, buttons: int) -> None:
        """Release the given mouse buttons.

        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.
        """
        if self._report_format.clear_buttons(self.report, buttons):
            self._send_no_move()

    def release_all(self) -> None:
        """Release all the mouse buttons."""
        self._report_format.clear_all_buttons(self.report)
        self._send_no_move()

    def click(self, buttons: int) -> None:
        """Press and release the given mouse buttons.

        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.

        Examples::

            # Click the left button.
            m.click(Mouse.LEFT_BUTTON)

            # Double-click the left button.
            m.click(Mouse.LEFT_BUTTON)
            m.click(Mouse.LEFT_BUTTON)
        """
        self.press(buttons)
        self.release(buttons)

    def move(self, x: int = 0, y: int = 0, wheel: int = 0, pan: int = 0) -> None:
        """Move the mouse and turn the wheel as directed.

        :param x: Move the mouse along the x axis. Negative is to the left, positive
            is to the right.
        :param y: Move the mouse along the y axis. Negative is upwards on the display,
            positive is downwards.
        :param wheel: Rotate the wheel this amount. Negative is toward the user, positive
            is away from the user. The scrolling effect depends on the host.
        :param pan: Pan (horizontal scroll) this amount. Negative is to the left,
            positive is to the right. Ignored if the mouse report format does not
            support pan.

        Examples::

            # Move 100 to the left. Do not move up and down. Do not roll the scroll wheel.
            m.move(-100, 0, 0)
            # Same, with keyword arguments.
            m.move(x=-100)

            # Move diagonally to the upper right.
            m.move(50, 20)
            # Same.
            m.move(x=50, y=-20)

            # Roll the mouse wheel away from the user.
            m.move(wheel=1)
        """
        if self._report_format.pan_limit == 0:
            pan = 0

        while x != 0 or y != 0 or wheel != 0 or pan != 0:
            partial_x = self._limit(x, self._report_format.xy_limit)
            partial_y = self._limit(y, self._report_format.xy_limit)
            partial_wheel = self._limit(wheel, self._report_format.wheel_limit)
            partial_pan = self._limit(pan, self._report_format.pan_limit)
            self._report_format.fill_movement_report(self.report, partial_x, partial_y, partial_wheel, partial_pan)
            self._send_report()
            x -= partial_x
            y -= partial_y
            wheel -= partial_wheel
            pan -= partial_pan

    def _send_no_move(self) -> None:
        """Send a button-only report."""
        self._report_format.clear_movement_report(self.report)
        self._send_report()

    def _send_report(self) -> None:
        if self._report_format.report_id is None:
            self._mouse_device.send_report(self.report)
        else:
            self._mouse_device.send_report(self.report, self._report_format.report_id)

    @staticmethod
    def _limit(dist: int, limit: int) -> int:
        return min(limit, max(-limit, dist))
