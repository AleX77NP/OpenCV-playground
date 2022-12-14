import numpy as np
import cv2

base = cv2.imread('assets/soccer.jpg', 0)
template = cv2.imread('assets/ball.PNG', 0)

height, width = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    image = base.copy()

    result = cv2.matchTemplate(image, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(min_loc, max_loc)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + width, location[1] + height)
    cv2.rectangle(image, location, bottom_right, 255, 5)

    cv2.imshow('Detect', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
