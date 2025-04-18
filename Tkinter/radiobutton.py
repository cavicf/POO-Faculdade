#RADIOBUTTON: campo de seleção check, seleciona marcando como selecionados

import tkinter as tk
janela = tk.Tk()
janela.title('RADIOBUTTON')
janela.geometry('250x250')

def obter():
    resultado = selecionado1.get()
    print(resultado)

selecionado1 = tk.IntVar() #facilita a comunicação entre os widgets da interface gráfica e o código para guardar o valor selecionado.

rad1 = tk.Radiobutton(janela, command= obter, text='primeiro', value=1, variable=selecionado1) #aqui criamos um objeto da classe tk de radiobutton e passamos como parametro o lugar onde ela esta que é a janela, o seu texto que será exibido e o seu valor
rad1.grid(column=0, row=0, padx=10, pady=10) #aqui posicionamos na janela

rad2 = tk.Radiobutton(janela, command=obter, text='segundo', value=2, variable=selecionado1)#o value representa o valor que a seleção daquele campo assume , pode ser também string e booleano , ou seja o resultado
rad2.grid(column=0, row=1, padx=10, pady=10) 

rad3 = tk.Radiobutton(janela, command= obter, text='terceiro', value=3, variable=selecionado1) #precisa do commando pois funciona por seleção no clique 
rad3.grid(column=0, row=2, padx=10, pady=10) 

janela.mainloop()