#O Tkinter possui 3 mecanismos pra gerenciamento de geometria, ou seja, de posicionamento/coordenadas, que são: .place, .pack, . grid

#O place usa coordenadas absolutas em pixels
#O pack coloca os widgets em um dos quatro lados.
#o grid coloca os widgets em uma grade com linhas e colunas

import tkinter as tk
janela = tk.Tk()
janela.title('Geometria')
janela.geometry('300x300')
janela.config(bg='grey')

label_place = tk.Label(janela, width=15, height=2, text='exemplo de place', fg='white', bg='black')
label_place.place(x=80, y=80) #determina a distancia em pixels das coordenadas do eixo x e y em que a label será posicionada (x=horizontal e y=vertical)

label_grid = tk.Label(janela, width=15, height=2, text='exemplo de grid', fg='white', bg='blue')
label_grid.grid(row=10, column=10)#determina a posição de acordo com linhas e colunas de grade respectivamente

label_pack = tk.Label(janela, width=15, height=2, text='exemplo de pack', fg='white', bg='red')
label_pack.pack() #assim sem nada como parametro, ele centraliza na janela e cria uma pilha caso adicione novos widgets usando o pack. Se passar o parmetro side= pode definir se a label fica no right, left

#ATENÇÃO: o Tkinter não permite misturar diferentes gerenciadores de geometria (como pack, grid e place) dentro do mesmo contêiner (janela ou frame). Ou seja, você não pode usar o pack e o grid na mesma janela ao mesmo tempo. ESCOLHER SÓ 1!!

janela.mainloop()