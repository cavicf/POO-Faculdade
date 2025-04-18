#Camily Victal Finamor - 2024001197
class Pessoa:
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def cpf(self):
        return self.__cpf
    
    def printDescricao(self):
        print(f"Nome: {self.nome}, Endereço: {self.endereco}, Idade: {self.idade}, CPF: {self.cpf}")

###########################################################################################

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        if titulacao != "Doutor":
            raise ErroTitulacaoInvalida(f"Titulação inválida para o professor {nome}, deve ser 'Doutor'\n")
        if idade < 30:
            raise ErroIdadeInvalida(f"A idade do professor {nome} deve ser igual ou maior que 30 anos\n")
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        super().printDescricao()
        print(f"Titulação: {self.titulacao}")

############################################################################################

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        if curso not in ["CCO", "SIN"]:
            raise ErroCursoInvalido(f"Curso inválido para o aluno {nome}, deve ser 'CCO' ou 'SIN'\n")
        if idade < 18:
            raise ErroIdadeInvalida(f"A idade do aluno {nome} deve ser igual ou maior que 18 anos\n")
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        super().printDescricao()
        print(f"Curso: {self.curso}")

#############################################################################################

class Cadastro:
    def __init__(self):
        self.pessoas = []
    
    def adicionarPessoa(self, pessoa):
        for p in self.pessoas:
            if p.cpf == pessoa.cpf:
                raise Exception(f"CPF {pessoa.cpf} já está cadastrado\n")
        self.pessoas.append(pessoa)
    
    def listarPessoas(self):
        for pessoa in self.pessoas:
            pessoa.printDescricao()
            print()

################################################################################################

class ErroIdadeInvalida(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

###############################################################################################

class ErroCursoInvalido(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

###############################################################################################

class ErroTitulacaoInvalida(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

##############################################################################################
if __name__ == "__main__":
    cadastro = Cadastro()
    try:
        professorValido = Professor("Dr. João", "Rua A", 40, "12345678900", "Doutor")
        cadastro.adicionarPessoa(professorValido)
    except (ErroIdadeInvalida, ErroTitulacaoInvalida, Exception) as e:
        print(e)

    try:
        alunoInvalido = Aluno("Ana", "Rua B", 17, "12345678901", "SIN")
        cadastro.adicionarPessoa(alunoInvalido)
    except (ErroIdadeInvalida, ErroCursoInvalido, Exception) as e:
        print(e)

    try:
        professorInvalido = Professor("José", "Rua C", 29, "12345678902", "Mestre")
        cadastro.adicionarPessoa(professorInvalido)
    except (ErroIdadeInvalida, ErroTitulacaoInvalida, Exception) as e:
        print(e)

    try:
        alunoValido = Aluno("Maria", "Rua D", 20, "12345678903", "CCO")
        cadastro.adicionarPessoa(alunoValido)
    except (ErroIdadeInvalida, ErroCursoInvalido, Exception) as e:
        print(e)

    print('PESSOAS CADASTRADAS:')
    cadastro.listarPessoas()
