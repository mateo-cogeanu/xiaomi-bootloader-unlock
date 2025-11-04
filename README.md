# How to unlock the Xiaomi bootloader

## Phone side setup

1. Turn on your Xiaomi phone and open settings -> Xiaomi Account -> Add your credentials and sign in
2. Go Back -> open settings -> About Phone -> tap OS Version untill you see "you are now a developer"
3. Go back -> additional settings -> Developer options -> turn on OEM unlocking, turn on USB debbuging and USB debugging (Security settings)

## Computer side setup

### Windows setup
Go to [python.org](https://python.org/)
press downloads and then download Python.
and then Download Windows installer (64-bit) or Download Windows installer (32-bit) **depending on your system**
double-click the `.exe` file and proceed with the installation but make sure you **press add to path**

### MacOS setup
Install homebrew [brew.sh](https://brew.sh/) and the instructions are very straight-foward
then install python3 with

```bash
brew install python3
```

### Linux setup

**Debian/Ubuntu**
Python3 might be pre-installed on your system, but if not here is the command

```bash
sudo apt install python3
```

## Main Setup

Install requirements

```bash
pip3 install pyautogui ntplib
```

Download `scrcpy` for your OS from this repository or from the original [source](https:/Genymobile/scrcpy/releases)

Plug your phone into your PC; and if you are on macOS press `Allow`

On the phone press `allow`

Open `scrcpy` on your PC and if you see your phones screen `scrcpy` is ready!

Download the Python script named `timed-click.py`

In your text edidor/code editor open `timed-click.py` and at line `21` change the time to your local time when it is 23:59 and 59 seconds in china you can use [timeanddate.com](https://www.timeanddate.com/worldclock/converter.html?iso=20251104T155900&p1=33) and just add your country and change the code

### WIP



# CREDITS:

### [scrcpy](https:/github.com/Genymobile/scrcpy/)
Copyright (C) 2018 Genymobile

Copyright (C) 2018-2025 Romain Vimont

Licensed under the [Apache License, Version 2.0](ttps://www.apache.org/licenses/LICENSE-2.0)

### [Original Python script](https://www.reddit.com/r/Android/comments/1mgn0yj/xiaomis_bootloader_unlock_system_is_broken_heres/) from `EstimateMuted4573` on Reddit

I do **NOT** own any of the files included in this repository and do **NOT** take credit for the original work.

All rights remain with the original authors.
