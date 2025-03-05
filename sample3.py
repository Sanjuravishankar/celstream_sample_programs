

### subprocess-powershell



import subprocess

# Function to set system volume using PowerShell
def set_system_volume(volume_level):
    subprocess.run(["powershell", "-c", f"(New-Object -ComObject WScript.Shell).SendKeys([char]175)"] * (volume_level // 2)) 
    print(f"Volume set to approximately {volume_level}%")

# Function to get current system volume (Requires `nircmd` tool)
def get_system_volume():
    output = subprocess.run(["nircmd.exe", "getvolume", "default"], capture_output=True, text=True)
    return float(output.stdout.strip()) if output.returncode == 0 else None

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
    current_volume_before = get_system_volume() or 50  # Default to 50% if not detected
    set_system_volume(50)
    current_volume_after = get_system_volume() or 50
    compare_volumes(current_volume_before, current_volume_after)
