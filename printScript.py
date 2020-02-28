import time
from Util import includeTheName
from addNewUser import addNewPersonDir
from recognizeFaces import recogFaces
from getSamples import captureFaces
from gettingData import getNameArray


def welcome():
    print('------------------------------------')
    print('Welcome to the Face Recognition Application')
    print('------------------------------------')
    time.sleep(1)


def getOptions():
    time.sleep(0.5)
    print('(1)Go to the application that recognizes faces belonging to registered users')
    print('(2)Register a new user')
    print('(3)List the all registered user(s)')
    print('(4)Terminate the program')
    print('------------------------------------')


def makeAChoice():
    while True:
        choice = input('Please make a choice (1, 2, 3 or 4): ')
        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            return choice
        else:
            print('\nERROR: Enter 1, 2, 3 or 4')


def operateChoice(choice, samplePath, haarcascadePath):
    if choice == '1':
        choice1(samplePath, haarcascadePath)
    elif choice == '2':
        choice2(samplePath, haarcascadePath)
    elif choice == '3':
        choice3(samplePath, haarcascadePath)
    elif choice == '4':
        choice4()


def rechoose(samplePath, haarcascadePath):
    getOptions()
    choice = makeAChoice()
    operateChoice(choice, samplePath, haarcascadePath)


def choice1(samplePath, haarcascadePath):
    print('Selected 1')
    print('------------------------------------')
    time.sleep(0.6)
    print('Everything is done.')
    time.sleep(0.5)
    print('Please wait, application is started...')
    print('**PRESS Esc TO TERMINATE THE PROGRAM**')
    time.sleep(0.75)

    #Recognize registered faces, label them and give confident prob., if the face looking at the camera is not registered, then label them as unknown
    recogFaces(samplePath, haarcascadePath)

    rechoose(samplePath, haarcascadePath)


def choice2(samplePath, haarcascadePath):
    print('Selected 2')
    print('------------------------------------')

    while True:
        time.sleep(0.3)
        while True:
            personName = input('Please enter your name: ')
            if includeTheName(personName, samplePath):
                print('ERROR: The name entered already exists. Please try another\n')
            else:
                time.sleep(0.3)
                print('Welcome ' + personName)
                break

        print('------------------------------------')
        time.sleep(0.5)
        print('Directory is created...')
        time.sleep(0.5)
        print('Name of user is registered to the file \'namesOfPeople\'...')

        #Directory for new user is created(p*) and name of the user is added to the txt file that store all name registered
        path = addNewPersonDir(samplePath, personName)

        time.sleep(0.5)
        print('Registration is completed')
        print('------------------------------------')
        time.sleep(0.5)
        print('Now we need your photos. The more different face expression and angels the more successful results')
        time.sleep(2)
        print('Ready? Please look at the camera')
        print('Light of the camera is closed when capturing is done')
        time.sleep(2)

        #Needed sample photos including faces of the new user is captured from camera
        captureFaces(path, haarcascadePath)
        print('Your faces are added to dataset successfully')

        time.sleep(0.3)
        print('------------------------------------')

        rechoose(samplePath, haarcascadePath)

        print('------------------------------------')


def choice3(samplePath, haarcascadePath):
    print('Selected 3')
    print('------------------------------------')
    time.sleep(0.3)

    names = getNameArray(samplePath)

    if len(names) == 0:
        print('There is no registered user')
    else:
        names.sort()
        print('The list of registered user:')
        time.sleep(0.6)
        for name in names:
            if name == 'None':
                continue
            else:
                print(name)

    print('------------------------------------')

    rechoose(samplePath, haarcascadePath)


def choice4():
    print('------------------------------------')
    print('\nProgram is terminated')
    exit()
