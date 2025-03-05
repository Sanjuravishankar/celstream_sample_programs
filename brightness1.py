
## screen_brightness_control


import screen_brightness_control as sbc

def set_brightness(level):
    """Set system brightness."""
    sbc.set_brightness(level)

def get_brightness():
    """Get current system brightness."""
    return sbc.get_brightness()

def compare_brightness(prev, current):
    """Compare previous and current brightness levels."""
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
