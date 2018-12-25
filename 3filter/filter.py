import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import math

def box_filter(img):
    width, height = img.shape
    fil = [[1/9,1/9,1/9],
            [1/9,1/9,1/9],
            [1/9,1/9,1/9],
    ]
    new_img = img
    for y in range (1,height-1):
        for x in range (1,width-1):
            summation = 0
            for j in range (-1,2):
                for u in range (-1,2):
                    summation = summation + (img[x+u,y+j]*fil[u+1][j+1])
            new_img[x,y] = round(summation)
    return new_img

def gaussian_filter(img):
    width, height = img.shape
    sigma = 2
    cofactor=0
    fil = np.zeros((5, 5))
    for u in range (-2,3):
        for j in range (-2,3):
            fil[u+2][j+2] = math.pow(2.718,-1*((math.pow(u,2))+(math.pow(j,2))/(2*sigma*sigma)))
            cofactor=cofactor + fil[u+2][j+2]
    new_img = img
    for y in range (2,height-2):
        for x in range (2,width-2):
            summation = 0
            for j in range (-2,3):
                for u in range (-2,3):
                    summation = summation + (img[x+u,y+j]*(fil[u+2][j+2]))
            new_img[x,y] = round(summation/cofactor)
    return new_img

file = 'jpg'
name = 'image'
pil_img = Image.open(name+'.'+file).convert('RGB') 
cv_img = np.array(pil_img)
img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
box_img = box_filter(gray_img)
guassian_img = gaussian_filter(gray_img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median_filter =  cv2.medianBlur(gray_img,3)




plt.subplot(1,4,1), plt.imshow(gray_img,cmap='gray')
plt.subplot(1,4,2), plt.imshow(box_img,cmap='gray')
plt.subplot(1,4,3), plt.imshow(guassian_img,cmap='gray')
plt.subplot(1,4,4), plt.imshow(median_filter,cmap='gray')
plt.show()
