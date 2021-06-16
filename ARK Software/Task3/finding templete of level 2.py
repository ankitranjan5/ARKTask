import cv2 as cv
import numpy as np

img = cv.imread('Task round\zucky_elon.png')
template = cv.imread('level 1 chupi image.png')
h = np.shape(template)[0]
w = np.shape(template)[1]
img2 = img.copy()
result = cv.matchTemplate(img2, template,cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
location=max_loc
bottom_right = (location[0] + w, location[1] + h)
print(location)  
cv.rectangle(img, location, bottom_right, 255, 5)
cv.imshow('COLOR',img)
cv.waitKey(0)