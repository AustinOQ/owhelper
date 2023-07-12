import sys
sys.path.append('/path/to/opencv/installation')
import cv2
#def PlayerFound(screenshot):
def playerFound():
    


    # Load the pre-trained human detection model (HOG-based)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Load the screenshot image
    image_path = 'screenshot.png'  # Replace with the path to your screenshot image
    image = cv2.imread(image_path)

    # Resize the image (optional, depending on the image size)
    # image = cv2.resize(image, (new_width, new_height))

    # Detect humans in the image
    boxes, _ = hog.detectMultiScale(image)

    if len(boxes) > 0:
        # Get the first detected human's rectangle
        (x, y, w, h) = boxes[0]
    
        # Get the vertices of the rectangle
        top_left = (x, y)
        bottom_right = (x + w, y + h)
    
        # Return the vertices of the rectangle
        print("Human detected. Rectangle vertices:", top_left, bottom_right)
    else:
        # No humans detected
        print("No humans detected.")
        # Return 0 to indicate no rectangle found
        vertices = 0

playerFound()