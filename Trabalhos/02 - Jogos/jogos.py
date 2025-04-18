#Aluna: Camily Victal Finamor
#Matricula: 2024001197

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CLASSE MODEL
class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco, controlador):
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco
        self.controlador = controlador
        self.__avaliacao = []
        self.__media = 0

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def console(self):
        return self.__console
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def avaliacao(self):
        return self.__avaliacao
    
    @property
    def media(self):
        return self.__media
    
    @media.setter
    def media(self,valor):
        self.__media = valor

    @codigo.setter
    def codigo(self, valor):
        listajogos = self.controlador.getLista()
        if valor == '':
            raise ValueError("Todos os campos devem ser preenchidos {}".format(valor))
        for jogo in listajogos:
            if jogo.codigo == valor:
                raise ValueError("Jogo ja cadastrado {}".format(valor))
        self.__codigo = valor

    @titulo.setter
    def titulo(self, valor):
        if valor == '':
            raise ValueError("Todos os campos devem ser preenchidos {}".format(valor))
        self.__titulo = valor

    @console.setter
    def console(self, valor):
        if valor == '':
            raise ValueError("Todos os campos devem ser preenchidos {}".format(valor))
        self.consoles = ['XBox','PlayStation', 'Switch', 'PC']
        if not valor in self.consoles:
            raise ValueError("Console inválido: {}".format(valor))
        self.__console = valor

    @genero.setter
    def genero(self, valor):
        if valor == '':
            raise ValueError("Todos os campos devem ser preenchidos {}".format(valor))
        self.generos = ['Ação', 'Aventura', 'Estratégia', 'RPG', 'Esporte', 'Simulação']
        if not valor in self.generos:
            raise ValueError("Genero inválido: {}".format(valor))
        self.__genero = valor
    
    @preco.setter
    def preco(self, valor):
        if valor == '':
            raise ValueError("Todos os campos devem ser preenchidos {}".format(valor))
        if valor < 0 or valor > 500:
            raise ValueError("Preço inválido: {}".format(valor))
        self.__preco = valor

    def adicionarAvaliacao(self, valor):
        self.avaliacoes = [1, 2, 3, 4, 5]
        if not valor in self.avaliacoes:
            raise ValueError("avaliacao inválida: {}".format(valor))
        self.__avaliacao.append(valor)
    
    def calcularmedia(self):
        media = sum(self.avaliacao)/len(self.avaliacao)
        if media >= 0 and media <= 1:
            self.media = 1
        elif media > 1 and media <= 2:
            self.media = 2
        elif media > 2 and media <= 3:
            self.media = 3
        elif media > 3 and media <= 4:
            self.media = 4
        else:
            self.media = 5
        return self.media

    def getJogo(self):
        return "Codigo: " + str(self.codigo)\
        + "\nTitulo: " + str(self.titulo)\
        + "\nConsole: " + str(self.console)\
        + "\nGênero: " + str(self.genero)\
        + "\nPreço: " + str(self.preco)\
        + "\nAvaliação: " + str(self.media)\
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VIEW DO CADASTRO
class ViewCadastrar(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('Cadastrar Jogo')
    
        self.framecodigo = tk.Frame(self)
        self.framecodigo.pack()
        self.frametitulo = tk.Frame(self)
        self.frametitulo.pack()
        self.frameconsole = tk.Frame(self)
        self.frameconsole.pack()
        self.framegenero = tk.Frame(self)
        self.framegenero.pack()
        self.framepreco = tk.Frame(self)
        self.framepreco.pack()
        self.framebotao = tk.Frame(self)
        self.framebotao.pack()
        self.labelcodigo = tk.Label(self.framecodigo, width=7, text='Código:')
        self.labelcodigo.pack(side='left',pady=5, padx=2)
        self.inputcodigo = tk.Entry(self.framecodigo, width=20)
        self.inputcodigo.pack(side='left',pady=5, padx=2)
        self.labeltitulo = tk.Label(self.frametitulo, width=7, text='Título:')
        self.labeltitulo.pack(side='left',pady=5, padx=2)
        self.inputtitulo = tk.Entry(self.frametitulo, width=20)
        self.inputtitulo.pack(side='left',pady=5, padx=2)
        self.labelconsole = tk.Label(self.frameconsole, width=7, text='Console:')
        self.labelconsole.pack(side='left',pady=5, padx=2)
        self.inputconsole = tk.Entry(self.frameconsole, width=20)
        self.inputconsole.pack(side='left',pady=5, padx=2)
        self.labelgenero = tk.Label(self.framegenero, width=7, text='Gênero:')
        self.labelgenero.pack(side='left',pady=5, padx=2)
        self.inputgenero = tk.Entry(self.framegenero, width=20)
        self.inputgenero.pack(side='left',pady=5, padx=2)
        self.labelpreco = tk.Label(self.framepreco, width=7, text='Preço:')
        self.labelpreco.pack(side='left',pady=5, padx=2)
        self.inputpreco= tk.Entry(self.framepreco, width=20)
        self.inputpreco.pack(side='left',pady=5, padx=2)
        self.botaoCadastrar = tk.Button(self.framebotao, text='Cadastrar', command=self.controlador.salvarJogo)
        self.botaoCadastrar.pack(side='left',pady=5, padx=10)
        self.botaoClear = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparCampos)
        self.botaoClear.pack(side='left', pady=5)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VIEW DA CONSULTA 
