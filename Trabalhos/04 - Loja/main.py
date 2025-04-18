#Camily Victal Finamor - 2024001197
import tkinter as tk
import produto as prod
import cupom as cup

#LIMITE PRINCIPAL-----------------------------------------------------------------------------------------
class viewPrincipal:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.menuProd = tk.Menu(self.menubar)
        self.menuCupom = tk.Menu(self.menubar)

        self.menuProd.add_command(label = 'Cadastrar', command=self.controller.cadastrarProd)
        self.menuProd.add_command(label = 'Consultar', command=self.controller.consultarProd)
        self.menubar.add_cascade(label='Produto', menu=self.menuProd)

        self.menuCupom.add_command(label = 'Criar', command=self.controller.criarCupom)
        self.menuCupom.add_command(label = 'Consultar', command=self.controller.consultarCupom)
        self.menubar.add_cascade(label='Cupom Fiscal', menu=self.menuCupom)

        self.root.config(menu=self.menubar)

#CONTROLADOR PRINCIPAL------------------------------------------------------------------------------------
class controllerPrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.controllerProd = prod.controllerProd()
        self.controllerCup = cup.controllerCup(self.controllerProd)

        self.view = viewPrincipal(self.root, self)
        self.root.title('Loja Conveniência')

        self.root.mainloop()

    def cadastrarProd(self):
        self.controllerProd.cadastrarProd()

    def consultarProd(self):
        self.controllerProd.consultarProd()

    def criarCupom(self):
        self.controllerCup.criarCupom()

    def consultarCupom(self):
        self.controllerCup.consultarCupom()

#---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    c = controllerPrincipal()