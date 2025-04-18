import tkinter as tk
from tkinter import messagebox

#MODELO---------------------------------------------------------------
class Cupom:
    def __init__(self, nroCupom):
        self.__nroCupom = nroCupom
        self.__itensCupom = []

    @property
    def nroCupom(self):
        return self.__nroCupom
    
    @property
    def itensCupom(self):
        return self.__itensCupom
    
    def adicionar_item(self, produto):
        self.__itensCupom.append(produto)
    
    def calcular_total(self):
        total = sum([float(produto.valor) for produto in self.__itensCupom])
        return total
    
    def exibir_dados(self):
        dados = f"Cupom Número: {self.__nroCupom}\n"
        dados += "Produtos:\n"
        for produto in self.__itensCupom:
            dados += f"- {produto.descricao} | R${produto.valor}\n"
        dados += f"Total: R${self.calcular_total()}\n"
        return dados

#LIMITE CUPOM--------------------------------------------------------
class viewCriaCup(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cadastrar Cupom Fiscal")
        self.controller = controller

        self.framecod = tk.Frame(self)
        self.frameprodutos = tk.Frame(self)
        self.framebutton = tk.Frame(self)
        self.framecod.pack()
        self.frameprodutos.pack()
        self.framebutton.pack()

        self.labelcod = tk.Label(self.framecod, text='Número do Cupom:')
        self.labelcod.pack(side='left')
        
        self.inputcod = tk.Entry(self.framecod, width=20)
        self.inputcod.pack(side='left')

        self.labelprod = tk.Label(self.frameprodutos, text='Escolha um Produto:')
        self.labelprod.pack(side='left')
        
        self.listboxprodutos = tk.Listbox(self.frameprodutos)
        for produto in self.controller.getListaProdutos():
            self.listboxprodutos.insert(tk.END, produto.descricao)
        self.listboxprodutos.pack()

        self.salvabutton = tk.Button(self.framebutton, text='Adicionar Produto', command=self.controller.adicionar_item)
        self.salvabutton.pack(side='left')

        self.finalizarbutton = tk.Button(self.framebutton, text='Finalizar Cupom', command=self.controller.finalizar_cupom)
        self.finalizarbutton.pack(side='left')


#LIMITE CUPOM--------------------------------------------------------
class ViewConsultarCupom(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Consultar Cupom Fiscal")
        self.controller = controller

        self.framecod = tk.Frame(self)
        self.framecod.pack()

        self.labelcod = tk.Label(self.framecod, text='Número do Cupom:')
        self.labelcod.pack(side='left')

        self.inputcod = tk.Entry(self.framecod, width=20)
        self.inputcod.pack(side='left')

        self.consultarbutton = tk.Button(self.framecod, text='Consultar', command=self.controller.buscaCupom)
        self.consultarbutton.pack(side='left')


#CONTROLADOR CUPOM---------------------------------------------------
class controllerCup:
    def __init__(self, controllerprod):
        self.controllerprod = controllerprod
        self.cupons_fiscais = []

    def getListaProdutos(self):
        return self.controllerprod.getlistaprod()

    def criarCupom(self):
        self.viewcupom = viewCriaCup(self)

    def adicionar_item(self):
        produto_descricao = self.viewcupom.listboxprodutos.get(tk.ACTIVE)
        nro_cupom = self.viewcupom.inputcod.get()
        if not produto_descricao or not nro_cupom:
            messagebox.showerror('Erro', 'Preencha todos os campos.')
            return
        produtoselecionado = next((p for p in self.controllerprod.getlistaprod() if p.descricao == produto_descricao), None)
        if produtoselecionado:
            cupom = next((c for c in self.cupons_fiscais if c.nroCupom == nro_cupom), None)
            if not cupom:
                cupom = Cupom(nro_cupom)
                self.cupons_fiscais.append(cupom)
            cupom.adicionar_item(produtoselecionado)
            messagebox.showinfo('Sucesso', f'Produto "{produto_descricao}" adicionado ao cupom.')
        else:
            messagebox.showerror('Erro', 'Produto não encontrado.')

    def finalizar_cupom(self):
        nro_cupom = self.viewcupom.inputcod.get()
        cupom = next((c for c in self.cupons_fiscais if c.nroCupom == nro_cupom), None)
        if cupom:
            dados = cupom.exibir_dados()
            messagebox.showinfo('Cupom Fiscal', dados)
        else:
            messagebox.showerror('Erro', 'Número de cupom inválido.')

        self.viewcupom.destroy() 

    def consultarCupom(self):
        self.viewcupom = ViewConsultarCupom(self)
    
    def buscaCupom(self):
        nro_cupom = self.viewcupom.inputcod.get()
        cupom = next((c for c in self.cupons_fiscais if c.nroCupom == nro_cupom), None)
        if cupom:
            dados = cupom.exibir_dados()
            messagebox.showinfo('Cupom Fiscal', dados)
        else:
            messagebox.showerror('Erro', 'Cupom não encontrado.')
        self.viewcupom.destroy()

