import sys
sys.path.append('/path/to/opencv/installation')
import cv2
import numpy as np

def playerFound(given):
    # Load the pre-trained human detection model (HOG-based)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Load the screenshot image
    #image_path = 'screenshot.png'  # Replace with the path to your screenshot image
    #image = cv2.imread(image_path)
    image=cv2.cvtColor(np.array(given), cv2.COLOR_RGB2BGR)

    # Resize the image (optional, depending on the image size)
    # image = cv2.resize(image, (new_width, new_height))

    # Detect humans in the image
    boxes, _ = hog.detectMultiScale(image)

    if len(boxes) > 0:
        # Check if any human is in the center of the screen
        image_height, image_width, _ = image.shape
        center_x = image_width // 2
        center_y = image_height // 2

        for (x, y, w, h) in boxes:
            if x <= center_x <= x + w and y <= center_y <= y + h:
                # Print the position of the human in the center
                print("Human found at center of the screen: (x={}, y={})".format(center_x, center_y))
                return True

    return False