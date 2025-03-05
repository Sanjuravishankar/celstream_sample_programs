

###   sounddevice--cross platform



import sounddevice as sd

# Function to get the current system volume (returns sample rate, not actual volume)
def get_system_volume():
    print("Fetching current system volume...")
    devices = sd.query_devices(kind='output')  # Get default output device
    volume = devices['default_samplerate']  # This is the system sample rate
    print(f"Current system volume (sample rate): {volume} Hz")
    return volume

# Function to compare previous and current volume levels
def compare_volumes(previous_volume, current_volume):
    print(f"Previous Volume: {previous_volume} Hz")
    print(f"Current Volume: {current_volume} Hz")
    
    if current_volume > previous_volume:
        print(f"Volume increased by {current_volume - previous_volume} Hz")
    elif current_volume < previous_volume:
        print(f"Volume decreased by {previous_volume - current_volume} Hz")
    else:
        print("Volume remained the same.")

# Main execution block
if __name__ == "__main__":
    print("Starting volume check...")
    previous_volume = get_system_volume()
    current_volume = get_system_volume()  # No actual volume change in `sounddevice`
    compare_volumes(previous_volume, current_volume)
    print("Volume check completed!")
