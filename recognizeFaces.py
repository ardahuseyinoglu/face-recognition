import cv2
from gettingData import getFacesAndLabels
from gettingData import getNameArray
import numpy as np
import os

def recogFaces(samplePath, haarcasacdePath):

    names = []
    path = samplePath

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    if os.path.exists(path):
        faces, labels = getFacesAndLabels(samplePath, haarcasacdePath)
        names = getNameArray(samplePath)
        face_recognizer.train(faces, np.array(labels))
    faceCascade = cv2.CascadeClassifier(haarcasacdePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    recognizedFaces = []
    print('------------------------------------')

    while True:
        ret, img =cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces_in_frame = faceCascade.detectMultiScale(gray, 1.2, 5, minSize = (int(minW), int(minH)))
        for(x,y,w,h) in faces_in_frame:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            if os.path.exists(path):
                id, confidence = face_recognizer.predict(gray[y:y+h,x:x+w])

                if (confidence < 100):
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x,y+h-5),font,1,(255,255,0),1)

                if not (id in recognizedFaces or id == 'unknown'):
                    recognizedFaces.append(id)
                    print(id + ' is recognized')


            else:
                cv2.putText(img,'unknown',(x+5,y-5),font,1,(255,255,255),2)

        cv2.imshow('camera',img)
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

    print('------------------------------------')
