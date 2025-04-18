#LABEL: é o que nos permite apresentar alguns textos dentro da nossa janela, caixas de texto

import tkinter as tk

janela = tk.Tk()

janela.title('Labels')

janela.config(bg='white')

janela.resizable(width=True, height=True)

janela.minsize(300, 200) 
janela.maxsize(800, 600) 

label_name = tk.Label(janela, width=10, height=2, text='Nome: ', bg='purple') #cria um objeto da classe tk de label e passa alguns parametros: primeiro vem onde essa label será colocoda, ou seja, na janela, depois define a largura e altura respectivamente da caixa e em seguida é passado o atributo text= que define o texto a ser exibido. O bg muda a cor de fundo do label 

label_name.grid(row=0, column=0) #aqui vamos definir onde na janela a label será exibida, podem ser usados os metodos .grid .place e .pack dependendo da aplicação. Aqui no caso do grid foi passado a linha e a coluna respectivamente de dimensão da janela como parametro pra posicionar a label.

label_idade = tk.Label(janela, width=10, height=2, text='Idade: ', font=('Arial 15 bold')) #aqui adicionamos a definiçãao da fonte como parametro também, os atributos são passados entre parenteses e aspas simples onde o primeiro é o estilo da fonte, o segundo com o tamanho da fonte e o terceiro define q ela será em negrito
label_idade.grid(row=1, column=0, pady=10) #o pady define a distancia entre acima e abaixo da label ja o padx a distancia das laterais

label_pais= tk.Label(janela, width=10, height=2, text='País: ', fg='red') #aqui adicionamos a definiçãao da cor do texto da label com o atributo fg que é a abreviação de foregorund
label_pais.grid(row=2, column=0)


janela.mainloop()
