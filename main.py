import cv2
import cv2.misc
import numpy


def r_cam():
    vid = cv2.VideoCapture(0)
    vid.open(0,0)  
     
    while(True):
        x, frame = vid.read()   
        vid.grab()
        if not (x):
            print("stream error")
            cv2.destroyAllWindows()
            vid.release()
            break
        c = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        cv2.imshow('cam', c)
        #camera does not display without a waitkey esc
        if(cv2.waitKey(1) == ord('q')):
            break   
    vid.release()

r_cam()