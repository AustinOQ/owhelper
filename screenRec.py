
import pyautogui
import sys
from PIL import ImageGrab
sys.path.append('/path/to/opencv/installation')
import cv2
import numpy as np
def playerFound(given):
    # Load the pre-trained human detection model (HOG-based)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    #image=cv2.cvtColor(np.array(given), cv2.COLOR_RGB2BGR)
    image=given
    # Detect humans in the image
    boxes, _ = hog.detectMultiScale(image)
    if len(boxes) > 0:
        # Check if any human is in the center of the screen
        image_height, image_width, _ = image.shape
        center_x = image_width // 2
        center_y = image_height // 2
        for (x, y, w, h) in boxes:
            if (x+w*.1) <= center_x <= x+(w*.9)  and (y+h*.01) <= center_y <= y+h:
                return True
    return False
# Function to capture and save a screenshot
def capture_screenshot():
    REGION = (600, 360, 1285, 720)
    while True:
        # Capture the screenshot
        #screenshot = pyautogui.screenshot()
       
        if(playerFound(np.array(ImageGrab.grab(bbox=REGION)))):
            pyautogui.click(button='left')
            pyautogui.click(button='left')
           
        #else:
            #pyautogui.mouseUp(button='left')
            
          
       
capture_screenshot()
