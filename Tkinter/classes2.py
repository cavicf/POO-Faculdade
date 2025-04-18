import tkinter as tk

class GUI:
    def __init__(self):

#JANELA---------------------------------------------------------------------------------------

        self.janela = tk.Tk()
        self.janela.title('FRAMES2')
        self.janela.geometry('400x400')

#FRAMES---------------------------------------------------------------------------------------

        self.frameTopo = tk.Frame(self.janela) #aqui cria-se 2 frames, um pra base e outro pro topo
        self.frameBase = tk.Frame(self.janela)

#LABELSTOPO-----------------------------------------------------------------------------------
        
        self.label1 = tk.Label(self.frameTopo, text='Um')
        self.label2 = tk.Label(self.frameTopo, text='Dois')
        self.label3 = tk.Label(self.frameTopo, text='Tres')

#POSIÇÃOTOPO----------------------------------------------------------------------------------
#Aqui estamos posicionando as labels criadas no frame e comoo estamos usando o pack side top, esses labels serõ empilhados no topo do frame
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

#LABELSBASE-----------------------------------------------------------------------------------
        
        self.label4 = tk.Label(self.frameBase, text='Um')
        self.label5 = tk.Label(self.frameBase, text='Dois')
        self.label6 = tk.Label(self.frameBase, text='Tres')

#POSIÇÃOBASE----------------------------------------------------------------------------------
#Aqui estamos posicionando as labels criadas no frame da base e como estamos usando o pack side left, esses labels serão alocadas horizontalmente no frame
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

#POSIÇÃOFRAMES--------------------------------------------------------------------------------
#Depois de criar as labels e posicioná-las dentro dos frames, podemos aagora posicionar os frames dentro da janela. Como estamos utilizando o pack e nenhum argumento, esses frmes serão empilhados no meio da janela
        self.frameTopo.pack()
        self.frameBase.pack()

##############################################################################################

        self.janela.mainloop() #entra no loop da bertura da janela

##############################################################################################
#MAIN

def main():
    GUI()

main()