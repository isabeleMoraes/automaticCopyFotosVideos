import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#from service.organizationService import processCopy
from service.organizationServiceV2 import processCopy

def main():

    print("BORA MOVER ESSAS FOTOS DE FORMA AUTOMARIZADA.")
    originRootPath = input("Para começar, informe um diretório de ORIGEM: ")
    destinationRootPath = input("Chique 10. Agora informe um diretório de DESTINO: ")

    print("-------------------- BOA! VOU COMEÇAR! --------------------\n")
   

    processCopy(originRootPath, destinationRootPath)

    

    ## Receber dois diretórios, origem e destino
    ## Ler todos os arquivos e diretórios do diretório fornecido
    ## Verificar se é um diretório ou arquivo.
        ## Se for diretório
            ## Extrair o ano presente na pasta
            ## Se tiver ano certinho
                ## Buscar lista de diretorios do diretorio destino
                ## buscar na lista de diretório dos diretório de destino o diretório referente ao ano
                ## Se não existir pasta para o ano em questão, cria-la.
                ## Verificar se a pasta que estou copiando ja existe no diretório.
                    ## Se não existir, copiar a pasta inteira com seus arquivos filhos para dentro do diretório em questão
                    ## Se ja existir, entrar no diretório
                        ## Pegar imagem por imagem do diretório de origem e verificar se ele ja existe no diretório destino de acordo com o nome da imagem.
                            ## Se existir, não faz nada loga o nome da imagem e seu diretório falando que nao copiou. ((Adicionar em uma lista)
                            ## Se não existir, copiar a foto para o diretório e logar nome e diretório falando que foi copiado com sucesso.
            ## Se não tiver ano, mover para a raiz do diretório destino.
        ## Se for imagem, mover para raiz do destino. 

        ##Se ja existir, pode copiar para um outro diretorio (IDEIA)
    
if __name__ == "__main__":
    main()




