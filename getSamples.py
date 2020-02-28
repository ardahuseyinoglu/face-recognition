import cv2
import os

def captureFaces(path, haarcascadePath):

    os.chdir(path)
    face_detector = cv2.CascadeClassifier(haarcascadePath)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 640) # set video widht
    cap.set(4, 480) # set video height

    minW = 0.1*cap.get(3)
    minH = 0.1*cap.get(4)

    counter = 0
    numberOfImage = 1

    while True:
        ret, frame = cap.read()
        cv2.imshow('img', frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5, minSize = (int(minW), int(minH)))

        if not len(faces) == 0:
            (x,y,w,h) = faces[0]

        if counter % 30 == 0 and len(faces) != 0 :
            fileName = str(numberOfImage) + '.jpg'
            cv2.imwrite(fileName, gray[y:y+h,x:x+w])
            numberOfImage += 1

        if numberOfImage == 16:
            break

        counter += 1

    cap.release()
    cv2.destroyAllWindows()
