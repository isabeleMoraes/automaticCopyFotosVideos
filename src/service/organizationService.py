import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from utils.folderUtils import *
from utils.fileUtils import *
from utils.pathUtils import *


FOLDER_TO_UNDEFINED_YEAR = "ARQUIVOS SEM ANO"


def processCopy(originRootPath, destinationRootPath):
    print( f'Metodo processCopy chamado. Parametro originRootPath= "{originRootPath}" e destinationRootPath= "{destinationRootPath}" ')
    
    listPathOfOriginRootPath = getSubPaths(originRootPath)

    print("Lista de sub diretorios", listPathOfOriginRootPath)

    for fileOrFolder in listPathOfOriginRootPath:
        print(f"\n\n----- ${fileOrFolder} ----- \n")
        subPathOfOriginRootPath = makeFullPath(originRootPath, fileOrFolder)
        if(isFolder(subPathOfOriginRootPath)):
            copyFilesOrDirectoriesToDestination(subPathOfOriginRootPath,destinationRootPath, fileOrFolder)            
        else:
            print("Arquivo sem diretorio definido")
            pathFoldertoFileWithOutYearDefined = createFolder(makeFullPath(destinationRootPath, FOLDER_TO_UNDEFINED_YEAR))
            copyFile(subPathOfOriginRootPath, makeFullPath(pathFoldertoFileWithOutYearDefined, fileOrFolder))


def copyFilesOrDirectoriesToDestination(folderToBeCopy, destinationRootPath, folderName):
    print( f'Metodo copyFilesOrDirectoriesToDestination chamado. Parametro folderToBeCopy= "{folderToBeCopy}" e destinationRootPath= "{destinationRootPath}" e folderName "{folderName}" ')

    year = getYearOfName(folderName)
    print("ano extraido: ", year)

    if not year:
        print('Pasta sem ano definido')
        pathFoldertoFileWithOutYearDefined = createFolder(makeFullPath(destinationRootPath, FOLDER_TO_UNDEFINED_YEAR))
        copyFolder(folderToBeCopy, makeFullPath(pathFoldertoFileWithOutYearDefined, folderName))
    else:
        print('Tem Ano')

        year = year[0]
        pathToYearsFolder = createFolder(makeFullPath(destinationRootPath, year))
       
        pathToYearsFolderWithFolderNameDestination = makeFullPath(pathToYearsFolder, folderName)
        print('Caminho para a pasta destino dentro da pasta com ano: ', pathToYearsFolderWithFolderNameDestination)

        if existsFolder(pathToYearsFolderWithFolderNameDestination):
            copyFileByFileToAnExistingDestinationFolder(folderToBeCopy, pathToYearsFolderWithFolderNameDestination)
        else:
            copyFolder(folderToBeCopy, pathToYearsFolderWithFolderNameDestination)

    

def copyFileByFileToAnExistingDestinationFolder(originPath, destinationPath):
    print( f'Metodo copyFileByFileToAnExistingDestinationFolder chamado. Parametro originPath= "{originPath}" e destinationPath= "{destinationPath}" ')
    
    listFilesFromOriginFolder = getSubPaths(originPath)
    
    for fileName in listFilesFromOriginFolder:
        originPathWithFileNameToBeCopied = makeFullPath(originPath,fileName)
        print("Caminho do arquivo a ser copiado: ", originPathWithFileNameToBeCopied)
        
        destinationPathWithFileNameToBeCopied =  makeFullPath(destinationPath, fileName)
        print("Caminho do destino: ", destinationPathWithFileNameToBeCopied)

        copyFile(originPathWithFileNameToBeCopied, destinationPathWithFileNameToBeCopied)