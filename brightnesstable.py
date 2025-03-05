import screen_brightness_control as sbc
from tabulate import tabulate

def set_brightness(level):
    """Set system brightness."""
    sbc.set_brightness(level)

def get_brightness():
    """Get current system brightness."""
    return sbc.get_brightness()

def compare_brightness(prev, current):
    """Compare previous and current brightness levels."""
    return "Increased" if current > prev else "Decreased" if current < prev else "Unchanged"

def main():
    history = []
    prev_brightness = get_brightness()
    print(f"Initial Brightness: {prev_brightness}")
    
    while True:
        try:
            new_level = int(input("Enter new brightness level (0-100) or -1 to exit: "))
            if new_level == -1:
                break
            set_brightness(new_level)
            current_brightness = get_brightness()
            change_status = compare_brightness(prev_brightness, current_brightness)
            
            history.append([prev_brightness, current_brightness, change_status])
            print(tabulate(history, headers=["Previous", "Current", "Change"], tablefmt="grid"))
            
            prev_brightness = current_brightness
        except ValueError:
            print("Please enter a valid integer between 0 and 100.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
