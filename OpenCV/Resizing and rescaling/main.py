import cv2 as cv


# for video Rescaling
def rescaleFrame(input_frame, scale=0.75):
    # For Images, Videos, Live Videos
    width = int(input_frame.shape[1] * scale)
    height = int(input_frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(input_frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live Videos
    capture.set(3, width)
    capture.set(4, height)


# for image rescaling
# img = cv.imread("../Resources/Photos/cat.jpg")
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)
# cv.waitKey(0)


capture = cv.VideoCapture("../Resources/Videos/dog.mp4")
# 0 , 1, 2 for camera file path for videos
while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame, scale=0.5)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", resized_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyWindow()
