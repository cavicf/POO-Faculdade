#Aluna: Camily Victal Finamor
#Matricula: 2024001197

import tkinter as tk
import jogos as jogo

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CLASSE VIEW MAIN
class ViewPrincipal:
    def __init__(self, janela, controlador):
        self.janela = janela
        self.controlador = controlador
        self.janela.geometry('300x250')

        self.menu = tk.Menu(self.janela)
        self.menu1 = tk.Menu(self.menu)

        self.menu1.add_command(label='Cadastrar', command=self.controlador.CadastrarJogo)
        self.menu1.add_command(label='Avaliar', command=self.controlador.AvaliarJogo)
        self.menu1.add_command(label='Consultar', command=self.controlador.ConsultarJogo)
        self.menu.add_cascade(label='Jogo', menu=self.menu1)

        self.janela.config(menu=self.menu)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CLASSE CONTROLADORA MAIN
class ControladorPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Jogos')

        self.ControladorJogo = jogo.ControladorJogo(self)

        self.ViewPrincipal = ViewPrincipal(self.root, self)
        self.root.mainloop()

    def CadastrarJogo(self):
        return self.ControladorJogo.CadastrarJogo() 
    def AvaliarJogo(self):
        return self.ControladorJogo.AvaliarJogo()

    def ConsultarJogo(self):
        return self.ControladorJogo.ConsultarJogo()
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MAIN
if __name__ == '__main__':
    c = ControladorPrincipal()