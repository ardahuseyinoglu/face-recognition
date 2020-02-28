import os
from Util import howManyPeople

def addNewPersonDir(path, personName):

    if not os.path.exists(path):
        os.makedirs(path)
        os.chdir(path)

    numberOfPeople = howManyPeople(path)
    addNameToTXT(path, personName)

    personPath = path + '/' + 'p' +str(numberOfPeople+1)
    if not os.path.exists(personPath):
        os.makedirs(personPath)

    return personPath

def addNameToTXT(path, personName):
    os.chdir(path)
    for file in os.listdir(path):
        if os.path.isfile(file):
            f = open(file, 'a+')
            f.write(',' + personName)
            break
