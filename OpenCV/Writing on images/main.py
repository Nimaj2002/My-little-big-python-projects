import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Blank", blank)

# img = cv.imread("../Resources/Photos/cat.jpg")
# cv.imshow("Cat", img)

# Paint the image to certain color
# blank[0:300, 200:400] = 25, 85, 255
# cv.imshow("Green", blank)

# Draw a Rectangular
# cv.rectangle(blank, (0, 0), (300, 200), (0, 0, 255), thickness=20)
# # thickness = -1 or cv.field fills all the shape
# cv.imshow("Green", blank)

# Draw circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 255, 0), thickness=-1)
# cv.imshow("Green", blank)

# Draw Line
# cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=4)
# cv.imshow("Line", blank)

# Write Text on image
cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)
cv.waitKey(0)
