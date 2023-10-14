# SPDX-FileCopyrightText: 2018 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_hid.consumer_control_code.ConsumerControlCode`
========================================================

* Author(s): Benjamin T. (quaxalber), Dan Halbert
"""


class ConsumerControlCode:
    """
    USB HID Consumer Control Device constants.

    This list includes virtually all consumer control codes from
    https://www.usb.org/sites/default/files/hut1_4.pdf#page=126.
    """
    

    # 15.1 Generic Consumer Control Device

    CONSUMER_CONTROL = 0x1
    """
    General consumer control device.

    Section: 15.1 Generic Consumer Control Device, Usage Type: CA"""

    NUMERIC_KEY_PAD = 0x2
    """
    A collection usage for a generic numeric keypad. On a consumer device these are commonly used for channel selection. Usages for digits can be found on the Button page where numeric values starting with 0 are assigned to Button 1, numeric value 1 to Button 2, and so on.

    Section: 15.2 Numeric Key Pad, Usage Type: NAry"""

    PROGRAMMABLE_BUTTONS = 0x3
    """
    The user defines the function of these buttons to control software applications or GUI objects. The Programmable Buttons named array contains Section 12 Button Page (0x09) usages as selectors.

    Section: 15.14 Programmable Buttons, Usage Type: NAry"""

    MICROPHONE = 0x4
    """
    Names a collection that contains usages related to an audio receiver device for recording or amplifying sounds. This usage can also be used to name a logical collection (CL) if the microphone controls are part of another device.

    Section: 15.1 Generic Consumer Control Device, Usage Type: CA"""

    HEADPHONE = 0x5
    """
    Names a collection that contains usages related to an audio output device for playing back sounds. This usage can also be used to name a logical collection (CL) if the headphone controls are part of another device.

    Section: 15.1 Generic Consumer Control Device, Usage Type: CA"""

    GRAPHIC_EQUALIZER = 0x6
    """
    This collection contains Ordinal usages. An Ordinal usage is declared for each frequency band gain control supported by the Graphic Equalizer. The value associate with the ordinal determines the gain of an individual band in an graphic equalizer. The gain varies from 0 to 100% of the total gain supported by the band. This usage requires the definition of a Usage Descriptor to identify the center frequency and Q of the filter associated with the band. This usage can also be used to name a logical collection (CL) if the equalizer controls are part of another device.

    Section: 15.1 Generic Consumer Control Device, Usage Type: CA"""

    # 15.2 Numeric Key Pad

    PLUS_10 = 0x20
    """
    Increments channel by 10.

    Section: 15.2 Numeric Key Pad, Usage Type: OSC"""

    PLUS_100 = 0x21
    """
    Increments channel by 100.

    Section: 15.2 Numeric Key Pad, Usage Type: OSC"""

    AM_PM = 0x22
    """
    Toggles between AM and PM for time entry.

    Section: 15.2 Numeric Key Pad, Usage Type: OSC"""

    # 15.3 General Controls

    POWER = 0x30
    """
    Controls the application-specific power state. For global power control, see Section 4.5 System Controls .

    Section: 15.3 General Controls, Usage Type: OOC"""

    RESET = 0x31
    """
    Resets the device. All volatile settings revert to the defaults.

    Section: 15.3 General Controls, Usage Type: OSC"""

    SLEEP = 0x32
    """
    Initiates low power state on application-specific device now.

    Section: 15.3 General Controls, Usage Type: OSC"""

    SLEEP_AFTER = 0x33
    """
    Sets inactivity timeout to a value. The

    Section: 15.3 General Controls, Usage Type: OSC"""

    SLEEP_MODE = 0x34
    """
    Cycle through available sleep delays, such as no sleeping, 5 minutes, 10 minutes, 30 minutes, etc... The last selected mode will be enabled.

    Section: 15.3 General Controls, Usage Type: RTC"""

    ILLUMINATION = 0x35
    """
    Toggles illumination of consumer control's buttons and controls on/off.

    Section: 15.3 General Controls, Usage Type: OOC"""

    FUNCTION_BUTTONS = 0x36
    """
    A collection usage for generic function buttons. On a consumer device, these are commonly used for user-assigned functions. Usages for function buttons can be found on Section 12 Button Page (0x09) where Function Button 1 is assigned to Button 1, Function Button 2 to Button 2, and so on.

    Section: 15.3 General Controls, Usage Type: NAry"""

    # 15.4 Menu Controls

    MENU = 0x40
    """
    Initiates on-device-display main menu. Sets a mode in which the other menu controls are active. In this mode, a subsequent menu press will cancel the mode.

    Section: 15.4 Menu Controls, Usage Type: OOC"""

    MENU_PICK = 0x41
    """
    Picks an item from an on-screen menu.

    Section: 15.4 Menu Controls, Usage Type: OSC"""

    MENU_UP = 0x42
    """
    Moves the selection up in a device-displayed menu.

    Section: 15.4 Menu Controls, Usage Type: OSC"""

    MENU_DOWN = 0x43
    """
    Moves the selection down in a device-displayed menu.

    Section: 15.4 Menu Controls, Usage Type: OSC"""

    MENU_LEFT = 0x44
    """
    Moves the selection left in a device-displayed menu.

    Section: 15.4 Menu Controls, Usage Type: OSC"""

    MENU_RIGHT = 0x45
    """
    Moves the selection right in a device-displayed menu.

    Section: 15.4 Menu Controls, Usage Type: OSC"""

    MENU_ESCAPE = 0x46
    """
    Backs up a level in the on-screen menu system.

    Section: 15.4 Menu Controls, Usage Type: OSC"""

    MENU_VALUE_INCREASE = 0x47
    """
    Increments the value of the currently selected menu item. For example, after using a menu to select a volume control, the user can modify the volume level using this control.

    Section: 15.4 Menu Controls, Usage Type: OSC"""

    MENU_VALUE_DECREASE = 0x48
    """
    Decrements the value of the currently selected menu item.

    Section: 15.4 Menu Controls, Usage Type: OSC"""

    # 15.5 Display Controls

    DATA_ON_SCREEN = 0x60
    """
    Superimposes state data on the monitor video. Typically, channel information is displayed.

    Section: 15.5 Display Controls, Usage Type: OOC"""

    CLOSED_CAPTION = 0x61
    """
    Enables closed-caption display.

    Section: 15.5 Display Controls, Usage Type: OOC"""

    CLOSED_CAPTION_SELECT = 0x62
    """
    Cycles through closed-caption viewing options.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    VCR_TV = 0x63
    """
    Selects a recording source for VCR.

    Section: 15.5 Display Controls, Usage Type: OOC"""

    BROADCAST_MODE = 0x64
    """
    Cycles between available broadcast modes, such as Broadcast, CATV, etc. The last selected mode is enabled.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    SNAPSHOT = 0x65
    """
    Captures the screen or image of the currently selected window.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    STILL = 0x66
    """
    Pauses playback in the currently selected window.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    PICTURE_IN_PICTURE_TOGGLE = 0x67
    """
    Toggles the Picture-in-Picture feature on and off. In typical usage, if the overlaid picture-in-picture video is not currently visible, then it becomes visible, and if it is currently visible, then it is made not visible. Optionally, upon receipt of this control the host device may cycle through multiple picture-in-picture options. For example the host may cycle through various positions of the embedded picture on the screen before cycling back to the state in which the picture-in-picture image is not visible.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    PICTURE_IN_PICTURE_SWAP = 0x68
    """
    Swaps the video sources used for the main and embedded display if the picture-in-picture feature is currently enabled on the receiving device. If the picture-in-picture feature is not enabled at the time of the receipt of this control, no action should result.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    # 15.4 Menu Controls

    RED_MENU_BUTTON = 0x69
    """
    Red menu button on the remote control is currently pressed.

    Section: 15.4 Menu Controls, Usage Type: MC"""

    GREEN_MENU_BUTTON = 0x6A
    """
    Green menu button on the remote control is currently pressed.

    Section: 15.4 Menu Controls, Usage Type: MC"""

    BLUE_MENU_BUTTON = 0x6B
    """
    Blue menu button on the remote control is currently pressed.

    Section: 15.4 Menu Controls, Usage Type: MC"""

    YELLOW_MENU_BUTTON = 0x6C
    """
    Yellow menu button on the remote control is currently pressed.

    Section: 15.4 Menu Controls, Usage Type: MC"""

    # 15.5 Display Controls

    ASPECT = 0x6D
    """
    Selects the next available supported aspect ratio option on a device which outputs or displays video. For example, common aspect ratio options are 4:3 (standard definition), 16:9 (often used to stretch a standard definition source signal to a 16:9 video screen), letter-box and anamorphic widescreen.The order in which the aspect ratios are selected is implementation specific.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    SELECT_3D_MODE = 0x6E
    """
    Selects the next available supported 3D mode on a TV or other device which displays or outputs 3D video. For example, common modes are 3D disabled, sequential frame, left-over-right format and side-by-side format. The supported modes and the order in which the device cycles through these modes is implementation specific.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    DISPLAY_BRIGHTNESS_INCREMENT = 0x6F
    """
    Brightens the display by one unit, if possible.

    Section: 15.5 Display Controls, Usage Type: RTC"""

    DISPLAY_BRIGHTNESS_DECREMENT = 0x70
    """
    Dims the display by one unit, until off.

    Section: 15.5 Display Controls, Usage Type: RTC"""

    DISPLAY_BRIGHTNESS = 0x71
    """
    Sets brightness to a value between logical min and max. Logical min is off, logical max is brightest.

    Section: 15.5 Display Controls, Usage Type: LC"""

    DISPLAY_BACKLIGHT_TOGGLE = 0x72
    """
    Toggles the backlight state between off and last known brightness or default brightness if last known is unavailable.

    Section: 15.5 Display Controls, Usage Type: OOC"""

    DISPLAY_SET_BRIGHTNESS_TO_MINIMUM = 0x73
    """
    Dims the display to minimum brightness (not off).

    Section: 15.5 Display Controls, Usage Type: OSC"""

    DISPLAY_SET_BRIGHTNESS_TO_MAXIMUM = 0x74
    """
    Brightens the display to maximum brightness.

    Section: 15.5 Display Controls, Usage Type: OSC"""

    DISPLAY_SET_AUTO_BRIGHTNESS = 0x75
    """
    Permits the display to automatically control brightness.

    Section: 15.5 Display Controls, Usage Type: OOC"""

    # 15.21 Access Controls

    CAMERA_ACCESS_ENABLED = 0x76
    """
    Enables programmatic access to camera devices.

    Section: 15.21 Access Controls, Usage Type: OOC"""

    CAMERA_ACCESS_DISABLED = 0x77
    """
    Disables programmatic access to camera devices.

    Section: 15.21 Access Controls, Usage Type: OOC"""

    CAMERA_ACCESS_TOGGLE = 0x78
    """
    Toggles the current state of the camera access control.

    Section: 15.21 Access Controls, Usage Type: OOC"""

    # 15.22 Keyboard Backlight Controls

    KEYBOARD_BRIGHTNESS_INCREMENT = 0x79
    """
    Brightens the keyboard backlight by one unit, if possible.

    Section: 15.22 Keyboard Backlight Controls, Usage Type: OSC"""

    KEYBOARD_BRIGHTNESS_DECREMENT = 0x7A
    """
    Dims the keyboard backlight by one unit, if possible.

    Section: 15.22 Keyboard Backlight Controls, Usage Type: OSC"""

    KEYBOARD_BACKLIGHT_SET_LEVEL = 0x7B
    """
    Sets the keyboard backlight brightness directly with a value.

    Section: 15.22 Keyboard Backlight Controls, Usage Type: LC"""

    KEYBOARD_BACKLIGHT_OOC = 0x7C
    """
    Turns the keyboard backlight on or off.

    Section: 15.22 Keyboard Backlight Controls, Usage Type: OOC"""

    KEYBOARD_BACKLIGHT_SET_MINIMUM = 0x7D
    """
    Dims the keyboard backlight to minimum non-off level.

    Section: 15.22 Keyboard Backlight Controls, Usage Type: OSC"""

    KEYBOARD_BACKLIGHT_SET_MAXIMUM = 0x7E
    """
    Brightens the keyboard backlight to its brightest level.

    Section: 15.22 Keyboard Backlight Controls, Usage Type: OSC"""

    KEYBOARD_BACKLIGHT_AUTO = 0x7F
    """
    Permits the keyboard to use its own brightness algorithms.

    Section: 15.22 Keyboard Backlight Controls, Usage Type: OOC"""

    # 15.6 Selection Controls

    SELECTION = 0x80
    """
    A collection usage for a number of discrete selections. On a consumer device, these are commonly used for favorite selections. Usages for the selections can be found on the Button page where the choices are assigned to Button 1 and so on.

    Section: 15.6 Selection Controls, Usage Type: NAry"""

    ASSIGN_SELECTION = 0x81
    """
    This button works in conjunction with the

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    MODE_STEP = 0x82
    """
    Steps through devices (TV, VCR, cable) in a multi-mode remote.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    RECALL_LAST = 0x83
    """
    Returns to the last selected channel or mode.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    ENTER_CHANNEL = 0x84
    """
    Interprets the previous number entry as channel information.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    ORDER_MOVIE = 0x85
    """
    Requests pay-per-view entertainment.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    CHANNEL = 0x86
    """
    Channel selection control where the range of possible values is equal to the number of channels supported by the device.

    Section: 15.6 Selection Controls, Usage Type: LC"""

    MEDIA_SELECTION = 0x87
    """
    Identifies the media source to be manipulated or displayed. This collection will contain one of the following Media Select usages.

    Section: 15.6 Selection Controls, Usage Type: NAry"""

    MEDIA_SELECT_COMPUTER = 0x88
    """
    Selects the computer display.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_TV = 0x89
    """
    Selects the television display.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_WWW = 0x8A
    """
    Selects World Wide Web access.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_DVD = 0x8B
    """
    Selects the DVD drive.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_TELEPHONE = 0x8C
    """
    Selects telephone mode.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_PROGRAM_GUIDE = 0x8D
    """
    Selects the viewing guide.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_VIDEO_PHONE = 0x8E
    """
    Selects videophone mode.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_GAMES = 0x8F
    """
    Selects gaming mode.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_MESSAGES = 0x90
    """
    Selects message mode.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_CD = 0x91
    """
    Selects the CD drive.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_VCR = 0x92
    """
    Selects the VCR.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_TUNER = 0x93
    """
    Selects the tuner.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    QUIT = 0x94
    """
    Exits the current mode.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    HELP = 0x95
    """
    Displays the help screen.

    Section: 15.6 Selection Controls, Usage Type: OOC"""

    MEDIA_SELECT_TAPE = 0x96
    """
    Select the audio tape.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_CABLE = 0x97
    """
    Selects the cable receiver.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_SATELLITE = 0x98
    """
    Selects the satellite receiver.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_SECURITY = 0x99
    """
    Selects the security status display.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_HOME = 0x9A
    """
    Selects the home system status display.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    MEDIA_SELECT_CALL = 0x9B
    """
    Selects the telephone call status display.

    Section: 15.6 Selection Controls, Usage Type: Sel"""

    CHANNEL_INCREMENT = 0x9C
    """
    C.hannel control where each activation of the control increments the current channel selection to the next available channel.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    CHANNEL_DECREMENT = 0x9D
    """
    Channel control where each activation of the control decrements the current channel selection to the next available channel.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    # 15.13 PC Theatre

    MEDIA_SELECT_SAP = 0x9E
    """
    Select Tuner using Secondary Audio Program (SAP) information.

    Section: 15.13 PC Theatre, Usage Type: Sel"""

    # 15.6 Selection Controls

    VCR_PLUS = 0xA0
    """
    Initiates (and optionally terminates) VCR Plus code entry mode.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    ONCE = 0xA1
    """
    Performs the operation once.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    DAILY = 0xA2
    """
    Performs the operation once a day.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    WEEKLY = 0xA3
    """
    Performs the operation once a week.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    MONTHLY = 0xA4
    """
    Performs the operation once a month.

    Section: 15.6 Selection Controls, Usage Type: OSC"""

    # 15.7 Transport Controls

    PLAY = 0xB0
    """
    Begins streaming linear media.

    Section: 15.7 Transport Controls, Usage Type: OOC"""

    PAUSE = 0xB1
    """
    Stops streaming linear media.

    Section: 15.7 Transport Controls, Usage Type: OOC"""

    RECORD = 0xB2
    """
    Initiates transferring input data to media.

    Section: 15.7 Transport Controls, Usage Type: OOC"""

    FAST_FORWARD = 0xB3
    """
    Initiates fast forward scan of linear media.

    Section: 15.7 Transport Controls, Usage Type: OOC"""

    REWIND = 0xB4
    """
    Initiates fast reverse scan of linear media.

    Section: 15.7 Transport Controls, Usage Type: OOC"""

    SCAN_NEXT_TRACK = 0xB5
    """
    Moves to the next chapter or track boundary.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    SCAN_PREVIOUS_TRACK = 0xB6
    """
    Moves to the previous chapter or track boundary.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    STOP = 0xB7
    """
    Halts scanning, streaming, or recording linear media.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    EJECT = 0xB8
    """
    Removes media from the player.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    RANDOM_PLAY = 0xB9
    """
    Random selection of tracks.

    Section: 15.7 Transport Controls, Usage Type: OOC"""

    SELECT_DISC = 0xBA
    """
    Attached to a collection that defines the selection of one of many disks. The allowed disk numbers are enumerated with the declaration of ordinals in the Select Disc named array.

    Section: 15.7 Transport Controls, Usage Type: NAry"""

    ENTER_DISC = 0xBB
    """
    This button works in conjunction with the

    Section: 15.7 Transport Controls, Usage Type: MC"""

    REPEAT = 0xBC
    """
    Repeat selection of tracks.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    TRACKING = 0xBD
    """
    Adjusts media tracking.

    Section: 15.7 Transport Controls, Usage Type: LC"""

    TRACK_NORMAL = 0xBE
    """
    Sets media tracking to default or automatic value.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    SLOW_TRACKING = 0xBF
    """
    Adjusts media slow tracking.

    Section: 15.7 Transport Controls, Usage Type: LC"""

    FRAME_FORWARD = 0xC0
    """
    Moves forward one video frame.

    Section: 15.7 Transport Controls, Usage Type: RTC"""

    FRAME_BACK = 0xC1
    """
    Moves back one video frame.

    Section: 15.7 Transport Controls, Usage Type: RTC"""

    # 15.8 Search Controls

    MARK = 0xC2
    """
    Marks a reference point on the media. Synonymous with the counter memory function found on some transport devices.

    Section: 15.8 Search Controls, Usage Type: OSC"""

    CLEAR_MARK = 0xC3
    """
    Removes a marked reference point from the media.

    Section: 15.8 Search Controls, Usage Type: OSC"""

    REPEAT_FROM_MARK = 0xC4
    """
    Marks the current position as the end of the block and repeat-plays the block starting from the marked beginning of the block.

    Section: 15.8 Search Controls, Usage Type: OOC"""

    RETURN_TO_MARK = 0xC5
    """
    Positions at the last detected mark and plays.

    Section: 15.8 Search Controls, Usage Type: OSC"""

    SEARCH_MARK_FORWARD = 0xC6
    """
    Searches forward for a mark.

    Section: 15.8 Search Controls, Usage Type: OSC"""

    SEARCH_MARK_BACKWARDS = 0xC7
    """
    Searches backward for a mark.

    Section: 15.8 Search Controls, Usage Type: OSC"""

    COUNTER_RESET = 0xC8
    """
    Resets the time, position, or frame counter.

    Section: 15.8 Search Controls, Usage Type: OSC"""

    SHOW_COUNTER = 0xC9
    """
    Toggles between the position counter and the time display.

    Section: 15.8 Search Controls, Usage Type: OSC"""

    # 15.7 Transport Controls

    TRACKING_INCREMENT = 0xCA
    """
    Asserting this control increments the current value of media tracking until the maximum value is reached. Typically implemented as a single button.

    Section: 15.7 Transport Controls, Usage Type: RTC"""

    TRACKING_DECREMENT = 0xCB
    """
    Asserting this control decrements the current value of media tracking until the minimum value is reached. Typically implemented as a single button.

    Section: 15.7 Transport Controls, Usage Type: RTC"""

    STOP_EJECT = 0xCC
    """
    If linear media is scanning, streaming, or recording, stops the media stream. If linear media is halted, removes the media from the player.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    PLAY_PAUSE = 0xCD
    """
    If linear media is scanning, streaming, or recording, momentarily stops the media stream. If linear media is paused, resumes streaming.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    PLAY_SKIP = 0xCE
    """
    If linear media is halted, begins streaming. If linear media is already streaming, advances to the next channel.

    Section: 15.7 Transport Controls, Usage Type: OSC"""

    # 15.3 General Controls

    VOICE_COMMAND = 0xCF
    """
    Initiates listening for Voice Command. 
        
    Section: 15.3 General Controls, Usage Type: OSC"""

    # 15.20 Game Recording Controls

    INVOKE_CAPTURE_INTERFACE = 0xD0
    """
    Invokes or dismisses the user interface that allows users to invoke game capture and broadcasting features.

    Section: 15.20 Game Recording Controls, Usage Type: Sel"""

    START_OR_STOP_GAME_RECORDING = 0xD1
    """
    Toggles video capture of the game currently being played.

    Section: 15.20 Game Recording Controls, Usage Type: Sel"""

    HISTORICAL_GAME_CAPTURE = 0xD2
    """
    Takes a recording of the last X amount of gameplay.

    Section: 15.20 Game Recording Controls, Usage Type: Sel"""

    CAPTURE_GAME_SCREENSHOT = 0xD3
    """
    Takes a screenshot of the game currently being played.

    Section: 15.20 Game Recording Controls, Usage Type: Sel"""

    SHOW_OR_HIDE_RECORDING_INDICATOR = 0xD4
    """
    Toggle the visibility of User Interface elements that indicate that recording is happening.

    Section: 15.20 Game Recording Controls, Usage Type: Sel"""

    START_OR_STOP_MICROPHONE_CAPTURE = 0xD5
    """
    Toggle the inclusion of microphone input in game recordings and broadcasting.

    Section: 15.20 Game Recording Controls, Usage Type: Sel"""

    START_OR_STOP_CAMERA_CAPTURE = 0xD6
    """
    Toggle the inclusion of webcam capture in game recordings and broadcasting.

    Section: 15.20 Game Recording Controls, Usage Type: Sel"""

    START_OR_STOP_GAME_BROADCAST = 0xD7
    """
    Start or stop broadcasting your gameplay to broadcast providers.

    Section: 15.20 Game Recording Controls, Usage Type: Sel"""

    START_OR_STOP_VOICE_DICTATION_SESSION_ = 0xD8
    """
    Starts or stops a voice dictation session. If a session is not in progress, activation will start a new dictation session. If a session is in progress, activation will stop the session. 

    Section: 15.20 Game Recording Controls, Usage Type: OOC"""

    INVOKE_OR_DISMISS_EMOJI_PICKER = 0xD9
    """
    Invokes or dismisses the emoji picker widget. If the widget is not active, it will be invoked. If the widget is active, it will be dismissed.

    Section: 15.20 Game Recording Controls, Usage Type: OOC"""

    # 15.9 Audio Controls

    VOLUME = 0xE0
    """
    Audio volume control.

    Section: 15.9 Audio Controls, Usage Type: LC"""

    BALANCE = 0xE1
    """
    Audio balance control.

    Section: 15.9 Audio Controls, Usage Type: LC"""

    MUTE = 0xE2
    """
    Audio mute control. Sets the audio output level to the minimum value without affecting the current volume level. When Mute is disabled, the previous audio level will be restored. 15.9.2

    Section: 15.9 Audio Controls, Usage Type: OOC"""

    BASS = 0xE3
    """
    Audio bass control.

    Section: 15.9 Audio Controls, Usage Type: LC"""

    TREBLE = 0xE4
    """
    Audio treble control.

    Section: 15.9 Audio Controls, Usage Type: LC"""

    BASS_BOOST = 0xE5
    """
    Enables audio bass boost.

    Section: 15.9 Audio Controls, Usage Type: OOC"""

    SURROUND_MODE = 0xE6
    """
    Steps through surround mode options.

    Section: 15.9 Audio Controls, Usage Type: OSC"""

    LOUDNESS = 0xE7
    """
    Applies boost to audio bass and treble.

    Section: 15.9 Audio Controls, Usage Type: OOC"""

    MPX = 0xE8
    """
    Enables stereo multiplexer.

    Section: 15.9 Audio Controls, Usage Type: OOC"""

    VOLUME_INCREMENT = 0xE9
    """
    Asserting this control increments the current value of audio volume until the maximum value is reached. It is typically implemented as a single button.

    Section: 15.9 Audio Controls, Usage Type: RTC"""

    VOLUME_DECREMENT = 0xEA
    """
    Asserting this control decrements the current value of audio volume until the minimum value is reached. It is typically implemented as a single button.

    Section: 15.9 Audio Controls, Usage Type: RTC"""

    # 15.10 Speed Controls

    SPEED_SELECT = 0xF0
    """
    Cycles through media speed options.

    Section: 15.10 Speed Controls, Usage Type: OSC"""

    PLAYBACK_SPEED = 0xF1
    """
    A collection of controls that allow adjustment of playback speed (in units relative to normal playback speed). Contains the selectors Standard, Long, and Extended Play.

    Section: 15.10 Speed Controls, Usage Type: NAry"""

    STANDARD_PLAY = 0xF2
    """
    Selects the VCR's SP recording speed.

    Section: 15.10 Speed Controls, Usage Type: Sel"""

    LONG_PLAY = 0xF3
    """
    Selects the VCR's LP recording speed.

    Section: 15.10 Speed Controls, Usage Type: Sel"""

    EXTENDED_PLAY = 0xF4
    """
    Selects the VCR's EP recording speed.

    Section: 15.10 Speed Controls, Usage Type: Sel"""

    SLOW = 0xF5
    """
    Enables slow speed transport motion.

    Section: 15.10 Speed Controls, Usage Type: OSC"""

    # 15.11 Home and Security Controls

    FAN_ENABLE = 0x100
    """
    Controls the state of a overhead, furnace, or ventilation fan.

    Section: 15.11 Home and Security Controls, Usage Type: OOC"""

    FAN_SPEED = 0x101
    """
    Adjusts the speed of a overhead, furnace or ventilation fan.

    Section: 15.11 Home and Security Controls, Usage Type: LC"""

    LIGHT_ENABLE = 0x102
    """
    Controls the state of a light or lamp.

    Section: 15.11 Home and Security Controls, Usage Type: OOC"""

    LIGHT_ILLUMINATION_LEVEL = 0x103
    """
    Adjusts the illumination level of a light or lamp.

    Section: 15.11 Home and Security Controls, Usage Type: LC"""

    CLIMATE_CONTROL_ENABLE = 0x104
    """
    Enables or disables a climate control system.

    Section: 15.11 Home and Security Controls, Usage Type: OOC"""

    ROOM_TEMPERATURE = 0x105
    """
    Adjusts room temperature level.

    Section: 15.11 Home and Security Controls, Usage Type: LC"""

    SECURITY_ENABLE = 0x106
    """
    Enables or disables a security system.

    Section: 15.11 Home and Security Controls, Usage Type: OOC"""

    FIRE_ALARM = 0x107
    """
    Initiates a fire alarm.

    Section: 15.11 Home and Security Controls, Usage Type: OSC"""

    POLICE_ALARM = 0x108
    """
    Initiates a police alarm.

    Section: 15.11 Home and Security Controls, Usage Type: OSC"""

    PROXIMITY = 0x109
    """
    A value indicating proximity to a sensor.

    Section: 15.11 Home and Security Controls, Usage Type: LC"""

    MOTION = 0x10A
    """
    A value indicating detection of motion.

    Section: 15.11 Home and Security Controls, Usage Type: OSC"""

    DURESS_ALARM = 0x10B
    """
    Initiates a Panic alarm Indicates a forced operation of the alarm controls under duress. Typically a silent alarm.

    Section: 15.11 Home and Security Controls, Usage Type: OSC"""

    HOLDUP_ALARM = 0x10C
    """
    Initiates a Holdup alarm. Typically a silent alarm.

    Section: 15.11 Home and Security Controls, Usage Type: OSC"""

    MEDICAL_ALARM = 0x10D
    """
    Initiates a Medical alarm.

    Section: 15.11 Home and Security Controls, Usage Type: OSC"""

    # 15.9 Audio Controls

    BALANCE_RIGHT = 0x150
    """
    Asserting this control adjusts the audio output towards the right channel until the maximum value is reached. It is typically implemented as a single button.

    Section: 15.9 Audio Controls, Usage Type: RTC"""

    BALANCE_LEFT = 0x151
    """
    Asserting this control adjusts the audio to the left channel until the maximum value is reached. It is typically implemented as a single button. 15.9.3

    Section: 15.9 Audio Controls, Usage Type: RTC"""

    BASS_INCREMENT = 0x152
    """
    Asserting this control increments the current value of the audio bass control until the maximum value is reached. It is typically implemented as a single button.

    Section: 15.9 Audio Controls, Usage Type: RTC"""

    BASS_DECREMENT = 0x153
    """
    Asserting this control decrements the current value of the audio bass control until the minimum value is reached. It is typically implemented as a single button.

    Section: 15.9 Audio Controls, Usage Type: RTC"""

    TREBLE_INCREMENT = 0x154
    """
    Asserting this control increments the current value of the audio treble control until the maximum value is reached. It is typically implemented as a single button.

    Section: 15.9 Audio Controls, Usage Type: RTC"""

    TREBLE_DECREMENT = 0x155
    """
    Asserting this control decrements the current value of the audio treble control until the minimum value is reached. It is typically implemented as a single button. 15.9.5 Other UsageName UsageType Description

    Section: 15.9 Audio Controls, Usage Type: RTC"""

    # 15.11 Home and Security Controls

    SPEAKER_SYSTEM = 0x160
    """
    This collection is used to define controls that effect all channels of an individual speaker system if the device contains controls for more than one speaker system. Note: that the controls defined in the top-level collection will be the true master controls, effecting all speaker systems. This collection can contain any of the following

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_LEFT = 0x161
    """
    A collection of controls associated with the Left channel.

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_RIGHT = 0x162
    """
    A collection of controls associated with the Right channel.

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_CENTER = 0x163
    """
    A collection of controls associated with the Center channel.

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_FRONT = 0x164
    """
    A collection of controls associated with the Front channels. To provide more detail on controls, this collection may optionally contain

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_CENTER_FRONT = 0x165
    """
    A collection of controls associated with the Center Front channels. To provide more detail on controls, this collection may optionally contain

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_SIDE = 0x166
    """
    A collection of controls associated with the Side or wall channels. To provide more detail on controls, this collection may optionally contain

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_SURROUND = 0x167
    """
    A collection of controls associated with the Surround channels. The Audio class notation for this Channel Surround is S. To provide more detail on controls, this collection may optionally contain Channel Left and Channel Right collections The Audio class notation for this Channel Surround(Channel Left) is LS. The Audio class notation for this Channel Surround(Channel Right) is RS.

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_LOW_FREQUENCY_SUBWOOFER_ENHANCEMENT = 0x168
    """
    A collection of controls associated with the Low Frequency Enhancement or channel. The Audio class notation for this channel is LFE.

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_TOP = 0x169
    """
    A collection of controls associated with the Top or overhead channel. The Audio class notation for this channel is T.

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    CHANNEL_UNKNOWN = 0x16A
    """
    A collection of controls associated with an unknown channel position.

    Section: 15.11 Home and Security Controls, Usage Type: CL"""

    # 15.13 PC Theatre

    SUB_CHANNEL = 0x170
    """
    Digital TV sub-channel selection control where the range of possible values is equal to the number of sub-channels supported by the device.

    Section: 15.13 PC Theatre, Usage Type: LC"""

    SUB_CHANNEL_INCREMENT = 0x171
    """
    Digital TV sub-channel control where each activation of the control increments the current sub-channel selection to the next available subchannel.

    Section: 15.13 PC Theatre, Usage Type: OSC"""

    SUB_CHANNEL_DECREMENT = 0x172
    """
    Digital TV sub-channel control where each activation of the control decrements the current sub-channel selection to the next available subchannel.

    Section: 15.13 PC Theatre, Usage Type: OSC"""

    ALTERNATE_AUDIO_INCREMENT = 0x173
    """
    Digital TV alternate-audio control where each activation of the control increments the current alternate-audio selection to the next available alternate-audio.

    Section: 15.13 PC Theatre, Usage Type: OSC"""

    ALTERNATE_AUDIO_DECREMENT = 0x174
    """
    Digital TV alternate-audio control where each activation of the control decrements the current alternate-audio selection to the next available alternate-audio.

    Section: 15.13 PC Theatre, Usage Type: OSC"""

    # 15.15 Application Launch Buttons

    APPLICATION_LAUNCH_BUTTONS = 0x180
    """
    This array contains Application Launch (AL) selectors.

    Section: 15.15 Application Launch Buttons, Usage Type: NAry"""

    AL_LAUNCH_BUTTON_CONFIGURATION_TOOL = 0x181
    """
    Used to associate buttons in an array of Launch Buttons with the application to be launched.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_PROGRAMMABLE_BUTTON_CONFIGURATION_TOOL = 0x182
    """
    Used to associate Buttons in an array of

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CONSUMER_CONTROL_CONFIGURATION_TOOL = 0x183
    """
    Used to associate generic controls with a sepcific consumer device or software player to receive the control input, regardless of user focus. For example, a set of Transport Controls could be associated with a DVD-ROM player that would receive the

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_WORD_PROCESSOR = 0x184
    """
    Launch word processor.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_TEXT_EDITOR = 0x185
    """
    Launch text editor.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_SPREADSHEET = 0x186
    """
    Launch spreadsheet application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_GRAPHICS_EDITOR = 0x187
    """
    Launch graphics editor.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_PRESENTATION_APP = 0x188
    """
    Launch presentation application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_DATABASE_APP = 0x189
    """
    Launch database application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_EMAIL_READER = 0x18A
    """
    Launch email reader.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_NEWSREADER = 0x18B
    """
    Launch newsreader.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_VOICEMAIL = 0x18C
    """
    Launch voicemail application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CONTACTS_ADDRESS_BOOK = 0x18D
    """
    Launch contact database manager or address book application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CALENDAR_SCHEDULE = 0x18E
    """
    Launch calendar or schedule application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_TASK_PROJECT_MANAGER = 0x18F
    """
    Launch task or project manager application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_LOG_JOURNAL_TIMECARD = 0x190
    """
    Launch log, journal or timecard application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CHECKBOOK_FINANCE = 0x191
    """
    Launch checkbook or finance application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CALCULATOR = 0x192
    """
    Launch calculator.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_A_V_CAPTURE_PLAYBACK = 0x193
    """
    Launch A/V Capture or Playback application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_LOCAL_MACHINE_BROWSER = 0x194
    """
    Launch local machine browser.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_LAN_WAN_BROWSER = 0x195
    """
    Launch LAN/WAN browser.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_INTERNET_BROWSER = 0x196
    """
    Launch internet browser.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_REMOTE_NETWORKING_ISP_CONNECT = 0x197
    """
    Launch remote networking or ISP connection.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_NETWORK_CONFERENCE = 0x198
    """
    Launch network conference application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_NETWORK_CHAT = 0x199
    """
    Launch network chat application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_TELEPHONY_DIALER = 0x19A
    """
    Launch telephony or dialer application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_LOGON = 0x19B
    """
    Launch logon.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_LOGOFF = 0x19C
    """
    Launch logoff.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_LOGON_LOGOFF = 0x19D
    """
    Launch logon or logoff depending on current state.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_TERMINAL_LOCK_SCREENSAVER = 0x19E
    """
    Launch terminal lock or screensaver.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CONTROL_PANEL = 0x19F
    """
    Launch control panel.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_COMMAND_LINE_PROCESSOR_RUN = 0x1A0
    """
    Launch command line processor (Run).

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_PROCESS_TASK_MANAGER = 0x1A1
    """
    Launch process or task manager application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_SELECT_TASK_APPLICATION = 0x1A2
    """
    Launch task or application selection application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_NEXT_TASK_APPLICATION = 0x1A3
    """
    Go to next task or application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_PREVIOUS_TASK_APPLICATION = 0x1A4
    """
    Go to previous task or application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_PREEMPTIVE_HALT_TASK_APPLICATION = 0x1A5
    """
    Initiate preemptive task/application halt.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_INTEGRATED_HELP_CENTER = 0x1A6
    """
    Launch a system wide, context-insensitive integrated help center.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_DOCUMENTS = 0x1A7
    """
    Launch Documents Browser application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_THESAURUS = 0x1A8
    """
    Launch Thesaurus application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_DICTIONARY = 0x1A9
    """
    Launch Dictionary application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_DESKTOP = 0x1AA
    """
    Display Desktop (in a windowed environment).

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_SPELL_CHECK = 0x1AB
    """
    Launch Spell Check application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_GRAMMAR_CHECK = 0x1AC
    """
    Launch Grammar Check application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_WIRELESS_STATUS = 0x1AD
    """
    Launch Wireless Status/Management application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_KEYBOARD_LAYOUT = 0x1AE
    """
    Launch Keyboard Layout Management application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_VIRUS_PROTECTION = 0x1AF
    """
    Launch Virus Protection application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_ENCRYPTION = 0x1B0
    """
    Launch Encryption Management application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_SCREEN_SAVER = 0x1B1
    """
    Launch Screen Saver application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_ALARMS = 0x1B2
    """
    Launch Timer/Alarm application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CLOCK = 0x1B3
    """
    Launch System Clock application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_FILE_BROWSER = 0x1B4
    """
    Launch System File Browser.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_POWER_STATUS = 0x1B5
    """
    Launch

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_IMAGE_BROWSER = 0x1B6
    """
    Launch Image Browser.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_AUDIO_BROWSER = 0x1B7
    """
    Launch Audio Browser.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_MOVIE_BROWSER = 0x1B8
    """
    Launch Movie Browser.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_DIGITAL_RIGHTS_MANAGER = 0x1B9
    """
    Launch Digital Rights Manager (DRM) application. This application allows users to manage digital rights or similar credentials that they have acquired or created. The focus of the credentials cache is authentication for use of digital media.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_DIGITAL_WALLET = 0x1BA
    """
    Lanches the user's Digital Wallet manager. This application manages a store of credentials whose focus is online commerce.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_INSTANT_MESSAGING = 0x1BC
    """
    Launch the user's Instant Messaging Application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_OEM_FEATURES_TIPS_TUTORIAL_BROWSER = 0x1BD
    """
    Launch web browser with URL or app specific to PC/Web Appliance/Thin Client/ Set-top Box OEM that points out features, tips, and tutorials.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_OEM_HELP = 0x1BE
    """
    Launch help file or online help specific to a PC system, thin client or terminal. Not specific to OS or specific application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_ONLINE_COMMUNITY = 0x1BF
    """
    Launch web browser with URL specific to an online community.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_ENTERTAINMENT_CONTENT_BROWSER = 0x1C0
    """
    Launch web browser with URL specific to a site featuring music downloads, streaming video, web casts, entertainment news, and reviews.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_ONLINE_SHOPPING_BROWSER = 0x1C1
    """
    Launch web browser with URL specific to an online store and a variety of leading product and services.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_SMARTCARD_INFORMATION_HELP = 0x1C2
    """
    Launch web browser with URL specific to SmartCard Information and

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_MARKET_MONITOR_FINANCE_BROWSER = 0x1C3
    """
    Launch web browser with URL specific to Market news or an application that allows a user to monitor market activity.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CUSTOMIZED_CORPORATE_NEWS_BROWSER = 0x1C4
    """
    Launch web browser with URL specific to internal corporate news.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_ONLINE_ACTIVITIES_BROWSER = 0x1C5
    """
    Launch Online Activity browser. This usage would typically launch a web browser with a URL specific to a site featuring activities centered around the hardware package that included this button. i.e. a media center device would launch a web site that had activities centered around photo shooting, video shooting, camera product reviews, etc. A gaming machine would link the user to a website with gaming related reviews and news.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_RESEARCH_SEARCH_BROWSER = 0x1C6
    """
    Launch web browser with URL or app specific to doing research like an encyclopedia or thesaurus website or app,

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_AUDIO_PLAYER = 0x1C7
    """
    Launches an audio player. This audio player can play one or many audio formats.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_MESSAGE_STATUS = 0x1C8
    """
    Used to show status of stored voice or text messages.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CONTACT_SYNC = 0x1C9
    """
    Used to initiate synchronization of device stored contact list with host system.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_NAVIGATION = 0x1CA
    """
    Launch Navigation application.

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    AL_CONTEXT_AWARE_DESKTOP_ASSISTANT = 0x1CB
    """
    Launch context-aware desktop assistant application

    Section: 15.15 Application Launch Buttons, Usage Type: Sel"""

    # 15.16 Generic GUI Application Controls

    GENERIC_GUI_APPLICATION_CONTROLS = 0x200
    """
    An array that contains generic GUI Application Control (AC) selectors.

    Section: 15.16 Generic GUI Application Controls, Usage Type: NAry"""

    AC_NEW = 0x201
    """
    Create a new document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_OPEN = 0x202
    """
    Open an existing document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_CLOSE = 0x203
    """
    Close the current document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_EXIT = 0x204
    """
    Exit the application.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_MAXIMIZE = 0x205
    """
    Maximize the window size.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_MINIMIZE = 0x206
    """
    Minimize the window size or hides the window.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SAVE = 0x207
    """
    Save the current document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PRINT = 0x208
    """
    Print the current document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PROPERTIES = 0x209
    """
    Display the properties of the current document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_UNDO = 0x21A
    """
    Undo the last action.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_COPY = 0x21B
    """
    Copy the selected object to a buffer.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_CUT = 0x21C
    """
    Copy the selected object to a buffer and then delete the object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PASTE = 0x21D
    """
    Replace the selected object with the object in the buffer.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_ALL = 0x21E
    """
    Select all objects in the current document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FIND = 0x21F
    """
    Locate an object in the current document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FIND_AND_REPLACE = 0x220
    """
    Locate an object in the current document and replace it with another object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SEARCH = 0x221
    """
    Search for documents (URLs, files, web pages, etc).

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_GO_TO = 0x222
    """
    Display a certain point in the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_HOME = 0x223
    """
    Load the designated root of a hierarchical set of objects.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_BACK = 0x224
    """
    Load the previous document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FORWARD = 0x225
    """
    Load the next document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_STOP = 0x226
    """
    Stop loading of the current document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_REFRESH = 0x227
    """
    Reload the current document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PREVIOUS_LINK = 0x228
    """
    Find and select the next hypertext link in the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_NEXT_LINK = 0x229
    """
    Find and select the next hypertext link in the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_BOOKMARKS = 0x22A
    """
    Display a list of stored links.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_HISTORY = 0x22B
    """
    Display an ordered list of previously accessed documents.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SUBSCRIPTIONS = 0x22C
    """
    Display a list of subscribed content providers.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ZOOM_IN = 0x22D
    """
    Increase the zoom factor of the document display.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ZOOM_OUT = 0x22E
    """
    Decrease the zoom factor of the document display.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ZOOM = 0x22F
    """
    Set the zoom factor of the document display.

    Section: 15.16 Generic GUI Application Controls, Usage Type: LC"""

    AC_FULL_SCREEN_VIEW = 0x230
    """
    Utilize the entire screen to display the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_NORMAL_VIEW = 0x231
    """
    Turn off Full Screen View.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_VIEW_TOGGLE = 0x232
    """
    Switch between Full Screen View and Normal View.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SCROLL_UP = 0x233
    """
    Display a portion of the document closer to the beginning of the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SCROLL_DOWN = 0x234
    """
    Display a portion of the document closer to the end of the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SCROLL = 0x235
    """
    Set the vertical offset of the display in the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: LC"""

    AC_PAN_LEFT = 0x236
    """
    Display a portion of the document closer to the left margin of the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PAN_RIGHT = 0x237
    """
    Display a portion of the document closer to the right margin of the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PAN = 0x238
    """
    Set the horizontal offset of the display in the document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: LC"""

    AC_NEW_WINDOW = 0x239
    """
    Create a new window containing same document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_TILE_HORIZONTALLY = 0x23A
    """
    Arrange all windows one above the other with no overlapping edges.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_TILE_VERTICALLY = 0x23B
    """
    Arrange all windows one beside the other with no overlapping edges.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FORMAT = 0x23C
    """
    Apply a format to the selected object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_EDIT = 0x23D
    """
    Open the selected object for editing.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_BOLD = 0x23E
    """
    Set the font to Bold.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ITALICS = 0x23F
    """
    Set the font to Italics.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_UNDERLINE = 0x240
    """
    Set the font to Underline.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_STRIKETHROUGH = 0x241
    """
    Set the font to Underline.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SUBSCRIPT = 0x242
    """
    Set the font to Underline.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SUPERSCRIPT = 0x243
    """
    Set the font to Underline.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ALL_CAPS = 0x244
    """
    Set the font to Underline.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ROTATE = 0x245
    """
    Enable rotation control.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_RESIZE = 0x246
    """
    Enable resize control.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FLIP_HORIZONTAL = 0x247
    """
    Flip horizontally.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FLIP_VERTICAL = 0x248
    """
    Flip vertically.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_MIRROR_HORIZONTAL = 0x249
    """
    Mirror horizontally.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_MIRROR_VERTICAL = 0x24A
    """
    Mirror vertically.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FONT_SELECT = 0x24B
    """
    Enable font select control.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FONT_COLOR = 0x24C
    """
    Enable font color control.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FONT_SIZE = 0x24D
    """
    Enable font size control.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_JUSTIFY_LEFT = 0x24E
    """
    Left-justify selection.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_JUSTIFY_CENTER_H = 0x24F
    """
    Center-justify horizontally.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_JUSTIFY_RIGHT = 0x250
    """
    Right-justify.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_JUSTIFY_BLOCK_H = 0x251
    """
    Block-justify horizontally.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_JUSTIFY_TOP = 0x252
    """
    Left-justify.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_JUSTIFY_CENTER_V = 0x253
    """
    Center-justify vertically.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_JUSTIFY_BOTTOM = 0x254
    """
    Bottom-justify.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_JUSTIFY_BLOCK_V = 0x255
    """
    Block-justify vertically.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INDENT_DECREASE = 0x256
    """
    Decrease paragraph indent.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INDENT_INCREASE = 0x257
    """
    Increase paragraph indent.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_NUMBERED_LIST = 0x258
    """
    Convert text to a numbered list.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_RESTART_NUMBERING = 0x259
    """
    Renumber numbered text starting at 1.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_BULLETED_LIST = 0x25A
    """
    Convert text to a bulleted list.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PROMOTE = 0x25B
    """
    Promote outline level.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_DEMOTE = 0x25C
    """
    Demote outline level.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_YES = 0x25D
    """
    Select Yes.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_NO = 0x25E
    """
    Select No.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_CANCEL = 0x25F
    """
    Select Cancel.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_CATALOG = 0x260
    """
    E-commerce Go to Catalog.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_BUY_CHECKOUT = 0x261
    """
    E-commerce Buy Order.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ADD_TO_CART = 0x262
    """
    E-commerce Add to Order List.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_EXPAND = 0x263
    """
    Expand a hierarchical List Node.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_EXPAND_ALL = 0x264
    """
    Expand all hierarchical List Nodes.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_COLLAPSE = 0x265
    """
    Collapse a hierarchical List Node.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_COLLAPSE_ALL = 0x266
    """
    Collapse all hierarchical List Nodes.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PRINT_PREVIEW = 0x267
    """
    Preview Print Output.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PASTE_SPECIAL = 0x268
    """
    Non-standard Paste.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INSERT_MODE = 0x269
    """
    Toggle Insert/Overwrite edit modes.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_DELETE = 0x26A
    """
    Delete current object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_LOCK = 0x26B
    """
    Lock display to current location in document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_UNLOCK = 0x26C
    """
    Unlock display from current location in document.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_PROTECT = 0x26D
    """
    ect selection from changes.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_UNPROTECT = 0x26E
    """
    Unprotect selection from changes.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ATTACH_COMMENT = 0x26F
    """
    Attach a comment to an object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_DELETE_COMMENT = 0x270
    """
    Delete a comment.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_VIEW_COMMENT = 0x271
    """
    View a comment attached to an object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_WORD = 0x272
    """
    Select a word at edit point.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_SENTENCE = 0x273
    """
    Select a sentence at edit point.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_PARAGRAPH = 0x274
    """
    Select a paragraph at edit point.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_COLUMN = 0x275
    """
    Select a column at edit point.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_ROW = 0x276
    """
    Select a row at edit point.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_TABLE = 0x277
    """
    Select entire table at edit point

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_OBJECT = 0x278
    """
    Select object at edit point.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_REDO_REPEAT = 0x279
    """
    Redo or

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SORT = 0x27A
    """
    Sort selection.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SORT_ASCENDING = 0x27B
    """
    Sort in ascending order.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SORT_DESCENDING = 0x27C
    """
    Sort in descending order.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FILTER = 0x27D
    """
    Filter selection.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SET_CLOCK = 0x27E
    """
    Set system clock.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_VIEW_CLOCK = 0x27F
    """
    View system clock.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SELECT_TIME_ZONE = 0x280
    """
    Set system time zone.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_EDIT_TIME_ZONES = 0x281
    """
    Edit system time zone parameters.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SET_ALARM = 0x282
    """
    Set an alarm/timer.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_CLEAR_ALARM = 0x283
    """
    Clear an alarm/timer.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SNOOZE_ALARM = 0x284
    """
    Snooze an alarm timer.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_RESET_ALARM = 0x285
    """
    Reset an alarm/timer.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SYNCHRONIZE = 0x286
    """
    Synchronize remote and local data.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SEND_RECEIVE = 0x287
    """
    Send/Receive batch messages.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SEND_TO = 0x288
    """
    Send message to a specific recipient.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_REPLY = 0x289
    """
    Reply to a message, send only to sender in FROM: list.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_REPLY_ALL = 0x28A
    """
    Reply to a message, send to all recipients in TO:, FROM: and CC: fields.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_FORWARD_MSG = 0x28B
    """
    Forward a message.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SEND = 0x28C
    """
    Send a message.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_ATTACH_FILE = 0x28D
    """
    Attach a file.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_UPLOAD = 0x28E
    """
    Upload an object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_DOWNLOAD = 0x28F
    """
    Download an object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SET_BORDERS = 0x290
    """
    Set the graphical borders of selection.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INSERT_ROW = 0x291
    """
    Insert a row.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INSERT_COLUMN = 0x292
    """
    Insert a column.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INSERT_FILE = 0x293
    """
    Insert a file.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INSERT_PICTURE = 0x294
    """
    Insert a picture.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INSERT_OBJECT = 0x295
    """
    Insert an object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_INSERT_SYMBOL = 0x296
    """
    Insert a symbol.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SAVE_AND_CLOSE = 0x297
    """
    Save and close object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_RENAME = 0x298
    """
    Rename object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_MERGE = 0x299
    """
    Merge multiple objects into a single object.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SPLIT = 0x29A
    """
    Divide a single object into multiple objects. 

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_DISTRIBUTE_HORIZONTALLY = 0x29B
    """
    Space objects evenly along a horizontal axis.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_DISTRIBUTE_VERTICALLY = 0x29C
    """
    Space objects evenly along a vertical axis.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_NEXT_KEYBOARD_LAYOUT_SELECT = 0x29D
    """
    Switch through set of keyboard layouts.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_NAVIGATION_GUIDANCE = 0x29E
    """
    Play/re-play the last navigation guidance prompt.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_DESKTOP_SHOW_ALL_WINDOWS = 0x29F
    """
    Show all running Desktop windows.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SOFT_KEY_LEFT = 0x2A0
    """
    Function assigned to left soft key when display is under host control.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_SOFT_KEY_RIGHT = 0x2A1
    """
    Function assigned to right soft key when display is under host control.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_DESKTOP_SHOW_ALL_APPLICATIONS = 0x2A2
    """
    Show all user applications.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    AC_IDLE_KEEP_ALIVE = 0x2B0
    """
    Sent periodically when no keys are pressed to indicate that the devices is still active.

    Section: 15.16 Generic GUI Application Controls, Usage Type: Sel"""

    # 15.18 Descriptive Controls

    EXTENDED_KEYBOARD_ATTRIBUTES_COLLECTION = 0x2C0
    """
    Declares a Logical Collection containing extended attributes for a keyboard. The descriptive controls must be enclosed within a Logical Collection tagged with this usage, within a Generic Desktop(Keyboard) Top-Level Application Collection.

    Section: 15.18 Descriptive Controls, Usage Type: CL"""

    KEYBOARD_FORM_FACTOR = 0x2C1
    """
    • 0: Unknown Form Factor.\n    • 1: Full-Size keyboard.\n    • 2: Compact keyboard. Such keyboards are less than 13" wide.

    Section: 15.18 Descriptive Controls, Usage Type: SV"""

    KEYBOARD_KEY_TYPE = 0x2C2
    """
    • 0: Unknown Key Type.\n    • 1: Full-travel keys.\n    • 2: Low-travel keys such as those on laptop keyboards.\n    • 3: Zero-travel or virtual keys.

    Section: 15.18 Descriptive Controls, Usage Type: SV"""

    KEYBOARD_PHYSICAL_LAYOUT = 0x2C3
    """
    The usage does not refer to the legend set printed on the keys, but only to the physical keyset layout, defined by the relative location and shape of the textual keys in relation to each other. This usage indicates which of the de facto standard physical layouts to which the keyboard conforms. These layouts are commonly understood.\n    • 0: Unknown Layout.\n    • 1: 101 (e.g. US)\n    • 2: 103 (Korea)\n    • 3: 102 (e.g. German)\n    • 4: 104 (e.g. ABNT Brazil)\n    • 5: 106 (DOS/V Japan)\n    • 6: Vendor-specific - If specified, 'Vendor-Specific Keyboard Physical Layout' must also be specified.

    Section: 15.18 Descriptive Controls, Usage Type: SV"""

    VENDOR_SPECIFIC_KEYBOARD_PHYSICAL_LAYOUT = 0x2C4
    """
    A numeric identifier of the particular Vendor-specific Keyboard Physical Layout. Values for this field are defined by the hardware vendor but 0x00 is defined to not specify a Vendor-specific Keyboard Physical Layout. If non-zero, 'Keyboard Physical Layout' must have value 0x06. If this identifier is 0x00, 'Keyboard Physical Layout' must not have the value 0x06. If 'Keyboard Physical Layout' is omitted, 'Vendor-Specific Keyboard Physical Layout' must also be omitted.

    Section: 15.18 Descriptive Controls, Usage Type: SV"""

    KEYBOARD_IETF_LANGUAGE_TAG_INDEX = 0x2C5
    """
    String index of a String Descriptor having an IETF Language Tag. This Language Tag specifies the intended primary locale of the keyboard legend set, conformant to IETF BCP 473 or its successor. Operating systems may use this information to help select a layout that maps keyboard usages to textual glyphs. This specification does not specify the exact glyph sets, as small variances may apply in particular implementations. If an appropriate IETF Language Tag is not available, such as for custom, adaptive or new layouts, the control should be omitted or set to 0x00.

    Section: 15.18 Descriptive Controls, Usage Type: SV"""

    IMPLEMENTED_KEYBOARD_INPUT_ASSIST_CONTROLS = 0x2C6
    """
    Bitmap for physically implemented controls. The input report field for Keyboard Input Assist controls may be declared as an array using Usage Min and Usage Max tags, but the keyboard is not required to implement every control in that range. However, host software may need to know which controls are actually implemented in order to present an appropriate user interface.\n    • All 0: No Keyboard Input Assist controls are implemented.\n    • Bit 0: Previous Suggestion\n    • Bit 1: Next Suggestion\n    • Bit 2: Previous Suggestion Group\n    • Bit 3: Next Suggestion Group\n    • Bit 4: Accept Suggestion\n    • Bit 5: Cancel Suggestion All other bits reserved.

    Section: 15.18 Descriptive Controls, Usage Type: SV"""

    # 15.19 Input Assist Selectors

    KEYBOARD_INPUT_ASSIST_PREVIOUS = 0x2C7
    """
    Selects the previous Keyboard Assist element, if any.

    Section: 15.19 Input Assist Selectors, Usage Type: Sel"""

    KEYBOARD_INPUT_ASSIST_NEXT = 0x2C8
    """
    Selects the next Keyboard Input Assist element, if any.

    Section: 15.19 Input Assist Selectors, Usage Type: Sel"""

    KEYBOARD_INPUT_ASSIST_PREVIOUS_GROUP = 0x2C9
    """
    Highlights the previous Keyboard Input Assist element group, if any.

    Section: 15.19 Input Assist Selectors, Usage Type: Sel"""

    KEYBOARD_INPUT_ASSIST_NEXT_GROUP = 0x2CA
    """
    Highlights the previous Keyboard Input Assist element group, if any.

    Section: 15.19 Input Assist Selectors, Usage Type: Sel"""

    KEYBOARD_INPUT_ASSIST_ACCEPT = 0x2CB
    """
    Commits the selected Keyboard Input Assist element.

    Section: 15.19 Input Assist Selectors, Usage Type: Sel"""

    KEYBOARD_INPUT_ASSIST_CANCEL = 0x2CC
    """
    Cancels Keyboard Input Assist for the current input element boundary.

    Section: 15.19 Input Assist Selectors, Usage Type: Sel"""

    # 15.23 Privacy Screen Controls

    PRIVACY_SCREEN_TOGGLE = 0x2D0
    """
    Toggles state of privacy screen.

    Section: 15.23 Privacy Screen Controls, Usage Type: OOC"""

    PRIVACY_SCREEN_LEVEL_DECREMENT = 0x2D1
    """
    Decrease level of privacy screen.

    Section: 15.23 Privacy Screen Controls, Usage Type: RTC"""

    PRIVACY_SCREEN_LEVEL_INCREMENT = 0x2D2
    """
    Increase level of privacy screen.

    Section: 15.23 Privacy Screen Controls, Usage Type: RTC"""

    PRIVACY_SCREEN_LEVEL_MINIMUM = 0x2D3
    """
    Engage lowest level of privacy screen.

    Section: 15.23 Privacy Screen Controls, Usage Type: OSC"""

    PRIVACY_SCREEN_LEVEL_MAXIMUM = 0x2D4
    """
    Engage highest level of privacy screen.

    Section: 15.23 Privacy Screen Controls, Usage Type: OSC"""

    # 15.17 Contact List Controls

    CONTACT_EDITED = 0x500
    """
    True if the contact record has been changed by the device since it was last stored.

    Section: 15.17 Contact List Controls, Usage Type: OOC"""

    CONTACT_ADDED = 0x501
    """
    True if the contact record has been added by the device since it was last stored.

    Section: 15.17 Contact List Controls, Usage Type: OOC"""

    CONTACT_RECORD_ACTIVE = 0x502
    """
    If true the contact record is active, if false the record is not currently in use.

    Section: 15.17 Contact List Controls, Usage Type: OOC"""

    CONTACT_INDEX = 0x503
    """
    Indicates which record in the list of contacts is being stored or retrieved, with the Logical Minimum being the first contact record on the device and Logical Maximum being the last.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_NICKNAME = 0x504
    """
    Nickname displayed for the contact.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_FIRST_NAME = 0x505
    """
    Contact's given name.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_LAST_NAME = 0x506
    """
    Contact's surname.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_FULL_NAME = 0x507
    """
    Contact's full name including first and last names.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_PHONE_NUMBER_PERSONAL = 0x508
    """
    Contact's personal phone number.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_PHONE_NUMBER_BUSINESS = 0x509
    """
    Contact's office phone number.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_PHONE_NUMBER_MOBILE = 0x50A
    """
    Contact's mobile phone number.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_PHONE_NUMBER_PAGER = 0x50B
    """
    Contact's paging device number.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_PHONE_NUMBER_FAX = 0x50C
    """
    Contact's facsimile number.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_PHONE_NUMBER_OTHER = 0x50D
    """
    Contact's uncategorized phone number.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_EMAIL_PERSONAL = 0x50E
    """
    Contact's personal email address.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_EMAIL_BUSINESS = 0x50F
    """
    Contact's business email address.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_EMAIL_OTHER = 0x510
    """
    Contact's uncategorized email address.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_EMAIL_ID = 0x511
    """
    Contact's primary email address.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_SPEED_DIAL_NUMBER = 0x512
    """
    The speed dial shortcut key sequence assigned to this contact.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_STATUS_FLAG = 0x513
    """
    Buffered Byte array of the status for each contact using the status OOC usages defined above.

    Section: 15.17 Contact List Controls, Usage Type: DV"""

    CONTACT_MISC = 0x514
    """
    unformatted binary data associated with this contact record.

    Section: 15.17 Contact List Controls, Usage Type: DV"""
