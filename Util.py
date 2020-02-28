import os

def includeTheName(personName, samplePath):

    path = samplePath
    if not os.path.exists(path):
        return False
    else:
        os.chdir(path)
        for dirs in os.listdir(path):
            if os.path.isfile(dirs):
                f = open(dirs, 'r')
                names = f.read()
                names = names.split(',')
                for name in names:
                    if(personName == name):
                        return True
    return False


def howManyPeople(path):

    numberOfDirs = 0
    os.chdir(path)
    for dir in os.listdir(path):
        if os.path.isdir(dir):
            numberOfDirs += 1

    if numberOfDirs == 0:
        f = open('namesOfPeople.txt', 'a+')
        f.write('None')
        f.close()

    return numberOfDirs
