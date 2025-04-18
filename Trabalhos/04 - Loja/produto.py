import tkinter as tk
from tkinter import messagebox

#MODELO---------------------------------------------------------------------------
class Produto:
    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor(self):
        return self.__valor

#LIMITE PRODUTO------------------------------------------------------------------
class viewCadastraProd(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cadastrar")
        self.controller = controller

        self.framecod = tk.Frame(self)
        self.framedescr = tk.Frame(self)
        self.frameval = tk.Frame(self)
        self.framebutton = tk.Frame(self)
        self.framecod.pack()
        self.framedescr.pack()
        self.frameval.pack()
        self.framebutton.pack()
        
        self.labelcod = tk.Label(self.framecod, text='Código:')
        self.labelcod.pack(side='left')
        self.labeldescr = tk.Label(self.framedescr, text='Descrição:')
        self.labeldescr.pack(side='left')
        self.labelval = tk.Label(self.frameval, text='Valor:')
        self.labelval.pack(side='left')


        self.inputcod = tk.Entry(self.framecod, width=20)
        self.inputcod.pack(side='left')
        self.inputdescr = tk.Entry(self.framedescr, width=20)
        self.inputdescr.pack(side='left')
        self.inputval = tk.Entry(self.frameval, width=20)
        self.inputval.pack(side='left')

        self.salvabutton = tk.Button(self.framebutton, text='Salvar', command=self.controller.salvarProduto)
        self.salvabutton.pack(side='left')
        

#LIMITE PRODUTO------------------------------------------------------------
class ViewConsultaProd(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Consultar")
        self.controller = controller
        self.framecod2 = tk.Frame(self)
        self.framecod2.pack()
        self.labelcod2 = tk.Label(self.framecod2, text='Digite o código:')
        self.labelcod2.pack(side='left')
        self.inputcod2 = tk.Entry(self.framecod2, width=20)
        self.inputcod2.pack(side='left')
        self.framebutton2 = tk.Frame(self)
        self.framebutton2.pack()
        self.consultarbutton = tk.Button(self.framebutton2, text='Consultar', command=self.controller.buscarProduto)
        self.consultarbutton.pack(side='left')

#CONTROLADOR PRODUTO-------------------------------------------------------
class controllerProd:
    def __init__(self):
        self.listaprod = []

    def getlistaprod(self):
        return self.listaprod
    
    def cadastrarProd(self):
        self.viewProd = viewCadastraProd(self)

    def salvarProduto(self):
        codigoProd = self.viewProd.inputcod.get()
        descrProd = self.viewProd.inputdescr.get()
        valProd = self.viewProd.inputval.get()
        if not codigoProd or not descrProd or not valProd:
            messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
            return
        for c in self.listaprod:
            if codigoProd == c.codigo:
                messagebox.showerror('Erro', 'Código já existente na lista.')
                return
        produto = Produto(codigoProd, descrProd, valProd)
        self.listaprod.append(produto)
        messagebox.showinfo('Sucesso', 'Produto cadastrado com sucesso.')
        self.viewProd.destroy()

    def getProduto(self, cod):
        prodrest = None
        for c in self.listaprod:
            if cod ==  c.codigo:
                prodrest = c
                return prodrest
        return False

    def consultarProd(self):
        self.viewProd2 = ViewConsultaProd(self)

    def buscarProduto(self):
        cod = self.viewProd2.inputcod2.get()
        produto = self.getProduto(cod)
        if not produto:
            messagebox.showerror('ERRO:', 'Produto não encontrado')
        else:
            mensagem = f"Código: {produto.codigo}\nDescrição: {produto.descricao}\nValor: {produto.valor}"
            messagebox.showinfo('Produto Encontrado', mensagem)
        self.viewProd2.destroy()
