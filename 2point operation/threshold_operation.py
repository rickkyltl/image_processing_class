import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def threshold_operation(img):
    width, height = img.shape
    i=0
    ath=150
    new_img= np.zeros((width,height),np.uint8)   
    for y in range (0,height):
        for x in range (0,width):
            a = img[x,y]
            if a <= ath:
                f_a = 50
            else:
                f_a = 200
            new_img[x,y]=f_a 
        i = i+1            
    return new_img

file = 'jpg'
name = 'image'
pil_img = Image.open(name+'.'+file).convert('RGB') 
cv_img = np.array(pil_img)
img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
original_hist = cv2.calcHist(gray_img,[1],None,[255],[0,255])
new_img = threshold_operation(gray_img)
new_hist = cv2.calcHist(new_img,[0],None,[255],[0,255])


plt.subplot(2,2,1), plt.imshow(gray_img,cmap='gray')
plt.subplot(2,2,2), plt.imshow(new_img,cmap='gray')
plt.subplot(2,2,3), plt.plot(original_hist)
plt.subplot(2,2,4), plt.plot(new_hist)
plt.show()
