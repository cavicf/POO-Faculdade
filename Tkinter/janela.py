#Widgets: botões, etiquetas, caixas de textos e muito mais
#Os widgets possuem atributos padroes como dimensões, cores. fontes, ancoras, estilos de relevo, cursores e muito mais. Esses atributos podem ser alterados de acordo com a aplicação desenvolvida
#CRIAÇÃO DA PRIMEIRA JANELA: criar, definir titulo, configurar tamanho, alterar cor de fundo, alterar icone e tornar nao redimensionavel


#from tkinter import * da pra importar a biblioteca assim
import tkinter as tk #mas é preferivel assim para não causar confusão pois tudo q usarmos do tkinter tera q ter o prefixo tk. antes

janela = tk.Tk() #cria a janela principal, serve de base pra todos os widgets depois. Ao fazer isso também cria um objeto da classe tk, ou seja, janela agora é um objeto da classe tk e ja possui alguns atributos proprios q o tkinter tras com ele

janela.title('Janela tkinter') #define o titulo da janela principal. Por isso aqui n precisa do tk. pois agora janela ja é um objeto da classe tk que possui atributos e metodos

janela.geometry('300x250') #define as dimensões da janela, o primeiro valor define a largura e o segundo define a altura, são separados por um x e devem estar entre aspas simples

janela.config(bg='#bbede7') #define a cor de fundo da janela, bg é abreviação para background e entre aspas simples passa-se o código da cor. Esee método .config permite alterar propriedades de um widget já criado, podendo configurar texto, fonte, tamanho, comportamento, e mais.

#icone = tk.PhotoImage(file= 'logo.png') aqui cria um objeto tk de imagem para usar de icone, massa como atributo o file com o nome do arquivo que tem q estar na mesma pasta
#janela.iconphoto(False, icone) aqui altera o icone da janela, o primeiro parametro é falso para desativar o icone original e em seguida é passado o novo icone

janela.resizable(width=True, height=False) #define se a janela pode ser redimensionada pelo usuario, ele permite habilitar ou desabilitar o redimensionamento horizontal (largura) e vertical (altura) separadamente. O primeiro parametro é a largura e o segundo a altura e são booleanos, caso true pode redimensionar, se false não pode e fica travado

janela.minsize(300, 200) #define o tamanho minimo da janela
janela.maxsize(800, 600) #define o tamanho maximo da janela, também é uma forma de limitar o redimensionamento

janela.mainloop() #esse loop mantém a janela aberta, detecta o cliques e atualiza os elementos, gerenciando a interção do usuário. Geralmente é o ultimo a ser declarado pois é ele q vai controlar a abertura da janela e as interações dela

