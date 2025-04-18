import tkinter as tk

class GUI:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('BOTOES2')
        self.janela.geometry('250x250')

#CRINDO BOTÕES-----------------------------------------------------------------------------

        self.botao1 = tk.Button(self.janela, text='Botão 1', command=self.processaB1)
        self.botao2 = tk.Button(self.janela, text='Botão 2', command=self.processaB2)
        
#POSIÇÃO BOTÕES----------------------------------------------------------------------------

        self.botao1.pack()
        self.botao2.pack()

#LABEL-------------------------------------------------------------------------------------

        self.label = tk.Label(self.janela, text='Escolha...')
        self.label.pack()

#-------------------------------------------------------------------------------------------

        self.janela.mainloop()

#FUNÇÕES DE CALLBACK------------------------------------------------------------------------
#VEM DEPOIS DO MAINLOOP
    def processaB1(self):
        self.label.config(text='Botão 1 foi clicado')
    def processaB2(self):   
        self.label.config(text='Botão 2 foi clicado')

#--------------------------------------------------------------------------------------------
#MAIN:
def main():
    GUI()

main()