


import wmi

def get_brightness():
    """Get current brightness using WMI."""
    w = wmi.WMI(namespace='wmi')
    brightness = w.WmiMonitorBrightness()[0].CurrentBrightness
    return brightness

def set_brightness(level):
    """Set brightness using WMI."""
    w = wmi.WMI(namespace='wmi')
    methods = w.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(1, level)

def compare_brightness(prev, current):
    """Compare brightness levels."""
    return "Increased" if current > prev else "Decreased" if current < prev else "Unchanged"

# Main Execution Block
if __name__ == "__main__":
    prev_brightness = get_brightness()
    print(f"Previous Brightness: {prev_brightness}")

    new_level = int(input("Enter new brightness level (0-100): "))
    set_brightness(new_level)

    current_brightness = get_brightness()
    print(f"Current Brightness: {current_brightness}")

    print("Brightness Comparison:", compare_brightness(prev_brightness, current_brightness))
