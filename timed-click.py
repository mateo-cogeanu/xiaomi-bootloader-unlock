import pyautogui       # For automating mouse movements and clicks
import time            # For delays and time tracking
import ntplib          # For syncing with an accurate internet time server (NTP)
from datetime import datetime, timedelta  # For handling and calculating times

# --- Function: Synchronize local time with an NTP server ---
def sync_time():
    try:
        c = ntplib.NTPClient()                         # Create an NTP client instance
        response = c.request('pool.ntp.org', version=3)  # Query an NTP server for the current time
        offset = response.offset                       # Calculate the offset between local and NTP time
        return offset                                  # Return time correction offset
    except:
        print("[!] NTP sync failed, running on local clock")  # Fallback if NTP sync fails
        return 0                                       # No offset applied (local time only)

# Get time offset (in seconds) from the NTP server
offset = sync_time()

# --- Set the target time for the click ---
target_time_str = "20:23:59"  # The exact time (HH:MM:SS) when the click should happen

# Get current date/time
today = datetime.now()

# Combine today’s date with the target time
target_time = datetime.strptime(target_time_str, "%H:%M:%S").replace(
    year=today.year, month=today.month, day=today.day
)

# If the target time already passed today, schedule it for tomorrow
if datetime.now() > target_time:
    target_time += timedelta(days=1)

# --- Main loop: wait until the target time is reached ---
while True:
    now = datetime.now().timestamp() + offset           # Get current time corrected with NTP offset
    remaining = target_time.timestamp() - now           # Calculate remaining seconds until target

    # When less than or equal to 0.1 seconds remain, perform the click
    if remaining <= 0.10:
        pyautogui.click()                              # First click
        time.sleep(0.1)                                # Short delay between clicks
        pyautogui.click()                              # Second click
        print(f"[+] Clicked at {datetime.now().strftime('%H:%M:%S.%f')}")  # Log exact click time
        break                                           # Exit loop after clicking

    # Sleep efficiently to reduce CPU usage
    if remaining > 1:
        time.sleep(remaining - 0.9)  # Sleep until just before 1 second remains

