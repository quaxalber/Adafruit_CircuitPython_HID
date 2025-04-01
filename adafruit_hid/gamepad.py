import struct
from . import find_device

try:
    from typing import Sequence, Optional, Dict
except ImportError:
    pass


class Gamepad:
    """
    Enhanced gamepad supporting multiple axes, buttons, triggers, and hat switches.
    """

    # Axis ranges
    AXIS_MIN = -32768
    AXIS_MAX = 32767
    TRIGGER_MIN = 0
    TRIGGER_MAX = 255
    HAT_MIN = -1
    HAT_MAX = 1

    def __init__(self, devices: Sequence):
        """Initialize gamepad with enhanced features.

        :param devices: List of available HID devices
        """
        self._gamepad_device = find_device(devices, usage_page=0x1, usage=0x05)
        if not self._gamepad_device:
            raise RuntimeError("No gamepad device found")

        # Extended report size to accommodate all controls (32 bytes)
        self._report = bytearray(32)  # Changed from 16 to 32

        # Extended button state (32 bits)
        self._buttons_state = 0

        # All possible axes
        self._axes: Dict[str, int] = {
            # Main analog sticks
            "lx": 0,
            "ly": 0,  # Left stick
            "rx": 0,
            "ry": 0,  # Right stick
            # Triggers
            "lt": 0,
            "rt": 0,  # Analog triggers
            # Additional controls
            "throttle": 0,  # Throttle
            "rudder": 0,  # Rudder
            "wheel": 0,  # Steering wheel
            "gas": 0,  # Gas pedal
            "brake": 0,  # Brake pedal
        }

        # Multiple HAT switches
        self._hats: Dict[str, Dict[str, int]] = {
            "hat0": {"x": 0, "y": 0},  # Main D-pad
            "hat1": {"x": 0, "y": 0},  # Additional HAT 1
            "hat2": {"x": 0, "y": 0},  # Additional HAT 2
            "hat3": {"x": 0, "y": 0},  # Additional HAT 3
        }

    #    self.reset()

    def reset(self) -> None:
        """Reset all controls to initial state."""
        self._buttons_state = 0
        for axis in self._axes:
            self._axes[axis] = 0
        for hat in self._hats.values():
            hat["x"] = 0
            hat["y"] = 0
        self._send()

    def press(self, *buttons: int) -> None:
        """Press and hold the given buttons.

        :param buttons: Button constants to press (BTN_*)
        """
        for button in buttons:
            self._buttons_state |= button
        self._send()

    def release(self, *buttons: int) -> None:
        """Release the given buttons.

        :param buttons: Button constants to release (BTN_*)
        """
        for button in buttons:
            self._buttons_state &= ~button
        self._send()

    def move_axes(self, **kwargs: int) -> None:
        """Update axes positions with bounds checking.

        Valid kwargs:
        - lx, ly, rx, ry: -32768 to 32767
        - lt, rt, throttle, rudder, gas, brake: 0 to 255
        - wheel: -32768 to 32767
        """
        for axis, value in kwargs.items():
            if axis not in self._axes:
                raise ValueError(f"Invalid axis: {axis}")

            # Apply appropriate range checking based on axis type
            if axis in ("lt", "rt", "throttle", "rudder", "gas", "brake"):
                if not self.TRIGGER_MIN <= value <= self.TRIGGER_MAX:
                    raise ValueError(
                        f"{axis} must be between {self.TRIGGER_MIN} and {self.TRIGGER_MAX}"
                    )
            else:  # Main axes and wheel
                if not self.AXIS_MIN <= value <= self.AXIS_MAX:
                    raise ValueError(
                        f"{axis} must be between {self.AXIS_MIN} and {self.AXIS_MAX}"
                    )

            self._axes[axis] = value
        self._send()

    def set_hat(
        self, hat_id: str = "hat0", x: Optional[int] = None, y: Optional[int] = None
    ) -> None:
        """Set HAT switch position.

        :param hat_id: HAT switch identifier ("hat0" through "hat3")
        :param x: X axis value (-1, 0, 1)
        :param y: Y axis value (-1, 0, 1)
        """
        if hat_id not in self._hats:
            raise ValueError(f"Invalid HAT switch: {hat_id}")

        if x is not None:
            if not self.HAT_MIN <= x <= self.HAT_MAX:
                raise ValueError(
                    f"HAT X must be between {self.HAT_MIN} and {self.HAT_MAX}"
                )
            self._hats[hat_id]["x"] = x

        if y is not None:
            if not self.HAT_MIN <= y <= self.HAT_MAX:
                raise ValueError(
                    f"HAT Y must be between {self.HAT_MIN} and {self.HAT_MAX}"
                )
            self._hats[hat_id]["y"] = y

        self._send()

    def _send(self) -> None:
        """Send HID report with current state."""
        struct.pack_into(
            "<IHHHHBBBBBBBBBBBB",  # Extended format to support all controls
            self._report,
            0,
            self._buttons_state,  # 32-bit button state
            self._axes["lx"] & 0xFFFF,  # Left stick X
            self._axes["ly"] & 0xFFFF,  # Left stick Y
            self._axes["rx"] & 0xFFFF,  # Right stick X
            self._axes["ry"] & 0xFFFF,  # Right stick Y
            self._axes["lt"] & 0xFF,  # Left trigger
            self._axes["rt"] & 0xFF,  # Right trigger
            self._axes["throttle"] & 0xFF,  # Throttle
            self._axes["rudder"] & 0xFF,  # Rudder
            self._axes["wheel"] & 0xFF,  # Wheel (low byte)
            (self._axes["wheel"] >> 8) & 0xFF,  # Wheel (high byte)
            self._axes["gas"] & 0xFF,  # Gas
            self._axes["brake"] & 0xFF,  # Brake
            # HAT switches packed as 4 pairs of 4-bit values
            (self._hats["hat0"]["x"] & 0x0F) | ((self._hats["hat0"]["y"] & 0x0F) << 4),
            (self._hats["hat1"]["x"] & 0x0F) | ((self._hats["hat1"]["y"] & 0x0F) << 4),
            (self._hats["hat2"]["x"] & 0x0F) | ((self._hats["hat2"]["y"] & 0x0F) << 4),
            (self._hats["hat3"]["x"] & 0x0F) | ((self._hats["hat3"]["y"] & 0x0F) << 4),
        )
        self._gamepad_device.send_report(self._report)
