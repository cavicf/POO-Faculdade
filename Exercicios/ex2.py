class Artista:
    def __init__(self, nome):
        # Inicializa o artista com seu nome, e listas vazias para álbuns e músicas
        self.__nome = nome
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        # Propriedade para acessar o nome do artista
        return self.__nome

    @property
    def albuns(self):
        # Propriedade para acessar a lista de álbuns do artista
        return self.__albuns

    @property
    def musicas(self):
        # Propriedade para acessar a lista de músicas do artista
        return self.__musicas

    def addAlbum(self, album):
        # Método para adicionar um álbum à lista do artista
        self.__albuns.append(album)

    def addMusica(self, musica):
        # Método para adicionar uma música à lista do artista
        self.__musicas.append(musica)

#########################################################################################################################################

class Album:
    def __init__(self, titulo, artista, ano):
        # Inicializa o álbum com título, artista e ano, e uma lista vazia de faixas
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__faixas = []
        artista.addAlbum(self)  # Adiciona o álbum à lista de álbuns do artista

    @property
    def titulo(self):
        # Propriedade para acessar o título do álbum
        return self.__titulo

    @property
    def artista(self):
        # Propriedade para acessar o artista do álbum
        return self.__artista

    @property
    def ano(self):
        # Propriedade para acessar o ano do álbum
        return self.__ano

    @property
    def faixas(self):
        # Propriedade para acessar a lista de faixas do álbum
        return self.__faixas

    def addFaixa(self, titulo, artista=None):
        # Método para adicionar uma faixa ao álbum
        if artista is None:
            artista = self.__artista  # Se o artista não for especificado, usa o artista do álbum
        nroFaixa = len(self.__faixas)  # Número da nova faixa
        musica = Musica(titulo, artista, self, nroFaixa)  # Cria um objeto de música
        self.__faixas.append(musica)  # Adiciona a música à lista de faixas

###########################################################################################################################################

class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        # Inicializa a música com título, artista, álbum e número da faixa
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa
        artista.addMusica(self)  # Adiciona a música à lista de músicas do artista

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

############################################################################################################################################

class Playlist:
    def __init__(self, nome):
        # Inicializa a playlist com um nome e uma lista vazia de músicas
        self.__nome = nome
        self.__musicas = []

    @property
    def nome(self):
        # Propriedade para acessar o nome da playlist
        return self.__nome
    
    @property 
    def musicas(self):
        # Propriedade para acessar a lista de músicas da playlist
        return self.__musicas
    
    def addMusica(self, musica):
        # Método para adicionar uma música à lista da playlist
        self.__musicas.append(musica)

################################################################################################################################################

if __name__ == "__main__":    
    listaAlbuns = []  # Lista para armazenar os álbuns
    art1 = Artista('Coldplay')  # Cria um artista chamado Coldplay
    album1 = Album('Mylo Xyloto', art1, 2011)  # Cria um álbum de Coldplay
    album1.addFaixa('Paradise')  # Adiciona faixas ao álbum
    album1.addFaixa('Hurts Like Heaven')
    album1.addFaixa('Charlie Brown') 
    listaAlbuns.append(album1)  # Adiciona o álbum à lista de álbuns

    album2 = Album('A Head Full of Dreams', art1, 2015)  # Outro álbum de Coldplay
    album2.addFaixa('A Head Full of Dreams')
    album2.addFaixa('Birds')
    album2.addFaixa('Everglow')
    listaAlbuns.append(album2)  # Adiciona o álbum à lista de álbuns

    art2 = Artista('Skank')  # Cria um artista chamado Skank
    album3 = Album('Siderado', art2, 1998)  # Cria um álbum de Skank
    album3.addFaixa('Resposta')
    album3.addFaixa('Saideira')
    album3.addFaixa('Romance Noir')
    listaAlbuns.append(album3)  # Adiciona o álbum à lista de álbuns

    # Criar e exibir uma playlist com as músicas do álbum "Mylo Xyloto"
    playlist1 = Playlist('pl-mylo-xyloto')
    for musica in album1.faixas:
        playlist1.addMusica(musica)  # Adiciona as músicas do álbum à playlist
    print(playlist1.nome)  # Exibe o nome da playlist
    print('Músicas:')
    for musica in playlist1.musicas:
        print(musica.titulo)  # Exibe os títulos das músicas da playlist
    print()
    
    # Criar e exibir uma playlist com todas as músicas do Coldplay   
    playlist2 = Playlist('pl-coldplay')
    for musica in art1.musicas:
        playlist2.addMusica(musica)  # Adiciona as músicas do artista à playlist
    print(playlist2.nome)  # Exibe o nome da playlist
    print('Músicas:')
    for musica in playlist2.musicas:
        print(musica.titulo)  # Exibe os títulos das músicas da playlist

    print()

    # Criar e exibir uma playlist contendo uma música de cada álbum
    playlist3 = Playlist('pl-coletanea')
    for album in listaAlbuns:
        musicas = album.faixas
        playlist3.addMusica(musicas[0])  # Adiciona a primeira música de cada álbum à playlist
    print(playlist3.nome)  # Exibe o nome da playlist
    print('Músicas:')
    for musica in playlist3.musicas:
        print(musica.titulo)  # Exibe os títulos das músicas da playlist
