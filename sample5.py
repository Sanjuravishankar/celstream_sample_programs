
#  win32api-- another API method


import win32api
import win32con

# Function to increase system volume
def volume_up(steps=5):
    print(f"Increasing volume by {steps} steps...")
    for _ in range(steps):
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0)
    print("Volume increased successfully!")

# Function to decrease system volume
def volume_down(steps=5):
    print(f"Decreasing volume by {steps} steps...")
    for _ in range(steps):
        win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0)
    print("Volume decreased successfully!")

# Function to compare actions (simulating volume change comparison)
def compare_volumes(action):
    print(f"Checking volume change after {action}...")
    print("Volume change action executed, but exact volume level cannot be retrieved.")

# Main execution block
if __name__ == "__main__":
    print("Starting volume adjustment...")
    volume_up()
    compare_volumes("increasing volume")
    volume_down()
    compare_volumes("decreasing volume")
    print("Volume adjustment completed!")


