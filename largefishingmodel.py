import pyautogui, time, keyboard, os
import numpy as np
import soundcard as sc

# Function to simulate casting a fishing line
def cast_line():
    # Sleep for a random time between 0.3 and 0.55 seconds
    time.sleep(np.random.uniform(0.4,0.8))
    # Press down the casting key
    pyautogui.keyDown(f'{castingkey}')
    # Sleep for a random time between 0.1 and 0.5 seconds
    time.sleep(np.random.uniform(0.1,0.4))
    # Release the casting key
    pyautogui.keyUp(f'{castingkey}')

# Function to find the bobber in the game
def find_bob():
    global bob_found
    # Get the current working directory
    current_dir = os.getcwd()
    # Define the directory where the bobber images are stored
    bob_directory = f"{current_dir}/img"

    while True:
        print("<< Looking for Bob. Hold esc to quit. >>")
        bob_found = False
        # Sleep for a random time between 1.3 and 1.7 seconds
        time.sleep(np.random.uniform(1.3,1.7))

        # If the escape key is pressed, exit the program
        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()

        try:
            # Loop through all the files in the bobber directory
            for file in os.listdir(bob_directory):
                # If the file is a jpg image
                if file.endswith(".jpg"):
                    file = (f"{bob_directory}/{file}")
                    # Try to find the image on the screen
                    screen_loc = pyautogui.locateOnScreen(file, confidence=0.8, grayscale=True)
                    # If the image is found
                    if screen_loc:
                        print("<< Bob identified. >>")
                        # Calculate the location to move the mouse to
                        screen_loc_offset = ((screen_loc[0] + int(screen_loc[2] / 2) + np.random.uniform(-3,3)), (screen_loc[1] + int(screen_loc[3] / 2)) + np.random.uniform(-3,3))
                        print("<< Moving to bob... >>")
                        # Move the mouse to the calculated location
                        pyautogui.moveTo(screen_loc_offset[0], screen_loc_offset[1], np.random.uniform(0.4,1.1), pyautogui.easeOutQuad)
                        bob_found = True
                        break
        except pyautogui.ImageNotFoundException:
            pass
        break

# Function to simulate reeling in the fishing line
def reel_in():
    seconds_timer = 0
    global reeled

    while True:
        reeled = False

        # If the escape key is pressed, exit the program
        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()
        # If the user selected the default speakers as the audio output device
        if input_device == '1':
            audio_source = sc.default_speaker().name
        # If the user selected VoiceMeeter as the audio output device
        if input_device == '2':
            audio_source = sc.get_speaker('VoiceMeeter Input').name
        # Get the microphone that corresponds to the selected audio output device
        mic = sc.get_microphone(id=audio_source, include_loopback=True)
        # Record audio from the microphone
        data = mic.record(samplerate=48000, numframes=48000)
        # Calculate the peak of the audio signal
        audio_peak = np.max(abs(data))
        seconds_timer += 1

        # If the audio peak is greater than 0.06
        if audio_peak > 0.06:
            print("<< You (hopefully) caught something! >>\n")
            # Simulate a right mouse button click
            pyautogui.mouseDown(button='right')
            time.sleep(np.random.uniform(0.03,0.08))
            pyautogui.mouseUp(button='right')
            time.sleep(np.random.uniform(0.35,0.5))
            reeled = True
            break

        # If the timer has exceeded 12 seconds
        if seconds_timer > 12:
            print("<< Failed. Trying again. >>")
            break

# Main function
if __name__ == "__main__":
    print("Welcome to BaitMaster 1.0. Enjoy fishing.")

    global input_device
    global castingkey
    # Ask the user to select the audio output device
    input_device = input("\nSelect your in-game Audio Output device\n[1] Default Speakers [2] VoiceMeeter [3] Exit the app >> ")
    if input_device == '3':
        exit()
    # Ask the user to input the casting key
    castingkey = input("\nInput your casting key or type exit to quit the program >> ")
    castingkey = castingkey.lower()
    if castingkey == 'exit':
        exit()
    else:
        print("\nStarting in 10 seconds. Activate the correct window.")
        time.sleep(7)
        print("\n3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1\n")
        time.sleep(1)

    while True:
        # If the escape key is pressed, exit the program
        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()

        print("\n<< Casting >>")
        # Cast the fishing line
        cast_line()
        # Try to find the bobber
        find_bob()
        # If the bobber was found
        if bob_found:
            # Reel in the fishing line
            reel_in()
            if reeled:
                continue
        else:
            time.sleep(np.random.uniform(2.3,3.7))
            print("<< Could not find Bob. Trying again. >>")
            continue
