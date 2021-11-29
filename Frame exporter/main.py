import cv2

# Opens the Video file
cap = cv2.VideoCapture("traffic2.mp4")
i = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imwrite('kang'+str(i)+'.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()


