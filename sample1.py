

#### pycaw ---ORIGINAL METHOD


from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Function to set the system volume
def set_system_volume(volume_level):
    # Get the audio interface for the default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, 
        0, 
        None
    )
    volume = interface.QueryInterface(IAudioEndpointVolume)
    
    # Get the current volume level before setting the new volume
    previous_volume = volume.GetMasterVolumeLevelScalar() * 100
    
    # Set the system volume in the range
    volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)
    print(f"Volume set to {volume_level}%")
    
    # Return the previous volume level 
    return previous_volume

# Function to get the current system volume
def get_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, 
        0, 
        None
    )
    volume = interface.QueryInterface(IAudioEndpointVolume)
    
    # Get the current volume level
    current_volume = volume.GetMasterVolumeLevelScalar() * 100
    return current_volume

# Comparison function 
def compare_volumes(previous_volume, current_volume):
    
    
    print(f"Previous Volume: {previous_volume:.2f}%")
    print(f"Current Volume: {current_volume:.2f}%")
    
    if current_volume > previous_volume:
        print(f"Volume increased by {current_volume - previous_volume:.2f}%")
    elif current_volume < previous_volume:
        print(f"Volume decreased by {previous_volume - current_volume:.2f}%")
    else:
        print("Volume remained the same.")

# Main block 
if __name__ == "__main__":
    # Get the current volume before changing it
    current_volume_before = get_system_volume()
    print(f"Current Volume: {current_volume_before}%")
    
    # Set volume to 50% and capture the previous volume level
    previous_volume = set_system_volume(30)
    
    # Get the current volume after changing it
    current_volume_after = get_system_volume()
    
    # Compare the previous and current volume
    compare_volumes(previous_volume, current_volume_after)
    
    
