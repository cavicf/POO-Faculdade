#Podemos utilizar classes para ajudar na organização da criação de interfaces

import tkinter as tk

class GUI: #aqui criamos uma classe que receberá toda a estrutura da janela, ou seja, vai encapsular toda a lógica da interface gráfica
    def __init__(self): #construtor da classe 
        self.janela = tk.Tk()
        self.janela.title('CLASSE')
        self.janela.geometry('400x400')
        self.label = tk.Label(self.janela, text='hello World', font=('Arial 20 bold'))
        self.label.pack()
        self.janela.mainloop()
#cria-se toda a estrutura de uma janela como fazia-se normalmente, porem agora utilizando o self como prefixo pois estamos dentro da classe


def main(): #cria-se uma função que chamaremos de main para fazer uma melhor separação e organização. Ela será responsável por dar ínicio ao nosso programa pois mela cria um objeto da classe GUI()
    GUI()

main()#aqui chamamos a função main, que colocará a classe GUI pra funcionar ao criar um objeto