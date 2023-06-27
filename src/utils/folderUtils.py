import shutil
import os

def copyFolder(src, destination):
    if not existsFolder(destination):
        shutil.copytree(src, destination)
        print("Pasta copiada")
        return True
    else:
        print(f'A pasta "{src}" ja existe no destino')
        return False

def isFolder(path):
    return os.path.isdir(path)

def createFolder(folderToCreate):
    if not existsFolder(folderToCreate):
        os.mkdir(folderToCreate)
    else:
        print('A pasta ja existe')
        
    return folderToCreate

def existsFolder(folder):
    return os.path.exists(folder)