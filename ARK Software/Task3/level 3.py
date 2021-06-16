import cv2 as cv
import numpy as np

img = cv.imread('Task round\maze_lv3.png')
green = np.zeros_like(img,dtype='uint8')
blue = np.zeros_like(img,dtype='uint8')
red = np.zeros_like(img,dtype='uint8')

for i  in range(180):
    for j in range(457):
        b , g , r = img[i,j] 
        if b == 230:
            blue[i,j] = 230,230,230
        elif g == 230:
            green[i,j] = 230,230,230
        else :
            red[i,j] = 230,230,230
cv.imshow('maze B found', blue)
cv.imshow('maze G found', green)
cv.imshow('maze R found', red)
cv.imwrite('maze.png',red)
cv.waitKey(0)