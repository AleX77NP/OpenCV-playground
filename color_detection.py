import numpy as np
import cv2

import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # use camera

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([230, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)  # bitwise AND to keep pixels

    cv2.imshow('Frame', result)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()  # release camera
cv2.destroyAllWindows()