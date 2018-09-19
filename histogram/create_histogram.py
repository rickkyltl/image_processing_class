import cv2
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

def gray_histogram(img):
    width, height = img.shape
    H = [0]*256
    for y in range (0,height):
        for x in range (0,width):
            intensity = img[x,y]
            i = intensity
            H[i] = H[i] +1
    return H

file = ['jpg','gif','png','bmp','tif']
name = 'image'
i=3
for img_type in file:
    pil_img = Image.open(name+'.'+img_type).convert('RGB') 
    cv_img = np.array(pil_img)
    img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    split_img = cv2.split(img)
    #o_hist = cv2.calcHist(gray_img,[1],None,[255],[0,255])
    o_hist2 = gray_histogram(gray_img)
    b_hist = cv2.calcHist(split_img,[0],None,[255],[0,255])
    g_hist = cv2.calcHist(split_img,[1],None,[255],[0,255])
    r_hist = cv2.calcHist(split_img,[2],None,[255],[0,255])
    plt.subplot(6,2,i)
    plt.plot(o_hist2)
    plt.text(10,50,'gray'+img_type)
    i = i+1
    plt.subplot(6,2,i)
    plt.plot(b_hist,color='b')
    plt.plot(g_hist,color='g')
    plt.plot(r_hist,color='r')
    plt.text(10,20000,'RGB'+img_type)
    i = i+1
 
plt.subplot(6,2,1), plt.imshow(gray_img,cmap='gray')
plt.subplot(6,2,2), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

