#Camily Victal Finamor - 2024001197

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email
    
    @property
    def codigo(self):
        return self.__codigo

########################################################################################################

class View():
    def __init__(self, master, controller):
        self.controller = controller 
        self.janela = tk.Frame(master) 
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Codigo: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")  
        self.labelInfo3.pack(side="left")  

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")                    
      
        self.buttonSubmit = tk.Button(self.janela,text="Salva")  
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Limpa")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)    

        self.buttonList = tk.Button(self.janela,text="Listar") 
        self.buttonList.pack(side="left")
        self.buttonList.bind("<Button>", controller.listaHandler)  

        self.buttonConsulta = tk.Button(self.janela,text="Consultar") 
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controller.consultaHandler)  


    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
      
##########################################################################################################
class Controller():       
    def __init__(self):
        self.root = tk.Tk() 
        self.root.geometry('300x100') 
        self.listaClientes = [] 
        self.clientesCadastrados = set() 

        
        self.view = View(self.root, self)
        self.root.title("Cadastro Clientes")
       
        self.root.mainloop()

    def salvaHandler(self, event):
        nomeCli = self.view.inputText1.get() 
        emailCli = self.view.inputText2.get()
        codigoCli = self.view.inputText3.get()
        if codigoCli in self.clientesCadastrados:
                self.view.mostraJanela('Erro Código Cliente', 'Erro: insira um codigo que não esteja sendo utilizado')
                self.clearCodigoHandler(event)
                return
        else:
            cliente = ModelCliente(nomeCli, emailCli, codigoCli) 
            self.clientesCadastrados.add(codigoCli)
            self.listaClientes.append(cliente)
            self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get())) 
    
    def clearCodigoHandler(self, event):
        self.view.inputText3.delete(0, len(self.view.inputText3.get())) 
    
    def listaHandler(self, event):
        strClientes = ''
        for clientes in self.listaClientes:
            strClientes += clientes.nome + ' - ' + clientes.email + ' - ' + clientes.codigo + '\n'
        self.view.mostraJanela('Clientes', strClientes)
    
    def consultaHandler(self, event):
        consultaCodigo = simpledialog.askstring("Consultar Cliente", "Digite o código que deseja buscar: ")
        if consultaCodigo:
            for clienteConsultado in self.listaClientes:
                if clienteConsultado.codigo == consultaCodigo:
                    self.view.mostraJanela('Cliente Encontrado', "Nome: {}\nEmail: {}".format(clienteConsultado.nome, clienteConsultado.email))
                    return
            self.view.mostraJanela('Cliente Não Encontrado', "Digite um código que esteja cadastrado")

#######################################################################################################################################################

if __name__ == '__main__':
    c = Controller()