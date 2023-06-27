import cv2

def imagensIguais(pathImagem1, pathImagem2):
    imagem1 = cv2.imread(pathImagem1)
    imagem2 = cv2.imread(pathImagem2)

    if imagem1 is None or imagem2 is None:
        raise ValueError("Falha ao ler as imagens.")

    # Comparando as imagens
    resultado = cv2.compare(imagem1, imagem2, cv2.CMP_EQ)

    # Verificando o resultado
    if resultado.all():
        return True
    else:
        return False