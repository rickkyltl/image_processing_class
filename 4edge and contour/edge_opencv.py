import cv2
from matplotlib import pyplot as plt

img_name = "image2.jpg"
img =  cv2.imread(img_name)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplac = cv2.Laplacian(gray_img,cv2.CV_64F)
sobel_x = cv2.Sobel(gray_img,cv2.CV_64F,1,0,ksize=5)
sobel_y = cv2.Sobel(gray_img,cv2.CV_64F,0,1,ksize=5)
canny = cv2.Canny(gray_img,10,50)

cv2.imshow("input",gray_img)
cv2.imshow("laplacian",laplac)
cv2.imshow("sobel_x",sobel_x)
cv2.imshow("sobel_y",sobel_y)
cv2.imshow("canny",canny)

while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
