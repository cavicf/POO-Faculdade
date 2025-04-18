#Camily Victal Finamor - 2024001197
import tkinter as tk
import albuns as album
import artistas as artista
import playlists as playlist
import musicas as music

#VIEW PRINCIPAL-----------------------------------------------------------
class viewPrincipal:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.geometry('300x250')
        self.menu = tk.Menu(self.root)
        self.menuArtista = tk.Menu(self.menu)
        self.menuAlbum = tk.Menu(self.menu)
        self.menuPlaylist = tk.Menu(self.menu)

        self.menuArtista.add_command(label='Cadastrar', command=self.controlador.cadastrarArtista)
        self.menuArtista.add_command(label='Consultar', command=self.controlador.consultarArtista)
        self.menu.add_cascade(label='Artista', menu=self.menuArtista)

        self.menuAlbum.add_command(label='Cadastrar', command=self.controlador.cadastrarAlbum)
        self.menuAlbum.add_command(label='Consultar', command=self.controlador.consultarAlbum)
        self.menu.add_cascade(label='Álbum', menu=self.menuAlbum)

        self.menuPlaylist.add_command(label='Cadastar', command=self.controlador.cadastrarPlaylist)
        self.menuPlaylist.add_command(label='Consultar', command=self.controlador.consultarPlaylist)
        self.menu.add_cascade(label='Playlist', menu=self.menuPlaylist)

        self.root.config(menu=self.menu)

#CONTROLADOR PRINCIPAL----------------------------------------------------
class controladorPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Player - Menu')
        
        self.controladorArtista = artista.controladorArtista(self)
        self.controladorAlbum = album.controladorAlbum(self)
        self.controladorPlaylist = playlist.controladorPlaylist(self)
        self.controladorMusica = music.controladorMusica()

        self.view = viewPrincipal(self.root, self)
        self.root.mainloop()

    def cadastrarArtista(self):
        return self.controladorArtista.cadastrarArtista()
    
    def consultarArtista(self):
        return self.controladorArtista.consultarArtista()
    
    def cadastrarAlbum(self):
        return self.controladorAlbum.cadastrarAlbum()
    
    def consultarAlbum(self):
        return self.controladorAlbum.consultarAlbum()
    
    def cadastrarPlaylist(self):
        return self.controladorPlaylist.cadastrarPlaylist()
    
    def consultarPlaylist(self):
        return self.controladorPlaylist.consultarPlaylist()

#MAIN---------------------------------------------------------------------
if __name__ == '__main__':
    c = controladorPrincipal()