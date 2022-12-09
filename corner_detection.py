import numpy as np
import cv2

image = cv2.imread('assets/board.jpg')
image = cv2.resize(image, (0, 0), fx=0.75, fy=0.75)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_image, 100, 0.01, 10)
# print(corners)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()  # flatten array
    cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda elem: int(elem), np.random.randint(0, 255, size=3)))
        cv2.line(image, corner1, corner2, color, 1)

cv2.imshow('Chess Board', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
