

#### pyautogui--cross platform 


import pyautogui
import time

# Function to set system volume using keyboard shortcuts
def set_system_volume(volume_level):
    for _ in range(50):  # Reset volume to zero
        pyautogui.press("volumedown")

    time.sleep(1)  # Allow the system to process
    
    for _ in range(volume_level // 2):  # Increase volume gradually
        pyautogui.press("volumeup")

    print(f"Volume set to approximately {volume_level}%")

# Function to compare volumes (No built-in way to get current volume)
def compare_volumes(previous_volume, current_volume):
    print(f"Previous Volume: {previous_volume:.2f}%")
    print(f"Current Volume: {current_volume:.2f}%")

# Main execution block
if __name__ == "__main__":
    set_system_volume(50)
