import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def equalization(img):
    hist = cv2.calcHist(img,[1],None,[255],[0,255])
    cummu = np.cumsum(hist)
    row = np.size(img,0)
    col = np.size(img,1)
    equ_img= np.zeros((row,col),np.uint8)
    for i in range(0,255):
        H_eq= round(((cummu[i])/(cummu[254]))*255)
        equ_img[img==i]=[H_eq]               
    return equ_img

file = 'jpg'
name = 'image2'
pil_img = Image.open(name+'.'+file).convert('RGB') 
cv_img = np.array(pil_img)
img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
o_hist = cv2.calcHist(gray_img,[1],None,[255],[0,255])
cummu_o_hist = np.cumsum(o_hist)
gray_equ = equalization(gray_img)
equ_hist = cv2.calcHist([gray_equ],[0],None,[255],[0,255])
cummu_equ_hist = np.cumsum(equ_hist)

plt.subplot(2,2,1), plt.imshow(gray_img,cmap='gray')
plt.subplot(2,2,2), plt.imshow(gray_equ,cmap='gray')
plt.subplot(2,2,3), plt.plot(cummu_o_hist)
plt.subplot(2,2,4), plt.plot(cummu_equ_hist,color='r')
plt.show()
