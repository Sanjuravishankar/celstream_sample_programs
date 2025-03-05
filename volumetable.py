from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from tabulate import tabulate

def set_system_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, 0, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    previous_volume = volume.GetMasterVolumeLevelScalar() * 100
    volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)
    return previous_volume

def get_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, 0, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    return volume.GetMasterVolumeLevelScalar() * 100

def main():
    volume_changes = []
    
    for i in range(5):
        new_volume = float(input(f"new volume?? {i+1}: "))
        previous_volume = get_system_volume()
        set_system_volume(new_volume)
        current_volume = get_system_volume()
        change = current_volume - previous_volume
        
        volume_changes.append([i+1, previous_volume, current_volume, change])
        
        print("\nVolume Change Summary:")
        print(tabulate(volume_changes, headers=["SINO", "Previous Volume (%)", "Current Volume (%)", "Change (%)"], tablefmt="grid"))

if __name__ == "__main__":
    main()
