#Camily Victal Finamor - 2024001197
import tkinter as tk
import profissional as prof
import aluno as aluno
#VIEW-------------------------------------------------------------------
class ViewPrincipal:
    def __init__(self, janela, controlador):
        self.janela = janela
        self.controlador = controlador
        self.janela.geometry('300x250')

        self.menu = tk.Menu(self.janela)
        self.menuProfissional = tk.Menu(self.menu)
        self.menuAluno = tk.Menu(self.menu)

        self.menuProfissional.add_command(label='Cadastrar', command=self.controlador.cadastrarProfissional)
        self.menuProfissional.add_command(label='Listar', command=self.controlador.listarProfissional)
        self.menuProfissional.add_command(label='Faturamento', command=self.controlador.faturamentoProfissional)
        self.menu.add_cascade(label='Profissional', menu=self.menuProfissional)

        self.menuAluno.add_command(label='Cadastrar', command=self.controlador.cadastrarAluno)
        self.menuAluno.add_command(label='Consultar', command=self.controlador.consultarAluno)
        self.menu.add_cascade(label='Aluno', menu=self.menuAluno)

        self.janela.config(menu=self.menu)


#CONTROLADOR PRINCIAPL--------------------------------------------------
class ControladorPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Gerenciar Estúdio')

        self.ControladorProfissional = prof.ControladorProfissional(self)
        self.ControladorAluno = aluno.ControladorAluno(self)

        self.ViewPrincipal = ViewPrincipal(self.root, self)
        self.root.mainloop()

    def cadastrarProfissional(self):
        return self.ControladorProfissional.cadastrarProfissional()
    
    def listarProfissional(self):
        return self.ControladorProfissional.listarProfissional()
    
    def faturamentoProfissional(self):
        return self.ControladorProfissional.faturamentoProfissional()

    def cadastrarAluno(self):
        return self.ControladorAluno.cadastrarAluno()
    
    def consultarAluno(self):
        return self.ControladorAluno.consultarAluno()

#MAIN-------------------------------------------------------------------
if __name__ == '__main__':
    c = ControladorPrincipal()
