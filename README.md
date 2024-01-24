# BaitMaster 1.0

## Simple and efficient fishing bot for World of Wacraft Classic 1.15.0

## Overview
A simple Python script to automate fishing in WoW Classic. The script employs image recognition algorithms to accurately identify the position of your fishing bobber within the World of Warcraft Classic environment. Upon detection of a sound exceeding a predefined decibel threshold - indicative of a fish bite - the system initiates the reeling process, thereby automating the fishing activity within the game.

## Disclaimer
Utilization of this software is entirely at the discretion of the user. It is crucial to note that any form of automation, inclusive of all botting variants, contravenes the Terms of Service and may precipitate punitive measures such as account suspension or termination. This bot was conceived and developed as a educational endeavor, serving primarily as a learning resource. Consequently, it is unlikely to receive subsequent updates or enhancements post its initial release.

## Installation & Configuration
1. Install [Python](https://www.python.org)
2. Check your installation:
    - `python --version` or `python3 --version`
3. Install packages and dependencies for python:
    - `pip install pyautogui` or `pip3 install pyautogui`
    - `pip install opencv-python` or `pip3 install opencv-python`
    - `pip install keyboard` or `pip3 install keyboard`
    - `pip install soundcard` or `pip3 install soundcard` 
3. Enable the auto loot option in the game settings.
4. Disable all sound options from the game audio settings.
5. Download the "Better Fishing" addon and enable "Enhance sounds" for 100%.
6. Bind your "Fishing" spell to a keyboard button.
7. If you want to be able to fish up BoP items, download the "Leatrix Plus" addon and enable the "disable loot warnings" option from the menu.

## Usage
- Find a location with no other fishers as other bobbers will confuse the bot.
- Navigate to the folder where the script is with `cd /path/to/your/folder`.
- Start the script with `python baitmaster.py` and enjoy.
- Use your default audio output device. You cannot listen to other audio while botting. No further changes needed.
- If you are having issues with bobber detection due to resolution or other differences, 

## Troubleshooting
1. Error message complaining about Pillow when running the script?
- `pip install --upgrade Pillow`
- If this doesn't fix the issue, see Pillow documentation for supported Python versions.

2. Poor bobber detection?
- Use your own bobber images for detection. Replace the existing images with a few of your own bobber screenshots (must be .jpg). See the original files for reference.