class ViewConsultar(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('Consultar jogos')

        self.escolhacombo = tk.StringVar()
        self.framecombo = tk.Frame(self)
        self.framecombo.pack()
        self.labelcombo = tk.Label(self.framecombo, width=7, text='Avaliação:')
        self.labelcombo.pack(side='left', padx=2, pady=5)
        self.combo = ttk.Combobox(self.framecombo, width=15, values=(1, 2, 3, 4, 5), textvariable=self.escolhacombo)
        self.combo.pack(side='left', padx=2, pady=5)
        self.combo.bind("<<ComboboxSelected>>", self.controlador.procurarJogo)
        self.framejogo = tk.Frame(self)
        self.framejogo.pack()
        self.textjogo = tk.Text(self.framejogo, height=20,width=40)
        self.textjogo.pack()
        self.textjogo.config(state=tk.DISABLED)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class viewAvaliar(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('Avaliar Jogo')

        self.framecodigo = tk.Frame(self)
        self.framecodigo.pack()
        self.labelcodigo = tk.Label(self.framecodigo, width=7, text='Código:')
        self.labelcodigo.pack(side='left', padx=2, pady=5)
        self.inputcodigo = tk.Entry(self.framecodigo, width=20)
        self.inputcodigo.pack(side='left',padx=2, pady=5)
        self.escolhacombo = tk.StringVar()
        self.framecombo = tk.Frame(self)
        self.framecombo.pack()
        self.labelcombo = tk.Label(self.framecombo, width=7, text='Avalie:')
        self.labelcombo.pack(side='left', padx=2, pady=5)
        self.combo = ttk.Combobox(self.framecombo, width=17, values=(1, 2, 3, 4, 5), textvariable=self.escolhacombo)
        self.combo.pack(side='left', padx=2, pady=5)
        self.framebotao = tk.Frame(self)
        self.framebotao.pack()
        self.botaoavaliar = tk.Button(self.framebotao, text='Avaliar', command= self.controlador.Avaliar)
        self.botaoavaliar.pack(side='left', padx=10, pady=5)
        self.botaolimpa = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparAvaliar)
        self.botaolimpa.pack(side='left', pady=5)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CONTROLADOR JOGO
class ControladorJogo:
    def __init__(self, controladorPrincipal):
        self.controladorPrincipal = controladorPrincipal
        self.listaJogos = []
    
    def CadastrarJogo(self): 
        self.ViewCadastrar = ViewCadastrar(self)

    def ConsultarJogo(self):
        self.ViewConsultar = ViewConsultar(self)

    def AvaliarJogo(self):
        self.ViewAvaliar = viewAvaliar(self)
    
    def salvarJogo(self):
        codigo = self.ViewCadastrar.inputcodigo.get()
        titulo = self.ViewCadastrar.inputtitulo.get()
        console = self.ViewCadastrar.inputconsole.get()
        genero = self.ViewCadastrar.inputgenero.get()
        preco = float(self.ViewCadastrar.inputpreco.get())
        try:
            jogo = Jogo(codigo, titulo, console, genero, preco, self)
            self.listaJogos.append(jogo)
            self.ViewCadastrar.mostraJanela('Sucesso:', 'Jogo cadastrado com sucesso')
            self.ViewCadastrar.destroy()
        except ValueError as error:
            self.ViewCadastrar.mostraJanela('Erro:', error)

    def Avaliar(self):
        codigo = self.ViewAvaliar.inputcodigo.get()
        avaliacao = self.ViewAvaliar.escolhacombo.get()
        if not codigo or not avaliacao:
            messagebox.showinfo('Erro:', 'O campo deve ser preenchido')
        try:
            jogo = self.getjogodaLista(codigo)
            if jogo:
                jogo.adicionarAvaliacao(int(avaliacao))
                self.ViewAvaliar.mostraJanela('Sucesso:', 'Jogo avaliado!')
                self.ViewAvaliar.destroy()
            else:
                self.ViewAvaliar.mostraJanela('Erro:', 'Jogo não encontrado.')
        except ValueError as error:
            self.ViewAvaliar.mostraJanela('Erro:', error)


    def procurarJogo(self, event):
        avalsel = int(self.ViewConsultar.escolhacombo.get())
        self.ViewConsultar.textjogo.config(state='normal')
        self.ViewConsultar.textjogo.delete('1.0', tk.END)
        encontrou = False
        for jogo in self.listaJogos:
            mediajogo = jogo.calcularmedia()
            if mediajogo == avalsel:
                encontrou = True
                jogoSel = jogo.getJogo() + '\n\n'
                self.ViewConsultar.textjogo.insert(tk.END, jogoSel)
        if not encontrou:
            self.ViewConsultar.textjogo.insert(tk.END, 'Nenhum jogo encontrado')
        self.ViewConsultar.textjogo.config(state='disabled')
        

    def getjogodaLista(self, codigo):
        for jogo in self.listaJogos:
            if jogo.codigo == codigo:
                return jogo
            
    def getLista(self):
        lista = []
        for jogo in self.listaJogos:
            lista.append(jogo)
        return lista

    def limparCampos(self):
        self.ViewCadastrar.inputcodigo.delete(0, tk.END)
        self.ViewCadastrar.inputtitulo.delete(0, tk.END)
        self.ViewCadastrar.inputconsole.delete(0, tk.END)
        self.ViewCadastrar.inputgenero.delete(0, tk.END)
        self.ViewCadastrar.inputpreco.delete(0, tk.END)

    def limparAvaliar(self):
        self.ViewAvaliar.inputcodigo.delete(0, tk.END)
        self.ViewAvaliar.combo.set(value='')
    
        
        
