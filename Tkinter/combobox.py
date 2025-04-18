#COMBOBOX: caixa de seleção, com opções listadas que podem ser selecionadas

import tkinter as tk
from tkinter.ttk import Combobox

janela = tk.Tk()
janela.title('COMBOBOX')
janela.geometry('250x250')

label_nome = tk.Label(janela, width=15, height=2, text='Faça sua escolha:', font=('Arial 10'))
label_nome.grid(row=0, column=0, pady=5, padx=5)

label_nomere = tk.Label(janela, width=30, height=2, font=('Arial 10'))
label_nomere.grid(row=3, column=0, pady=5, padx=5)

def obter(): #criando a função que realiza a ação ao apertar o botão
    resultado = combo.get()
    print(resultado)
    label_nomere.config(text= 'A opção escolhida foi: ' + resultado) #alterando o texto da label pra apresentar o resultando conforme a opção escolhida através do combo.get

combo = Combobox(janela) #aqui é criado um objeto da classe tk de combobox, onde o unico parametro passado é a janela que é onde ele estará

combo.config(values= (1,2,3,4, 'joao', 'futi')) #aqui com o config alteramos os atributos padroes do objeto, no caso o values pois estamos adicionando valores as serem listados na combo

combo.grid(row=1, column=0, pady=5, padx=5)#aqui adicionamos e posicionamos a combobox na janela do programa

combo.current(0) #faazendo a pré-definição da primeira opção



botao = tk.Button(janela, command=obter, width=10, height=1, text='ver', bg='grey', relief='groove', fg='white')
botao.grid(row=2, column=0, padx=5, pady=20)



janela.mainloop()