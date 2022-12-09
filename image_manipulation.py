import cv2
import random

img = cv2.imread('assets/netero.jpeg', -1)

# print(img.shape)  # height, width, channels

# for i in range(100):  # manipulate image
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
#

# copy part of image and paste it on original image
part = img[500:700, 600:900]  # np slice for rows and columns
img[100:300, 650:950] = part

cv2.imshow('Isaac Netero modified', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
