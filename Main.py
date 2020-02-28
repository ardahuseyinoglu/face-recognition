from printScript import getOptions
from printScript import makeAChoice
from printScript import operateChoice
from printScript import welcome

samplePath = r'C:\Users\User\PycharmProjects\SAGE\computerVision\project1-FaceRecognition\samples'
haarcascadePath = r'C:\Users\User\PycharmProjects\SAGE\computerVision\project1-FaceRecognition\haarcascade_frontalface_default.xml'

welcome()
getOptions()
choice = makeAChoice()
operateChoice(choice, samplePath, haarcascadePath)
