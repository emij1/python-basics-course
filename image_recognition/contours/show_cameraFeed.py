from cv2 import cv2

videoCapture = cv2.VideoCapture(0)

if not videoCapture.isOpened():
    print("Camera not found.")
    exit()
while True:
    cameraType, cameraFeed = videoCapture.read()
    grayscaleFeed = cv2.cvtColor(cameraFeed, cv2.COLOR.BGR2GRAY)
    cv2.imshow("Video live feed", cameraFeed)
    if cv2.waitKey(1) == ord("q"):
        break
    
videoCapture.release()
cv2.destroyAllWindows()

