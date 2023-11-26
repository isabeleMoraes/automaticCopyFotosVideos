import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from service.duplicateImageService import *

print('aa')
image1 = input("imagem 1: ")
image2 = input("Imagem 2: ")

findImages(image1, image2)