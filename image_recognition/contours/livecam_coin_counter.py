from cv2 import cv2
import numpy as np

def orderPoints(points):
    n_points = np.concatenate([points[0], points[1], points[2], points[3]]).tolist()
    y_order = sorted(n_points, key = lambda n_points: n_points[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key = lambda x1_order: x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key = lambda x2_order: x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def alignment(image, height, width):
    aligned_image = None
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_type, threshold_image = cv2.threshold(grayscale_image, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("Threshold", threshold_image)
    contours = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = sorted(contours, key = cv2.contourArea, reverse=True)
    for c in contours:
        epsilon = 0.01*cv2.arcLength(c, True)
        approximation = cv2.approxPolyDP(c, epsilon, True)
        if len(approximation) == 4:
            points = orderPoints(approximation)
            points1 = np.float32(points)
            points2 = np.float32([[0,0], [width,0], [0,height], [width, height]])
            M = cv2.getPerspectiveTransform(points1, points2)
            aligned_image = cv2.warpPerspective(image, M, (width, height))
    return aligned_image

videoCapture = cv2.VideoCapture(0)

while True:
    camera_type, cameraFeed = videoCapture.read()
    if camera_type == False:
        break
    image_A6 = alignment(cameraFeed, width = 480, height = 677)
    if image_A6 is not None: 
        points = []
        grayscale_image = cv2.cvtColor(image_A6, cv2.COLOR_BGR2GRAY)
        gaussBlur_image = cv2.GaussianBlur(grayscale_image, (5,5), 1)
        __, threshold_image2 = cv2.threshold(gaussBlur_image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
        cv2.imshow("Threshold", threshold_image2)
        contour2 = cv2.findContours(threshold_image2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(image_A6, contour2, -1, (0, 0, 255), 2)
        sum1 = 0.0
        sum2 = 0.0
        for c_2 in contour2:
            area = cv2.contourArea(c_2)
            moments = cv2.moments(c_2)
            if(moments["m00"] == 0):
                moments["m00"] = 1.0
            x = int(moments["m10"]/moments["m00"])
            y = int(moments["m01"]/moments["m00"])
            
            if area < 9300 and area > 8000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image_A6, "S/. 0.20", (x, y), font, 0.75, (0, 255, 0), 2)
                sum1 += 0.2

            if area < 7800 and area > 6500:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image_A6, "S/. 0.10", (x, y), font, 0.75, (0, 255, 0), 2)
                sum2 += 0.1
        total = sum1 + sum2
        print("Total sum in cents:", round(total,2))
        cv2.imshow("Imagen A6", image_A6)
        cv2.imshow("Camera Feed", cameraFeed)
    if cv2.waitKey(1) == ord("s"):
        break
videoCapture.release()     
cv2.destroyAllWindows()
