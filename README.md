# Bait Master 1.0

## Fishing Bot for World of Warcraft Classic utilizing a simple and efficient Python script.

## Overview
A simple Python script to automate fishing in WoW Classic. The script employs image recognition algorithms to accurately identify the position of your fishing bobber within the World of Warcraft Classic environment. Upon detection of a sound exceeding a predefined decibel threshold - indicative of a fish bite - the system initiates the reeling process, thereby automating the fishing activity within the game.

## Disclaimer
Utilization of this software is entirely at the discretion of the user. It is crucial to note that any form of automation, inclusive of all botting variants, contravenes the Terms of Service and may precipitate punitive measures such as account suspension or termination. This bot was conceived and developed as a educational endeavor, serving primarily as a learning resource. Consequently, it is unlikely to receive subsequent updates or enhancements post its initial release.

## Installation
1. Install [Python](https://www.python.org)
2. Check your installation:
    - `python --version` or `python3 --version`
3. Install packages and dependencies for python:
    - `pip install pyautogui` or `pip3 install pyautogui`
    - `pip install opencv-python` or `pip3 install opencv-python`
    - `pip install keyboard` or `pip3 install keyboard`
    - `pip install soundcard` or `pip3 install soundcard`

## Game Configuration
1. Enable the auto loot option in the game settings.
2. Disable all sound options from the game audio settings.
3. Download the "Better Fishing" addon and enable "Enhance sounds" for 100%.
4. Bind your "Fishing" spell to a keyboard button.
5. If you want to be able to fish up BoP items, download the "Leatrix Plus" addon and enable the "Disable Loot Warnings" option from the menu.
6. Find a location with no other fishers as other bobbers might confuse the bot.

## Script Usage
1. Open the Terminal App.
2. Navigate to the folder where the script is with the command `cd /path/to/your/folder`.
3. Start the script with `python baitmaster.py`.
4. Use your default audio output device. You cannot listen to other audio while botting.

## Troubleshooting

### If you get an error message about the Pillow package when you run the script:
- `pip install --upgrade Pillow` or `pip3 install --upgrade Pillow`
- If this doesn't solve the problem, check the Pillow documentation for supported Python versions.

### If the bob can't be reliably detected:
- Add your own images of bobs at the specific location you're fishing.
- Take screenshots and crop them so that only the bob is displayed.
- Save them as .jpg and put them in the "img" folder.
- Check the original files for reference.
