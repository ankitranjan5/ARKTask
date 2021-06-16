import cv2 as cv
import numpy as np

final = np.zeros((200,150,3),dtype='uint8')
final[150,75] = 255,255,255
cv.imshow('final', final)
cv.waitKey(0)