#MODELO MUSICAS-------------------------------------------------------
class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        # Inicializa a música com título, artista, álbum e número da faixa
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

    @property
    def titulo(self):
        # Propriedade para acessar o título da música
        return self.__titulo
    
    @property
    def artista(self):
        # Propriedade para acessar o artista da música
        return self.__artista

    @property
    def album(self):
        # Propriedade para acessar o álbum da música
        return self.__album

    @property
    def nroFaixa(self):
        # Propriedade para acessar o número da faixa
        return self.__nroFaixa

#CONTROLADOR MUSICA----------------------------------------------------
class controladorMusica:
    def __init__(self):
        self.listaMusicas = []
    
    def criarMusica(self, tituloMusica, artista, album, nroFaixa):
        novaMusica = Musica(tituloMusica, artista, album, nroFaixa)
        self.listaMusicas.append(novaMusica)
        return novaMusica