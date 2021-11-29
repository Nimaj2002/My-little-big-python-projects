import cv2 as cv

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("cat", img)


# # convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Blur
# blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# Edge Cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow("canny", canny)

# Dilating the image
# dilated = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow("dilated", dilated)

# Eroding
# eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow("eroded", eroded)

# Resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
# cv.imshow("resized", resized)

# Cropping
# cropped = img[50:200, 200:400]
# cv.imshow("cropped", cropped)

cv.waitKey(0)
