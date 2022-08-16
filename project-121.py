import cv2 
import numpy as np
import time

fourcc = cv2.VideoWriter_fourcc(*"XVID")
outputFile = cv2.VideoWriter("vid.avi", fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)
time.sleep(2)
bg = 0

# img2 = cv2.imread("C:\hm\bg\5437549.jpg")

for i in range(0,60):
    ret, bg = cap.read()
bg = np.flip(bg, axis = 1)

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret: 
        break
    img = np.flip(img, axis = 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerBlack = np.array([30, 30, 0])
    upperBlack = np.array([104, 153, 70])
    mask1 = cv2.inRange(hsv, lowerBlack, upperBlack)
    # lowerBlack2 = np.array([30, 30, 0])
    # upperBlack2 = np.array([104, 153, 70])
    # mask2 = cv2.inRange(hsv, lowerBlack2, upperBlack2)
    # mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    # mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    # mask2 = cv2.bitwise_not(mask1)

    result1 = cv2.bitwise_and(img, img, mask = mask1)
    # result2 = cv2.bitwise_and(bg, img, mask = mask1)
    finaloutput = cv2.addWeighted(result1, 1, result1, 1 , 0)
    outputFile.write(finaloutput)
    cv2.imshow("output", finaloutput)
    cv2.waitKey(1)

cap.release() 
outputFile.release()
cv2.destroyAllWindows()





