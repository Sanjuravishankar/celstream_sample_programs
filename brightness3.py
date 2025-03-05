import ddcci

def get_brightness():
    """Get brightness from external monitor."""
    with ddcci.get_monitor(0) as monitor:
        return monitor.get_brightness()

def set_brightness(level):
    """Set brightness on external monitor."""
    with ddcci.get_monitor(0) as monitor:
        monitor.set_brightness(level)

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
