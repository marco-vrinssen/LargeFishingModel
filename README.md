# BaitMaster 1.0 - A Fishing Bot for WoW Classic

## Functionality
A simple Python script to automate fishing in WoW Classic. The script employs image recognition algorithms to accurately identify the position of your fishing bobber within the World of Warcraft Classic environment. Upon detection of a sound exceeding a predefined decibel threshold - indicative of a fish bite - the system initiates the reeling process, thereby automating the fishing activity within the game.

## Disclaimer
Utilization of this software is entirely at the discretion of the user. It is crucial to note that any form of automation, inclusive of all botting variants, contravenes the Terms of Service and may precipitate punitive measures such as account suspension or termination. This bot was conceived and developed as a pedagogical endeavor, serving primarily as a learning resource. Consequently, it is unlikely to receive subsequent updates or enhancements post its initial release.

## Installation & Configuration
1. Run the following commands to install dependencies:
    - `pip install pyautogui`
    - `pip install opencv-python`
    - `pip install keyboard`
    - `pip install soundcard`
2. Enable the auto looting option in game settings.
3. Disable all sound options from the game audio options.
4. Download the "Better Fishing" addon and enable "Enhance sounds" option from the addon and set it to 100%.
5. Bind your "Fishing" spell to a keyboard button.
6. If you want to be able to fish up BoP items, download the "Leatrix Plus" addon and enable the "disable loot warnings" option from the menu.

## Usage
- Find a location with no other fishers as other bobbers will confuse the bot. 
- Start the script with `python baitmaster.py` and enjoy.
- Use your default audio output device. You cannot listen to other audio while botting. No further changes needed.
- If you are having issues with bobber detection due to resolution or other differences, 

## Troubleshooting
1. Error message complaining about Pillow when running the script?
- `pip install --upgrade Pillow`
- If this doesn't fix the issue, see Pillow documentation for supported Python versions.

2. Poor bobber detection?
- Use your own bobber images for detection. Replace the existing images with a few of your own bobber screenshots (must be .jpg). See the original files for reference.