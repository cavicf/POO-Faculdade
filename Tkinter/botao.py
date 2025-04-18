# BOTÃO: é um widget que serve para executar alguma ação como dar inicio a um evento, cancelar um evento, submeter algo, etc

import tkinter as tk

janela = tk.Tk()
janela.title('BOTÃO')
janela.geometry('250x250')

global contador #definindo a variavel como global para utilizar dentro da fução
contador = 0

def executaBotao(): #criando uma função que será executada ao clicar no botão
    global contador
    texto1 = 'numero impar: '
    texto2 = 'numero par: '
    if (contador %2) == 0:
        resultado = texto2 + str(contador)
        label.config(text= resultado)  #Aqui estamos definindo que o texto da label sera alterado de acordo com a execução da função, passamos o atributo da label que será alterado com o metodo .configure
    else:
        resultado = texto1 + str(contador)
        label.config(text = resultado) #LEMBRE: o .config serve pra alterar a configuração original do widget
    contador += 1

label = tk.Label(janela, width=20, height=2, text='texto sera apresentado', bg='white', relief='flat', fg='black')
label.pack(side='left')


botao = tk.Button(janela, width=10, height=1, text='Clique aqui', bg='grey', relief='groove', fg='white', command=executaBotao)#com o command=nome-da-função faz o link do boão com a função, ou seja, agora a função será executada ao apertar o botao

#aqui cria um objeto da classe tk de botão e são passados alguns atributos assim como na label, a unica diferença q usamos aqui foi o relief que muda o estilo do botão (tambem funciona pra label)
botao.pack(side='left', padx=5) #assim como a label temos que posiciona-lo na janela

janela.mainloop()