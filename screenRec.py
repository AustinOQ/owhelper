
import time
import pyautogui
import sys
sys.path.append('/path/to/opencv/installation')
import cv2
import numpy as np
def playerFound(given):
    # Load the pre-trained human detection model (HOG-based)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image=cv2.cvtColor(np.array(given), cv2.COLOR_RGB2BGR)
    # Detect humans in the image
    boxes, _ = hog.detectMultiScale(image)
    if len(boxes) > 0:
        # Check if any human is in the center of the screen
        image_height, image_width, _ = image.shape
        center_x = image_width // 2
        center_y = image_height // 2
        for (x, y, w, h) in boxes:
            if (x+w*.1) <= center_x <= x + w and y <= center_y <= y + (h*.9):
                return True
    return False
# Function to capture and save a screenshot
def capture_screenshot():
    while True:
        # Capture the screenshot
        screenshot = pyautogui.screenshot()
        if(playerFound(screenshot)):
            pyautogui.click(button='left')
        time.sleep(.001)
          
       
capture_screenshot()