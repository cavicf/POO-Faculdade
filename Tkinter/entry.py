#ENTRY: campos de inserção, caixas de entrada de textos que interagem com o usuário

import tkinter as tk

janela = tk.Tk()
janela.title('ENTRY')
janela.geometry('250x250')

#função que pega a inserção
def obter():
    nome = entry_nome.get() #aqui define que será recolhido da entry oq for escrito e colocado na variavel
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_nomere.config(text= 'Nome: ' + nome) #aqui alteramos o texto exibido com a resposta
    label_idadere.config(text= 'Idade: ' + idade)
    label_paisre.config(text= 'Pais: ' + pais)

    entry_nome.delete(0,len(nome)) #aqui define que será apagado tudo que estiver escrito no entry do inicio 0 até o tamanho da string 
    entry_idade.delete(0, len(idade))
    entry_pais.delete(0, len(pais))

#nome-----------------------------------------------------------------------------------------
label_nome = tk.Label(janela, width=10, height=2, text='Nome: ', font=('Arial 10'))
label_nome.grid(row=0, column=0)
entry_nome= tk.Entry(janela, width=15, font=('Arial 10')) #aqui criamos um objeto da classe tk de entry, define q será na janela e a largura (NAO PODE MEXER NA ALTURA DE ENTRY), define a font pra ajustar a altura como gambiarra
entry_nome.grid(row=0, column=1, padx=5, pady=5)#posiciona na janela

#idade----------------------------------------------------------------------------------------
label_idade = tk.Label(janela, width=10, height=2, text='Idade: ', font=('Arial 10'))
label_idade.grid(row=1, column=0)
entry_idade= tk.Entry(janela, width=15, font=('Arial 10')) 
entry_idade.grid(row=1, column=1, padx=5, pady=5)#posiciona na janela

#pais-----------------------------------------------------------------------------------------
label_pais = tk.Label(janela, width=10, height=2, text='Pais: ', font=('Arial 10'))
label_pais.grid(row=2, column=0)
entry_pais= tk.Entry(janela, width=15, font=('Arial 10'), state='disabled') #com o state determimamos se a entry esta desativada ou ativa passando o parametro
entry_pais.grid(row=2, column=1, padx=5, pady=5)

#respostas------------------------------------------------------------------------------------
label_nomere = tk.Label(janela, width=10, height=2, text='Nome: ', font=('Arial 10'))
label_nomere.grid(row=0, column=2)

label_idadere = tk.Label(janela, width=10, height=2, text='Idade: ', font=('Arial 10'))
label_idadere.grid(row=1, column=2)

label_paisre = tk.Label(janela, width=10, height=2, text='Pais: ', font=('Arial 10'))
label_paisre.grid(row=2, column=2)

botao = tk.Button(janela,command=obter ,width=10, height=1, text='ver', bg='grey', relief='groove', fg='white')
botao.grid(row=3, column=0, padx=5, pady=10)


janela.mainloop()