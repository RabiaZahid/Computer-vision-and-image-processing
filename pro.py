import cv2
import numpy as np
pic=cv2.imread('apple.jpg',0)
height,width=pic.shape

sobel_x = cv2.Sobel(pic,cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(pic,cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('original pic',pic)
cv2.waitKey(0)

cv2.imshow('Sobel X pic',sobel_x)
cv2.waitKey(0)

cv2.imshow('Sobel Y pic',sobel_y)
cv2.waitKey(0)

sobel_Or = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('sobel or pic',sobel_Or)
cv2.waitKey(0)

canny = cv2.Canny(pic,20,170)
cv2.imshow('canny edge',canny)
cv2.waitKey(0)

kernel_3x3=np.ones((3,3),np.float32)/9
blurred=cv2.filter2D(canny,-1,kernel_3x3)
cv2.imshow('3x3_blurring', blurred)
cv2.waitKey(0)



kernel_9x9=np.ones((9,9),np.float32)/81
blurred=cv2.filter2D(canny,-1,kernel_9x9)
cv2.imshow('9x9_blurring', blurred)
cv2.waitKey(0)

kernel_25x25=np.ones((25,25),np.float32)/625
blurred=cv2.filter2D(canny,-1,kernel_25x25)
cv2.imshow('25x25_blurring', blurred)
cv2.waitKey(0)
