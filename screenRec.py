import time
import pyautogui
from playerfound import *

def main():
    while True:
        # Capture the screen and store it in a variable
        screenshot = pyautogui.screenshot()

        #left click if in hitbox
        if playerFound(screenshot):
            pyautogui.click(button='left')
            # Add a delay to avoid continuous clicks
            time.sleep(0.5)


        # Wait for 5 second before updating the screenshot
        #this will help not eat too much 
        time.sleep(5)
