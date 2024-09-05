#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
#here kernel size is (3,3) ,kernel means a window/matrix where all values are taken except the center 
#one and calculate the average of put int hte center and then slide it for later image 
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur(more effective for blurring )
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur(more effective than gaussian blur and used to remove noise)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral(Most Effective)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)
#try to keep lower value for medianblur and bilateral
cv.waitKey(0)
