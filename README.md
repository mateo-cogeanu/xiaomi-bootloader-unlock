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
install homebrew [brew.sh](https://brew.sh/) and the instructions are very straight-foward
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

install `pyautogui` and `ntplib`

```bash
pip3 install pyautogui ntplib
```

run `scrcpy`

on the phone navigate to xiaomi community 
## WIP


# CREDITS:

## [scrcpy](https:/github.com/Genymobile/scrcpy/)

## [Python script](https://www.reddit.com/r/Android/comments/1mgn0yj/xiaomis_bootloader_unlock_system_is_broken_heres/)

I Do **NOT** own any of the files included in this repository and do **NOT** take credit
