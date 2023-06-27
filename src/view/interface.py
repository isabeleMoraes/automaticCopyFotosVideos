import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from service.backupService import processCopy
from tkinter import *
from tkinter import filedialog 

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "16")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 50
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 50
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 40
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 40
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Backup de fotos")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()

        self.origemLabel = Label(self.segundoContainer,text="Origem", font=self.fontePadrao)
        self.origemLabel.pack(side=LEFT)

        self.origem = Entry(self.segundoContainer)
        self.origem["width"] = 30
        self.origem["font"] = self.fontePadrao
        self.origem.pack(side=LEFT)

        self.botaoExplorarOrigem = Button(self.segundoContainer)
        self.botaoExplorarOrigem["text"] = "buscar"
        self.botaoExplorarOrigem["font"] = ("Calibri", "10")
        self.botaoExplorarOrigem["width"] = 12
        self.botaoExplorarOrigem["command"] = self.browseFiles
        self.botaoExplorarOrigem.pack(side=LEFT)

        self.destinoLabel = Label(self.terceiroContainer, text="Destino", font=self.fontePadrao)
        self.destinoLabel.pack(side=LEFT)

        self.destino = Entry(self.terceiroContainer)
        self.destino["width"] = 30
        self.destino["font"] = self.fontePadrao
        self.destino.pack(side=LEFT)

        self.botaoExplorarDestino = Button(self.terceiroContainer)
        self.botaoExplorarDestino["text"] = "buscar"
        self.botaoExplorarDestino["font"] = ("Calibri", "10")
        self.botaoExplorarDestino["width"] = 12
        self.botaoExplorarDestino["command"] = self.browseFiles
        self.botaoExplorarDestino.pack(side=LEFT)

        self.botaoCopiar = Button(self.quartoContainer)
        self.botaoCopiar["text"] = "Copiar Fotos"
        self.botaoCopiar["font"] = ("Calibri", "16")
        self.botaoCopiar["width"] = 12
        self.botaoCopiar["command"] = self.iniciaProcesso 
        self.botaoCopiar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        #Método verificar senha
    def iniciaProcesso(self):
        origem = self.origem.get()
        destino = self.destino.get()

        if not origem or not destino:
            self.mensagem["text"] = "Informe os caminhos corretamente"
        else:
            processCopy(origem, destino)
            self.mensagem["text"] = "Feito!"

    def browseFiles(self): 
        self.origem = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))
       
                                                                                                
window = Tk() 
   
window.title('File Explorer') 
   
window.geometry("500x500") 
   
window.config(background = "white") 


root = Tk()
root.title("Backup de fotos - Created By Isabele Moraes")
Application(root)
root.mainloop()