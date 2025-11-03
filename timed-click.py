import pyautogui
import time
import ntplib
from datetime import datetime, timedelta

def sync_time():
    try:
        c = ntplib.NTPClient()
        response = c.request('pool.ntp.org', version=3)
        offset = response.offset  
        return offset
    except:
        print("[!] NTP sync failed, running on local clock")
        return 0

offset = sync_time()


target_time_str = "23:59:59"
today = datetime.now()
target_time = datetime.strptime(target_time_str, "%H:%M:%S").replace(
    year=today.year, month=today.month, day=today.day
)
if datetime.now() > target_time:
    target_time += timedelta(days=1)


while True:
    now = datetime.now().timestamp() + offset
    remaining = target_time.timestamp() - now

    if remaining <= 0.10:
        pyautogui.click()
        time.sleep(0.1)  
        pyautogui.click()
        print(f"[+] Clicked at {datetime.now().strftime('%H:%M:%S.%f')}")
        break
    if remaining > 1:
        time.sleep(remaining - 0.9)  
