

###ctypes--WINDOWS API


import ctypes
import time

# Load the Windows multimedia library
winmm = ctypes.WinDLL("winmm.dll")

# Function to set the system volume (0 to 100)
def set_system_volume(volume_level):
    volume = int(volume_level * 65535 / 100)  # Convert to Windows volume scale (0-65535)
    winmm.waveOutSetVolume(0, volume | (volume << 16))  # Set volume for left & right channels
    print(f"Volume set to {volume_level}%")

# Function to get the current system volume
def get_system_volume():
    volume = ctypes.c_uint()
    winmm.waveOutGetVolume(0, ctypes.byref(volume))  # Retrieve volume value
    current_volume = (volume.value & 0xFFFF) * 100 / 65535  # Convert back to percentage
    return current_volume

# Function to compare volumes
def compare_volumes(previous_volume, current_volume):
    print(f"Previous Volume: {previous_volume:.2f}%")
    print(f"Current Volume: {current_volume:.2f}%")
    
    if current_volume > previous_volume:
        print(f"Volume increased by {current_volume - previous_volume:.2f}%")
    elif current_volume < previous_volume:
        print(f"Volume decreased by {previous_volume - current_volume:.2f}%")
    else:
        print("Volume remained the same.")

# Main execution block
if __name__ == "__main__":
    current_volume_before = get_system_volume()
    previous_volume = current_volume_before  # Store initial volume
    set_system_volume(50)
    
    time.sleep(1)  # Delay to allow the volume to update
    
    current_volume_after = get_system_volume()
    compare_volumes(previous_volume, current_volume_after)
