# #reading image
import cv2 as cv #import openCV library
img=cv.imread("C:\\Users\\naima\\Desktop\\new folder\\pythonProject\\cat2.jpg") #file name  there is "\\" need because it is the convension
cv.imshow("Moon",img) #window_name, image_variable
cv.waitKey(0)  # show infint amount of time
