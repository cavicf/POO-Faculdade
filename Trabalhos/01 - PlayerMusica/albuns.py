import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

#MODEL-----------------------------------------------------------------
class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__faixas = []

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def ano(self):
        return self.__ano

    @property
    def faixas(self):
        return self.__faixas
        
#VIEW CADASTRAR--------------------------------------------------------
class viewCadastrarAlbum(tk.Toplevel):
    def __init__(self, controlador, listaartistas):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.musicastemporarias = []
        self.geometry = ('300x250')
        self.title('Cadastrar Album')

        self.frameTitulo = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameArtista = tk.Frame(self)
        self.frameArtista.pack()
        self.frameAno = tk.Frame(self)
        self.frameAno.pack()
        self.frameMusica = tk.Frame(self)
        self.frameMusica.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text='Digite o titulo:')
        self.labelTitulo.pack(side='left')
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side='left')

        self.labelArtista = tk.Label(self.frameArtista, text='Selecione o Artista')
        self.labelArtista.pack(side='left')
        self.escolhaCombo = tk.StringVar()
        self.comboArtista = Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.comboArtista.config(values= listaartistas)
        self.comboArtista.pack(side='left')
        
        self.labelAno = tk.Label(self.frameAno, text='Ano:')
        self.labelAno.pack(side='left')
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side='left')

        self.botaoMusica = tk.Button(self.frameMusica,text='Add Musica', command=self.controlador.adicionarMusica)
        self.botaoMusica.pack(side='left')
        self.inputMusica = tk.Entry(self.frameMusica, width=20)
        self.inputMusica.pack(side='left')
    
        self.frameBotao = tk.Frame(self)
        self.frameBotao.pack()

        self.botaoCadastra = tk.Button(self.frameBotao, text='Cadastrar', command=self.controlador.salvarAlbum)
        self.botaoCadastra.pack(side='left')

#VIEW CONSULTAR--------------------------------------------------------
class viewConsultarAlbum(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry = ('300x250')
        self.title('Consultar Album')

        self.frameProcurar = tk.Frame(self)
        self.frameProcurar.pack()

        self.labelProcurar = tk.Label(self.frameProcurar, text='Digite o titulo:')
        self.labelProcurar.pack(side='left')

        self.inputProcurar = tk.Entry(self.frameProcurar, width=20)
        self.inputProcurar.pack(side='left')

        self.frameBotao = tk.Frame(self)
        self.frameBotao.pack()

        self.botaoConsulta = tk.Button(self.frameBotao, text='Consultar', command=self.controlador.procurarAlbum)
        self.botaoConsulta.pack(side='left')

#VIEW MOSTRA ALBUM----------------------------------------------------
class mostraAlbum:
    def __init__(self, mensagem):
        messagebox.showinfo('SUCESSO:', mensagem)

#CONTROLADOR ALBUM--------------------------------------------------
class controladorAlbum:
    def __init__(self, controladorPrincipal):
        self.controladorPrincipal = controladorPrincipal
        self.listaAlbuns = []
        

    def cadastrarAlbum(self):
        listaartistas = self.controladorPrincipal.controladorArtista.getlistaArtistas()
        self.viewCadastrar = viewCadastrarAlbum(self, listaartistas)
    
    def consultarAlbum(self):
        self.viewConsultar = viewConsultarAlbum(self)
    
    def adicionarMusica(self):
        musica = self.viewCadastrar.inputMusica.get()
        if not musica:
            messagebox.showerror('ERRO:', 'O campo deve ser preenchido!')
        self.viewCadastrar.musicastemporarias.append(musica)
        self.viewCadastrar.inputMusica.delete(0, tk.END)

    def salvarAlbum(self):
        titulo = self.viewCadastrar.inputTitulo.get()
        artista = self.viewCadastrar.escolhaCombo.get()
        ano =  self.viewCadastrar.inputAno.get()
        if not titulo or not artista or not ano:
            messagebox.showerror('ERRO:', 'Todos os campos devem ser preenchidos!')
        album = Album(titulo, artista, ano)
        for nroFaixa, musica in enumerate(self.viewCadastrar.musicastemporarias, start=1):
            musica = self.controladorPrincipal.controladorMusica.criarMusica(musica,artista,titulo,nroFaixa)
            album.faixas.append(musica)
        self.listaAlbuns.append(album)
        self.controladorPrincipal.controladorArtista.addAlbuns(album)
        self.controladorPrincipal.controladorArtista.addMusica(album)
        messagebox.showinfo('SUCESSO:', 'Album cadastrado com sucesso')
        self.viewCadastrar.destroy()

    def getAlbum(self, titulo):
        albumres = None
        for alb in self.listaAlbuns:
            if alb.titulo == titulo:
                albumres = alb
                return albumres
        return False
    
    def procurarAlbum(self):
        titulo = self.viewConsultar.inputProcurar.get()
        album = self.getAlbum(titulo)
        if not album:
            messagebox.showerror('ERRO', 'Album não encontrado')
        else:
            mensagem = f'Album: {album.titulo}\n'
            mensagem += f'Artista: {album.artista}\n'
            mensagem += f'Ano de lançamento: {album.ano}\n'
            if album.faixas:
                mensagem += 'Faixas:\n'
            for faixas in album.faixas:
                mensagem += "    Faixa: " + str(faixas.nroFaixa) + ' - ' + faixas.titulo + '\n'
            self.mostraArtista = mostraAlbum(mensagem)                 


