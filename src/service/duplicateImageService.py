import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from utils.imageUtils import *

def findImages(pathOrigin, pathDestination):
    print (imagensIguais(pathOrigin, pathDestination))

# Receber apenas um caminho
## Identificar foto da raiz
