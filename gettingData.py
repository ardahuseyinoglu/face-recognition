import os
from PIL import Image
import cv2
import numpy as np

def getFacesAndLabels(samplePath, haarcasacdePath):

    face_detector = cv2.CascadeClassifier(haarcasacdePath)
    faces = []
    labels = []

    path = samplePath
    os.chdir(path)

    for dir in os.listdir(path):
        if os.path.isdir(dir):
            label = int(dir.replace("p", ""))
            imagesOfSamplePath = path + '/' + dir

            for image_path in os.listdir(imagesOfSamplePath):
                imagePath = imagesOfSamplePath + '/' + image_path
                PIL_img = Image.open(imagePath).convert('L') # grayscale
                img_numpy = np.array(PIL_img,'uint8')
                faces_in_frame = face_detector.detectMultiScale(img_numpy)

                for (x,y,w,h) in faces_in_frame:
                    faces.append(img_numpy[y:y+h,x:x+w])
                    labels.append(label)
    return faces, labels


def getNameArray(samplePath):
    nameArr = []
    path = samplePath
    if not os.path.exists(path):
        return nameArr
    else:
        os.chdir(path)
        for dirs in os.listdir(path):
            if os.path.isfile(dirs):
                f = open(dirs, 'r')
                names = f.read()
                nameArr = names.split(',')

    return nameArr
