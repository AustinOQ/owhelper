
import time
import pyautogui
from playerfound import *

# Function to capture and save a screenshot
def capture_screenshot():
  

    while True:
        # Capture the screenshot
        screenshot = pyautogui.screenshot()

        # Save the screenshot to the working directory
       

        print(f'Screenshot captured and saved as screenshot.png')

        

        if(playerFound(screenshot)):
            
            screenshot.save(f'screenshot.png')
       
        

        # Wait for 1 second before capturing the next screenshot
        time.sleep(5)

# Call the function to start capturing screenshots
capture_screenshot()

