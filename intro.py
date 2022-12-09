import cv2

img = cv2.imread('assets/netero.jpeg', 0)  # 0 for grayscale, -1 original, 1 transparency

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # resize, fx, fy = fraction for resize

img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('assets/new_netero.jpg', img)  # write new image

cv2.imshow('Isaac Netero', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
