import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
#MODEL-----------------------------------------------------------------
class Playlist:
    def __init__(self, nome):
        self.__nome = nome 
        self.__musicas = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
        
#VIEW CADASTRAR--------------------------------------------------------
class viewCadastarPlaylist(tk.Toplevel):
    def __init__(self, controlador, listaartistas):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.musicasSelecionadas = []
        self.geometry = ('300x250')
        self.title('Cadastrar Playlist')

        self.frameNome = tk.Frame(self)
        self.frameNome.pack()

        self.frameArtista = tk.Frame(self)
        self.frameArtista.pack()
        
        self.frameMusicas = tk.Frame(self)
        self.frameMusicas.pack()

        self.labelNome = tk.Label(self.frameNome, text='Digite o nome:')
        self.labelNome.pack(side='left')

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')

        self.labelArtista = tk.Label(self.frameArtista, text='Selecione o Artista')
        self.labelArtista.pack(side='left')
        self.escolhaCombo = tk.StringVar()
        self.comboArtista = Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.comboArtista.config(values= listaartistas)
        self.comboArtista.pack(side='left')
        self.comboArtista.bind("<<ComboboxSelected>>", controlador.atualizarMusicas)

        self.labelMusica = tk.Label(self.frameMusicas, text='Selecione as Musicas:')
        self.labelMusica.pack(side='top', anchor='center')
        self.listaMusica = tk.Listbox(self.frameMusicas)
        self.listaMusica.pack(side='left')

        self.frameBotaoInsere = tk.Frame(self)
        self.frameBotaoInsere.pack()
        self.botaoInsere = tk.Button(self.frameBotaoInsere, text='Inserir', command=controlador.inserirMusica)
        self.botaoInsere.pack(side='left')
        self.botaoCadastra = tk.Button(self.frameBotaoInsere, text='Cadastrar', command=self.controlador.salvarPlaylist)
        self.botaoCadastra.pack(side='left')


#VIEW CONSULTAR--------------------------------------------------------
class viewConsultarPlaylist(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry = ('300x250')
        self.title('Consultar Playlist')

        self.frameProcurar = tk.Frame(self)
        self.frameProcurar.pack()

        self.labelProcurar = tk.Label(self.frameProcurar, text='Digite o nome:')
        self.labelProcurar.pack(side='left')

        self.inputProcurar = tk.Entry(self.frameProcurar, width=20)
        self.inputProcurar.pack(side='left')

        self.frameBotao = tk.Frame(self)
        self.frameBotao.pack()

        self.botaoConsulta = tk.Button(self.frameBotao, text='Consultar', command=self.controlador.procurarPlaylist)
        self.botaoConsulta.pack(side='left')

#VIEW MOSTRA ARTISTA--------------------------------------------------------
class mostraPlaylist:
    def __init__(self, mensagem):
        messagebox.showinfo('SUCESSO:', mensagem)

#CONTROLADOR PLAYLISTS------------------------------------------------------
class controladorPlaylist:
    def __init__(self, controladorPrincipal):
        self.listaPlaylist = []
        self.controladorPrincipal = controladorPrincipal

    def cadastrarPlaylist(self):
        listaartistas = self.controladorPrincipal.controladorArtista.getlistaArtistas()
        self.viewCadastrar = viewCadastarPlaylist(self, listaartistas)
    
    def consultarPlaylist(self):
        self.viewConsultar = viewConsultarPlaylist(self)

    def atualizarMusicas(self, event):
        artistaNome = self.viewCadastrar.comboArtista.get()
        self.viewCadastrar.listaMusica.delete(0, tk.END)  #Limpa as músicas do listbox
        artista = self.controladorPrincipal.controladorArtista.getArtista(artistaNome)
        for musica in artista.musicas:
            self.viewCadastrar.listaMusica.insert(tk.END, musica.titulo)

    def inserirMusica(self):
        nomeMusicaSelecionada = self.viewCadastrar.listaMusica.get(tk.ACTIVE) #armazena a musica selecionada
        nomeArtista = self.viewCadastrar.comboArtista.get()
        musicaSelecionada = self.controladorPrincipal.controladorArtista.getMusicas(nomeArtista, nomeMusicaSelecionada)
        self.viewCadastrar.musicasSelecionadas.append(musicaSelecionada)
        messagebox.showinfo('SUCESSO:', 'Musica inserida')
        self.viewCadastrar.listaMusica.delete(tk.ACTIVE)


    def salvarPlaylist(self):
        nome = self.viewCadastrar.inputNome.get()
        if not nome:
            messagebox.showerror('ERRO:', 'Playlist deve conter um titulo')
        for playlists in self.listaPlaylist:
            if nome == playlists.nome:
                messagebox.showerror('ERRO:', 'Playlist ja existe')
        playlist = Playlist(nome)
        for musica in self.viewCadastrar.musicasSelecionadas:
            playlist.musicas.append(musica)
        self.listaPlaylist.append(playlist)
        messagebox.showinfo('SUCESSO:','Playlist cadastrada com sucesso')
        self.viewCadastrar.destroy()

    def getPlaylist(self, nome):
        playlistres = None
        for playlist in self.listaPlaylist:
            if playlist.nome == nome:
                playlistres = playlist
                return playlistres
        return False
    
    def procurarPlaylist(self):
        nome = self.viewConsultar.inputProcurar.get()
        playlist = self.getPlaylist(nome)
        if not playlist:
            messagebox.showerror('ERRO:','Preencha o campo')
        mensagem = f'Paylist: {playlist.nome}\n  Musicas da Playlist:\n'
        for musica in playlist.musicas:
            mensagem += "   Faixa: " + str(musica.nroFaixa) + ' - ' + musica.titulo + ' - Artista: ' + musica.artista + '\n'
        self.mostrarPlaylist = mostraPlaylist(mensagem)
        self.viewConsultar.destroy()    




    