import psutil
import os
import time

# Get battery info
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

# Display battery status
status = "Charging" if plugged else "Not Charging"
print(f"Battery Status: {status}, {percent}%")

# Ask user for action
choice = input("Enter 0 to do nothing, 1 to sleep for 3 seconds: ")

if choice == "1":
    print("Sleeping for 3 seconds...")
    time.sleep(3)
    print("Resumed execution.")
elif choice == "0":
    print("No action taken.")
else:
    print("Invalid input.")

