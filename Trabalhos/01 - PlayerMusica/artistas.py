import tkinter as tk
from tkinter import messagebox
#MODEL-----------------------------------------------------------------
class Artista:
    def __init__(self, nome):
        self.__nome = nome 
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas

#VIEW CADASTRAR--------------------------------------------------------
class viewCadastarArtista(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry = ('300x250')
        self.title('Cadastrar Artista')

        self.frameNome = tk.Frame(self)
        self.frameNome.pack()

        self.labelNome = tk.Label(self.frameNome, text='Digite o nome:')
        self.labelNome.pack(side='left')

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')

        self.frameBotao = tk.Frame(self)
        self.frameBotao.pack()

        self.botaoCadastra = tk.Button(self.frameBotao, text='Cadastrar', command=self.controlador.salvarArtista)
        self.botaoCadastra.pack(side='left')

#VIEW CONSULTAR--------------------------------------------------------
class viewConsultarArtista(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry = ('300x250')
        self.title('Consultar Artista')

        self.frameProcurar = tk.Frame(self)
        self.frameProcurar.pack()

        self.labelProcurar = tk.Label(self.frameProcurar, text='Digite o nome:')
        self.labelProcurar.pack(side='left')

        self.inputProcurar = tk.Entry(self.frameProcurar, width=20)
        self.inputProcurar.pack(side='left')

        self.frameBotao = tk.Frame(self)
        self.frameBotao.pack()

        self.botaoConsulta = tk.Button(self.frameBotao, text='Consultar', command=self.controlador.procurarArtista)
        self.botaoConsulta.pack(side='left')

#VIEW MOSTRA ARTISTA--------------------------------------------------------
class mostraArtista:
    def __init__(self, mensagem):
        messagebox.showinfo('SUCESSO:', mensagem)

#CONTROLADOR ARTISTAS--------------------------------------------------
class controladorArtista:
    def __init__(self, controladorPrincipal):
        self.listaArtistas = [Artista("Vários Artistas")]
        self.controladorPrincipal = controladorPrincipal

    def cadastrarArtista(self):
        self.viewCadastra = viewCadastarArtista(self)
    
    def consultarArtista(self):
        self.viewConsulta = viewConsultarArtista(self)

    def salvarArtista(self):
        artNome = self.viewCadastra.inputNome.get()
        if not artNome:
            messagebox.showerror('ERRO:', 'O campo deve ser preenchido')
            return
        for art in self.listaArtistas:
            if artNome == art.nome:
                messagebox.showerror('ERRO:', 'O artista já está cadastrado')
                return
        artista = Artista(artNome)
        self.listaArtistas.append(artista)
        messagebox.showinfo('SUCESSO:','Artista cadastrado com sucesso')
        self.viewCadastra.destroy()

    def addAlbuns(self, Album):
        for busca in self.listaArtistas:
            if busca.nome == Album.artista:
                busca.albuns.append(Album)
                self.addMusica(Album)

    def addMusica(self, Album):
        for busca in self.listaArtistas:
            if busca.nome == Album.artista:
                for buscamusica in Album.faixas:
                    if buscamusica not in busca.musicas:
                        busca.musicas.append(buscamusica)


    def getlistaArtistas(self):
        artistas = []
        for art in self.listaArtistas:
            artistas.append(art.nome)
        return artistas
    
    def getArtista(self, nome):
        artistares = None
        for art in self.listaArtistas:
            if art.nome == nome:
                artistares = art
                return artistares
        return False
    
    def getMusicas(self, nome, musica):
        musicares = None
        for art in self.listaArtistas:
            if art.nome == nome:
                for music in art.musicas:
                    if music.titulo == musica:
                        musicares = music
                        return musicares
        return False

    def procurarArtista(self):
        artNome = self.viewConsulta.inputProcurar.get()
        art = self.getArtista(artNome)
        if not art:
            messagebox.showerror('ERRO:', 'Artista não encontrado')
        else:
            mensagem = f'Artista: {art.nome}\n'
            if art.albuns:
                mensagem += 'Albuns: \n'
            for alb in art.albuns:
                mensagem += " Album: " + alb.titulo + '\n'
                mensagem += "  Musicas Album: " + '\n'
                for faixa in alb.faixas:
                    mensagem += "   Faixa: " + str(faixa.nroFaixa) + ' - ' + faixa.titulo + '\n'
            self.mostraArtista = mostraArtista(mensagem)
            self.viewConsulta.destroy()                