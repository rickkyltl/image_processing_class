import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def threshold_operation(img):
    width, height = img.shape
    hist = cv2.calcHist(gray_img,[1],None,[255],[0,255])
    i=0
    new_img= np.zeros((width,height),np.uint8)  
    index = 0
    count = 0
    for intensity in hist:      #find minimum and maximum intensity value from calcHist
        if intensity > 0 and count == 0:
            a_low = index
            count = 1
        if intensity == 0 and count == 1 and old != 0:
            a_high = index
        old = intensity
        index = index + 1
    print(a_high,a_low)
    for y in range (0,height):
        for x in range (0,width):
            a = img[x,y]
            f_a = round((a-a_low)*255/(a_high-a_low))
            if f_a <= 0:
                f_a = 0
            if f_a >= 255:
                f_a = 255
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
