import cv2 as cv
import numpy as np

img = cv.imread('treasure_mp3.png')

fill = open("myFile_final.txt","w")

#i = 6
#for j in 


for i in range(390):
    for j in range(390):
        b , g , r = img[i,j]
        if b == g == r :
             fill.writelines(str(b)+'\n')
     
fill.close()
cv.imshow('ori',img)
cv.waitKey(0)