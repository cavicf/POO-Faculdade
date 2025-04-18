#FRAME: é uma região retangular na tela. Um frame pode ser utilizado como classe de base para implementar e organizar widgets. Tipo um container

import tkinter as tk
janela = tk.Tk()
janela.title('FRAMES')
janela.geometry('500x500')

frame1 = tk.Frame(janela, width=200, height=200, bg='blue') #aqui criamos um objeto da classe tk de frame e passamos a janela como parametro, sua altura e largura e a cor de fundo
frame1.grid(row=0, column=0, padx=5, pady=5) #aqui posicionamos o frame na janela

frame2 = tk.Frame(janela, width=200, height=200, bg='red')
frame2.grid(row=1, column=0, padx=5, pady=5)

frame3 = tk.Frame(janela, width=200, height=200, bg='green')
frame3.grid(row=0, column=1, padx=5, pady=5)

frame4 = tk.Frame(janela, width=200, height=200, bg='yellow')
frame4.grid(row=1, column=1, padx=5, pady=5)

frame5 = tk.Frame(frame1, width=50, height=50, bg='pink') #aqui posicionamos um frame dentro de outro frame
frame5.grid(column=0, row=0, padx=50, pady=50)

janela.mainloop()