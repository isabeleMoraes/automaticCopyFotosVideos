import os
import datetime
import re
import shutil

def dadosFoto():
    diretorio =  r'C:/Users/Meums/Pictures/python'

    # Obter a lista de arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Verificar a data de criação de cada arquivo
    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        informacoes_arquivo = os.stat(caminho_completo)
        data_criacao = datetime.datetime.fromtimestamp(informacoes_arquivo.st_ctime)
        print(f'O arquivo {arquivo} foi adicionado em: {data_criacao}')

def getYearOfName(name):
    pattern = r"[@#$%_\- ]"
    nameSplited = re.split(pattern, name)
    return list(filter(lambda x: '20' in x, nameSplited))

def copyFile(src, destination):
    if not os.path.exists(destination):
        shutil.copy2(src, destination)
        print("ARQUIVO COPIADO")
        return True
    else:
        print(f'[JA EXISTE] O arquivo "{src}" no destino')
        return False