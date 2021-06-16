import cv2 as cv
import numpy as np

img = cv.imread('maze.png')
img[145:150,426:436] = 0,0,255
img[145:150,20:30] = 255,0,0
cv.imshow('maze',img)
cv.imwrite('colored maze.png',img)
cv.waitKey(0)