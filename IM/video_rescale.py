import cv2 as cv
def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture =cv.VideoCapture("C:\\Users\\naima\\Desktop\\new folder\\pythonProject\\kitten.mp4") #file name  there is "\\" need because it is the convension

while True:  #loop for continuous show frame by frame
    isTrue, frame = capture.read() #loop will continue if frame get value

    frame_resize = rescaleFrame(frame)

 #   cv.imshow("VideoFrame", frame)  #will show frame in a window name ""Video Frame"
    cv.imshow("VideoResized", frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'): # will exit after 20 frame or press "d"
        break
capture.release()
cv.destroyAllWindows()



