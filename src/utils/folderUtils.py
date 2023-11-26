import shutil
import os

def copyFolder(src, destination):
    if not existsFolder(destination):
        shutil.copytree(src, destination)
        print(f"PASTA COPIADA")
        return True
    else:
        print(f'A pasta JA EXISTE no destino')
        return False

def isFolder(path):
    return os.path.isdir(path)

def createFolder(folderToCreate):
    if not existsFolder(folderToCreate):
        os.mkdir(folderToCreate)
        print('Pasta criada')
    else:
        print(f'A pasta JA EXISTE')
        
    return folderToCreate

def existsFolder(folder):
    return os.path.exists(folder)