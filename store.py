import sqlite3
import datetime
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from tabulate import tabulate

# Function to create or connect to database
def create_db():
    conn = sqlite3.connect("volume_changes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS volume_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            previous_volume REAL,
            current_volume REAL,
            change REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to insert a volume change record
def log_volume_change(previous_volume, current_volume, change):
    conn = sqlite3.connect("volume_changes.db")
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO volume_log (previous_volume, current_volume, change, timestamp) VALUES (?, ?, ?, ?)",
                   (previous_volume, current_volume, change, timestamp))
    conn.commit()
    conn.close()

# Function to retrieve and display previous records
def fetch_previous_logs():
    conn = sqlite3.connect("volume_changes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM volume_log ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return data

# Function to get current system volume
def get_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, 0, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    return volume.GetMasterVolumeLevelScalar() * 100

# Function to set system volume
def set_system_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, 0, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    previous_volume = volume.GetMasterVolumeLevelScalar() * 100
    volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)
    return previous_volume

# Main function
def main():
    create_db()
    volume_changes = fetch_previous_logs()
    
    print("\n--- Previous Volume Change Logs ---")
    if volume_changes:
        print(tabulate(volume_changes, headers=["ID", "Previous Volume (%)", "Current Volume (%)", "Change (%)", "Timestamp"], tablefmt="grid"))
    else:
        print("No previous records found.")
    
    for i in range(5):
        new_volume = float(input(f"New volume?? {i+1}: "))
        previous_volume = get_system_volume()
        set_system_volume(new_volume)
        current_volume = get_system_volume()
        change = current_volume - previous_volume

        log_volume_change(previous_volume, current_volume, change)

        volume_changes = fetch_previous_logs()
        print("\n--- Updated Volume Change Logs ---")
        print(tabulate(volume_changes, headers=["ID", "Previous Volume (%)", "Current Volume (%)", "Change (%)", "Timestamp"], tablefmt="grid"))

if __name__ == "__main__":
    main()




#sqlite3 volume_changes.db
#SELECT * FROM volume_log;
