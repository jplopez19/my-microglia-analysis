import cv2
import numpy as np

# Create a blank white image
image = np.ones((100, 100), dtype=np.uint8)

# Draw a rectangle in the center
cv2.rectangle(image, (25, 25), (75, 75), 0, -1)

# Save the image
cv2.imwrite('test_image.png', image*255)
