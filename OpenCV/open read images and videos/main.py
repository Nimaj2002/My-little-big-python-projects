
import cv2 as cv

# Reading images
# img = cv.imread("Photos/cat_large.jpg")
# cv.imshow("Cat", img)
# cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture("../Resources/Videos/dog.mp4")
# 0 , 1, 2 for camera file path for videos
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyWindow()

