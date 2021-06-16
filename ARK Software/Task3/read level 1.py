import cv2 as cv
import numpy as np

img = cv.imread('Task round\Level1.png')
final = np.zeros((200,150,3),dtype='uint8')

l = 0
m = 0

for i in range(6,177):
    for j in range(177):
        if (i == 6 and j >= 94) or (6 < i < 176) or (i == 176 and j < 4):
             final[l,m] = img[i,j]
             if l < 199 and m == 149:
                 l = l + 1
                 m = 0
             else:
                 m = m + 1


cv.imshow('ori',img)
cv.imshow('tre',final)
cv.imwrite('readed.png',final)
cv.waitKey(0)