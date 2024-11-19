import cv2
import cv2.data
import cv2.mat_wrapper
import cv2.misc
import numpy


def r_cam():
    vid = cv2.VideoCapture(0)
    vid.open(0,0)  
    dec = cv2.FaceDetectorYN.create("face_detection_yunet_2023mar.onnx","face_detection_yunet_2023mar_int8.onnx",input_size=[640,480])
    
    while(True):
        x, frame = vid.read()   
        vid.grab()
        if not (x):
            print("stream error")
            cv2.destroyAllWindows()
            vid.release()
            break
        
        c, face =  dec.detect(frame)
        M = face[0,:]
        M = M[0]
        print(M)
        if  M == None:   
            print(face)
            cv2.imshow('cam', frame)
            
        else:
            d = face[0,:]
            d_double = d.astype(int)

            eyeLeft =  cv2.drawMarker(frame,[int(d[4]),int(d[5])],[0,0,255])     
            eyeRight =  cv2.drawMarker(frame,[int(d[6]),int(d[7])],[0,0,255])   
            mNose =  cv2.drawMarker(frame,[int(d[8]),int(d[9])],[0,0,255])
            mouthR = cv2.drawMarker(frame,[int(d[10]),int(d[11])],[0,0,255])
            mouthL =  cv2.drawMarker(frame,[int(d[12]),int(d[13])],[0,0,255]) 
            faceRect = cv2.rectangle(frame,[d_double[0],d_double[1]],[(d_double[0] + d_double[2]),(d_double[1]+d_double[3])],[0,0,255])
            cv2.imshow('cam', frame)
        #camera does not display without a waitkey esc
        if(cv2.waitKey(1) == ord('q')):
            break   
    vid.release()

r_cam()