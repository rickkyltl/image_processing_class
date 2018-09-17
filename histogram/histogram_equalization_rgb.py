import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

file = 'jpg'
name = 'image'
pil_img = Image.open(name+'.'+file).convert('RGB') 
cv_img = np.array(pil_img)
img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
split_img = cv2.split(img)
b_hist = cv2.calcHist(split_img,[0],None,[255],[0,255])
g_hist = cv2.calcHist(split_img,[1],None,[255],[0,255])
r_hist = cv2.calcHist(split_img,[2],None,[255],[0,255])
cummu_b_hist = np.cumsum(b_hist)
cummu_g_hist = np.cumsum(g_hist)
cummu_r_hist = np.cumsum(r_hist)
raw_equ_img = [None,None,None]
for i in range(0,3):
    raw_equ_img[i] = cv2.equalizeHist(split_img[i])
b_hist_eq = cv2.calcHist(raw_equ_img,[0],None,[255],[0,255])
g_hist_eq = cv2.calcHist(raw_equ_img,[1],None,[255],[0,255])
r_hist_eq = cv2.calcHist(raw_equ_img,[2],None,[255],[0,255])
cummu_b_hist_eq = np.cumsum(b_hist_eq)
cummu_g_hist_eq = np.cumsum(g_hist_eq)
cummu_r_hist_eq = np.cumsum(r_hist_eq)
equ_img = cv2.merge((raw_equ_img[0],raw_equ_img[1],raw_equ_img[2]))

plt.subplot(2,2,1), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.subplot(2,2,2), plt.imshow(cv2.cvtColor(equ_img,cv2.COLOR_BGR2RGB))
plt.subplot(2,2,3), plt.plot(cummu_b_hist,color='b'), plt.plot(cummu_g_hist,color='g'), plt.plot(cummu_r_hist,color='r')
plt.subplot(2,2,4), plt.plot(cummu_b_hist_eq,color='b'), plt.plot(cummu_g_hist_eq,color='g'), plt.plot(cummu_r_hist_eq,color='r')
plt.show()
