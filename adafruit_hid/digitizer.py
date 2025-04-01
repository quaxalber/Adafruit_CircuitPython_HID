from . import find_device

try:
    from typing import Sequence, Optional
except ImportError:
    pass


class Digitizer:
    """Send HID Digitizer reports."""

    def __init__(self, devices: Sequence):
        self._digitizer_device = find_device(devices, usage_page=0x0D, usage=0x02)
        if not self._digitizer_device:
            raise RuntimeError("No digitizer device found")

        # Initialize state tracking
        self._tracking_id = 0
        self._tool_type = 0
        self._width_major = 0
        self._width_minor = 0
        self._orientation = 0
        self._blob_id = 0
        self._misc = 0

        try:
            self._report = bytearray(32)
            self.reset()
        except OSError as e:
            raise RuntimeError("Failed to initialize digitizer device") from e

    def reset(self) -> None:
        """Reset all digitizer state to default values."""
        self._report = bytearray(32)
        self._tracking_id = 0
        self._tool_type = 0
        self._send()

    def update(
        self,
        x: int = 0,
        y: int = 0,
        pressure: int = 0,
        x_tilt: int = 0,
        y_tilt: int = 0,
        tool_type: int = 0,
        tip_switch: bool = False,
        barrel_switch: bool = False,
        second_barrel_switch: bool = False,
        eraser: bool = False,
        invert: bool = False,
        in_range: bool = True,
        distance: int = 0,
        touch_major: int = 0,
        touch_minor: int = 0,
        width_major: int = 0,
        width_minor: int = 0,
        orientation: int = 0,
        slot: Optional[int] = None,
        tracking_id: Optional[int] = None,
        blob_id: Optional[int] = None,
        position_x: Optional[int] = None,
        position_y: Optional[int] = None,
        mt_pressure: Optional[int] = None,
        misc: Optional[int] = None,
        mt_tool_type: Optional[int] = None,
    ) -> None:
        """Update digitizer state with all possible parameters from evdev mappings.

        :param x: X coordinate (0-32767)
        :param y: Y coordinate (0-32767)
        :param pressure: Pressure value (0-8191)
        :param x_tilt: X tilt angle (-127-127)
        :param y_tilt: Y tilt angle (-127-127)
        :param tool_type: Type of tool being used (0-15)
        :param tip_switch: True if tip is pressed
        :param barrel_switch: True if first barrel button is pressed
        :param second_barrel_switch: True if second barrel button is pressed
        :param eraser: True if eraser is active
        :param invert: True if tool is inverted
        :param in_range: True if tool is in detection range
        :param distance: Hover distance (0-255)
        :param touch_major: Major axis of touch (0-255)
        :param touch_minor: Minor axis of touch (0-255)
        :param width_major: Major axis of approaching tool (0-255)
        :param width_minor: Minor axis of approaching tool (0-255)
        :param orientation: Orientation (-127-127)
        :param slot: Active slot index (0-15)
        :param tracking_id: Contact identifier (0-63)
        :param blob_id: Blob ID (0-65535)
        :param position_x: Multi-touch X position (0-32767)
        :param position_y: Multi-touch Y position (0-32767)
        :param mt_pressure: Multi-touch pressure (0-255)
        :param misc: Miscellaneous data (0-65535)
        :param mt_tool_type: Multi-touch tool type (0-15)
        """
        # Input validation
        if not (0 <= x <= 32767):
            raise ValueError("X coordinate must be 0-32767")
        if not (0 <= y <= 32767):
            raise ValueError("Y coordinate must be 0-32767")
        if not (0 <= pressure <= 8191):
            raise ValueError("Pressure must be 0-8191")
        if not (-127 <= x_tilt <= 127):
            raise ValueError("X tilt must be -127-127")
        if not (-127 <= y_tilt <= 127):
            raise ValueError("Y tilt must be -127-127")
        if not (0 <= distance <= 255):
            raise ValueError("Distance must be 0-255")
        if not (0 <= touch_major <= 255):
            raise ValueError("Touch major must be 0-255")
        if not (0 <= touch_minor <= 255):
            raise ValueError("Touch minor must be 0-255")
        if not (-127 <= orientation <= 127):
            raise ValueError("Orientation must be -127-127")
        if not (0 <= tool_type <= 15):
            raise ValueError("Tool type must be 0-15")
        if misc is not None and not (0 <= misc <= 65535):
            raise ValueError("Misc must be 0-65535")
        if mt_tool_type is not None and not (0 <= mt_tool_type <= 15):
            raise ValueError("MT tool type must be 0-15")
        if position_x is not None and not (0 <= position_x <= 32767):
            raise ValueError("Position X must be 0-32767")
        if position_y is not None and not (0 <= position_y <= 32767):
            raise ValueError("Position Y must be 0-32767")
        if mt_pressure is not None and not (0 <= mt_pressure <= 255):
            raise ValueError("MT pressure must be 0-255")
        if slot is not None and not (0 <= slot <= 15):
            raise ValueError("Slot must be 0-15")
        # For tracking_id, the HID descriptor supports 6 bits (0-63)
        if tracking_id is not None and not (0 <= tracking_id <= 63):
            raise ValueError("Tracking ID must be 0-63")

        # If no explicit tracking_id is provided but a slot is, use the slot value.
        if tracking_id is None and slot is not None:
            tracking_id = slot

        if tracking_id is not None:
            self._tracking_id = tracking_id

        # Tool type and button bits (byte 1)
        tool_bits = (tool_type & 0x0F) << 4
        button_bits = (
            (1 if tip_switch else 0)
            | ((1 if barrel_switch else 0) << 1)
            | ((1 if second_barrel_switch else 0) << 2)
            | ((1 if eraser else 0) << 3)
            | ((1 if invert else 0) << 4)
        )
        self._report[1] = tool_bits | button_bits

        # Pack the In Range flag and Contact Identifier (6 bits) into a single byte (byte 2)
        self._report[2] = (1 if in_range else 0) | ((self._tracking_id & 0x3F) << 1)

        # X, Y coordinates (bytes 3-6)
        self._report[3] = x & 0xFF
        self._report[4] = (x >> 8) & 0xFF
        self._report[5] = y & 0xFF
        self._report[6] = (y >> 8) & 0xFF

        # Pressure (13 bits: bytes 7-8)
        self._report[7] = pressure & 0xFF
        self._report[8] = (pressure >> 8) & 0x1F

        # Distance and tilt (bytes 9-11)
        self._report[9] = distance & 0xFF
        self._report[10] = x_tilt & 0xFF
        self._report[11] = y_tilt & 0xFF

        # Touch and width measurements (bytes 12-15)
        self._report[12] = touch_major & 0xFF
        self._report[13] = touch_minor & 0xFF
        self._report[14] = width_major & 0xFF
        self._report[15] = width_minor & 0xFF

        # Orientation (byte 16)
        self._report[16] = orientation & 0xFF

        # Multi-touch specific data
        if position_x is not None:
            self._report[17] = position_x & 0xFF
            self._report[18] = (position_x >> 8) & 0xFF
        if position_y is not None:
            self._report[19] = position_y & 0xFF
            self._report[20] = (position_y >> 8) & 0xFF
        if mt_pressure is not None:
            self._report[21] = mt_pressure & 0xFF
        if mt_tool_type is not None:
            self._report[22] = mt_tool_type & 0xFF

        # Misc data (bytes 23-24)
        if misc is not None:
            self._report[23] = misc & 0xFF
            self._report[24] = (misc >> 8) & 0xFF

        # Blob ID (bytes 25-26)
        if blob_id is not None:
            self._report[25] = blob_id & 0xFF
            self._report[26] = (blob_id >> 8) & 0xFF

        self._send()

    def _send(self) -> None:
        """Send the current report."""
        # Set Report ID (byte 0)
        self._report[0] = 0x05
        self._digitizer_device.send_report(self._report)

    def press(self, *buttons: int) -> None:
        """Press and hold the given digitizer buttons.

        :param buttons: Button constants to press (from DigitizerButton class)
        """
        for button in buttons:
            # Update the button state in byte 1
            self._report[1] |= button
        self._send()

    def release(self, *buttons: int) -> None:
        """Release the given digitizer buttons.

        :param buttons: Button constants to release (from DigitizerButton class)
        """
        for button in buttons:
            # Clear the button state in byte 1
            self._report[1] &= ~button
        self._send()

    def release_all(self) -> None:
        """Release all digitizer buttons."""
        # Clear all button states while preserving tool type
        tool_bits = self._report[1] & 0xF0  # Keep the tool type bits
        self._report[1] = tool_bits
        self._send()
