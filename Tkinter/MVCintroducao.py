import tkinter as tk
from tkinter import messagebox

#------------------------------------------------------------------------------------------------------------------------------------
#CLASSE MODELO: aqui é feita a construção de classes modelo como ja visto na orientação a objetos anteriormente, definindo os atributos e propertys
class ModelCliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

#----------------------------------------------------------------------------------------------------------------------------------
#CLASSE VIEW: essa classe é responsável pela construção da interface gráfica do modelo
class View():
    def __init__(self, master, controller): #ela recebe a janela principal vinda do controlador e o próprio controlador para fazer uso de suas funções
        self.controller = controller #armazena a referencia ao controlador para utilizar os métodos dele
        self.janela = tk.Frame(master) #inicializa um frame na janela raiz criada pelo controlador, essa será nossa janela de fato, pois o controlador é responsável somente de dar inicio ao programa e ao loop da janela raiz. Aqui que serão colocados os widgets e a criação de outros frames.
        self.janela.pack() #faz o posicionamento desse frame na raiz
        self.frame1 = tk.Frame(self.janela) #faz a criação de um frame dentro do frame principal janela
        self.frame2 = tk.Frame(self.janela) #faz a criação de um frame dentro do frame principal janela
        self.frame1.pack() #posiciona esse novo frame no frame principal janela
        self.frame2.pack() #posiciona esse novo frame no frame principal janela
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ") #criando uma label que ficara no frame 1 exibindo o texto 'nome:'
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ") #criando uma label que ficara no frame 2 exibindo o texto 'email:'
        self.labelInfo1.pack(side="left") #posicionando a label no frame no lado esquerdo
        self.labelInfo2.pack(side="left") #posicionando a label no frame no lado esquerdo

        self.inputText1 = tk.Entry(self.frame1, width=20) #criando um campo de texto que ficara no frame 1, correspondente a label nome
        self.inputText1.pack(side="left") #posicionando o campo no frame ao lado esquerdo
        self.inputText2 = tk.Entry(self.frame2, width=20) #criando um campo de texto que ficara no frame 2, correspondente a label email
        self.inputText2.pack(side="left") #posicionando o campo no frame ao lado esquerdo           
      
        self.buttonSubmit = tk.Button(self.janela,text="Salva") #criando um botão com o titulo "Salva" no frame principal janela      
        self.buttonSubmit.pack(side="left") #posicionando esse botão no lado esquerdo da janela
        self.buttonSubmit.bind("<Button>", controller.salvaHandler) #conectando o evento "<Button>" que significa o clique do mouse à função salvaHandler do controlador, não precisa do () pois estamos passando apenas uma referencia da função ao bind, que só chamará a função quando o evento de clique ocorrer
      
        self.buttonClear = tk.Button(self.janela,text="Limpa") #criando um botão com o titulo "Limpa" no frame principal janela       
        self.buttonClear.pack(side="left") #posicionando esse botão no lado esquerdo da janela
        self.buttonClear.bind("<Button>", controller.clearHandler) #conectando o evento "<Button>" que significa o clique do mouse à função clearHandler do controlador, não precisa do () pois estamos passando apenas uma referencia da função ao bind, que só chamará a função quando o evento de clique ocorrer            

    def mostraJanela(self, titulo, mensagem): #cria uma função para fazer a demonstração da mensagem na tela, que recebe o titulo e a mensagem do controlador, pois ele que determinará quando o que essa mensagem mostrará dependendo dos eventos
        messagebox.showinfo(titulo, mensagem) #aqui é a criação da messagebox com o titulo e mensagem do controlador

#-------------------------------------------------------------------------------------------------------------------------------
#CLASSE CONTROLADORA: essa classe é responsavel porn fazer a ligação entre o modelo e a view, ela geralmente cria a janela principal do programa e inicializa o loop, guarda as listas de dados dos modelos e possui as funções de callback dos botões
class Controller():       
    def __init__(self):
        self.root = tk.Tk() #aqui cria a janela principal do programa
        self.root.geometry('300x100') #define o tamanho dessa janela
        self.listaClientes = [] #cria a lista que guardará os clientes cadastrados

        self.view = View(self.root, self) #cria a view como se estivesse criando um objeto da classe View e passa como parametro a janela raiz e a si proprio (controlador) para que a view possa fazer a construção gráfica e utilizar as funções de callback 

        self.root.title("Exemplo MVC") #define um titulo pra janela raiz
        self.root.mainloop() #Inicia o mainloop que manterá a janela aberta até finalizar todas as operações

    def salvaHandler(self, event): #função de callback do botão de salvar, ele recebe o evento de clique da view que é o "<Button>"
        nomeCli = self.view.inputText1.get() #coleta o que foi escrito no campo de texto do nome e salva numa variavel
        emailCli = self.view.inputText2.get() #coleta o que foi escrito no campo de texto do email e salva numa variavel
        cliente = ModelCliente(nomeCli, emailCli) #cria um objeto da classe modelo com esse nome e email 
        self.listaClientes.append(cliente) #e o coloca na lista de dados
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso') #define o titulo e a mensagem da messagebox a chamando como uma função
        self.clearHandler(event) #chama a função de callback do clear para limpar os campos após a inserção e salvamento

    def clearHandler(self, event): #função de callback do botão de limpar, ele recebe o evento de clique da view que é o "<Button>"
        self.view.inputText1.delete(0, len(self.view.inputText1.get())) #define que o campo de texto 1 será deletado do inicio ao fim
        self.view.inputText2.delete(0, len(self.view.inputText2.get())) #define que o campo de texto 2 será deletado do inicio ao fim

#-----------------------------------------------------------------------------------------------------------------------------
#MAIN: responsavel por chamar o controlador e dar inicio ao programa
if __name__ == '__main__':
    c = Controller() #cria um objeto da classe controladora que dará start ao programa, fazendo as ligações com as demais classes 