# #reading video
import cv2 as cv #import openCV library
capture =cv.VideoCapture("C:\\Users\\naima\\Desktop\\new folder\\pythonProject\\kitten.mp4") #file name  there is "\\" need because it is the convension

while True:  #loop for continuous show frame by frame
    isTrue, frame = capture.read() #loop will continue if frame get value
    cv.imshow("Video Frame", frame)  #will show frame in a window name ""Video Frame"

    if cv.waitKey(20) & 0xFF==ord('d'): # will exit after 20 frame or press "d"
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0) #continue infinite time

