import os

def makeFullPath(path, name):
    return os.path.join(path,name)

def getSubPaths(path):
    return os.listdir(path)