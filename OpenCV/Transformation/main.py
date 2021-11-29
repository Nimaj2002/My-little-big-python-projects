import numpy as np
import cv2 as cv

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("img", img)


def translate(image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)


# -x --> left
# -y --> Up
# +x --> Right
# +y --> Down

# translated = translate(img, -100, -100)
# cv.imshow("translated", translated)


# Rotation
def rotate(image, angle, rotPoint=None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(image, rotMat, dimensions)


# rotated = rotate(img, 45)
# cv.imshow("Rotated", rotated)

# Resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)

# Flip
# flipped = cv.flip(img, -1)
# # 0 for x axis , 1 for y axis , -1 for both
# cv.imshow("flipped", flipped)


cv.waitKey(0)

