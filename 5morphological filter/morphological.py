import cv2
from matplotlib import pyplot as plt
import numpy as np

img_name = "image2.jpg"
img =  cv2.imread(img_name)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
morpho = np.ones((3,3),np.uint8)
erosion = cv2.erode(gray_img,morpho)
dilation = cv2.dilate(gray_img,morpho)
opening = cv2.morphologyEx(gray_img, cv2.MORPH_OPEN, morpho)
closing = cv2.morphologyEx(gray_img, cv2.MORPH_CLOSE, morpho)

cv2.imshow("input",gray_img)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)

while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
