def mdc(m, n):
    # Função para calcular o máximo divisor comum (MDC) usando o algoritmo de Euclides
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

class Fracao:
    def __init__(self, num, den):
        # Inicializa a fração com numerador e denominador
        self.__num = num        
        self.__den = den     
        self.simplifica()  # Simplifica a fração logo após a inicialização

    def __str__(self):
        # Representação em string da fração
        return str(self.__num) + "/" + str(self.__den)

    @property
    def num(self):
        # Propriedade para acessar o numerador
        return self.__num

    @property
    def den(self):
        # Propriedade para acessar o denominador
        return self.__den       

    def simplifica(self):
        # Método para simplificar a fração
        divComum = mdc(self.__num, self.__den)  # Calcula o MDC
        self.__num = self.__num // divComum  # Divide o numerador pelo MDC
        self.__den = self.__den // divComum  # Divide o denominador pelo MDC   

    def __add__(self, outraFrac):
        # Método para somar frações
        novoNum = self.__num * outraFrac.den + self.__den * outraFrac.num  # Numerador da soma
        novoDen = self.__den * outraFrac.den  # Denominador da soma
        divComum = mdc(novoNum, novoDen)  # Calcula o MDC do resultado
        resultado = Fracao(novoNum // divComum, novoDen // divComum)  # Cria uma nova fração simplificada
        
        # Verifica se o resultado é uma fração imprópria
        if resultado.num >= resultado.den:
            parteInteira = resultado.num // resultado.den  # Parte inteira da fração
            novoNumFracionario = resultado.num % resultado.den  # Numerador da fração resultante
            # Se não há parte fracionária, retorna somente a parte inteira
            if novoNumFracionario == 0:
                return FracaoMista(parteInteira, 0, resultado.den)
            else:
                return FracaoMista(parteInteira, novoNumFracionario, resultado.den)
        else:
            return resultado  # Retorna a fração comum simplificada


class FracaoMista:
    def __init__(self, parteInteira, num, den):
        # Inicializa a fração mista com parte inteira, numerador e denominador
        self.parteInteira = parteInteira
        self.fracao = Fracao(num, den)  # Cria um objeto da classe Fracao

    def __str__(self):
        # Representação em string da fração mista
        if self.fracao.num == 0:
            return str(self.parteInteira)  # Se a fração for 0, retorna apenas a parte inteira
        return f"{self.parteInteira} {self.fracao}"  # Retorna parte inteira e fração

    def to_improper(self):
        # Converte fração mista para fração imprópria
        novo_num = self.parteInteira * self.fracao.den + self.fracao.num  # Calcula o numerador
        return Fracao(novo_num, self.fracao.den)  # Retorna a fração imprópria

    def __add__(self, outra):
        # Método para somar frações mistas e frações comuns
        if isinstance(outra, FracaoMista):
            frac1 = self.to_improper()  # Converte a fração mista para imprópria
            frac2 = outra.to_improper()  # Converte a outra fração mista para imprópria
        elif isinstance(outra, Fracao):
            frac1 = self.to_improper()  # Converte a fração mista para imprópria
            frac2 = outra  # A outra fração já está na forma de Fracao
        else:
            raise TypeError("A soma só pode ser feita entre Fracao e FracaoMista")  # Erro se o tipo for inválido
        
        # Usa o método de soma da classe Fracao
        return frac1 + frac2


if __name__ == "__main__":
    # Testando a soma de frações comuns
    frac1 = Fracao(1, 4)  # Cria a fração 1/4
    frac2 = Fracao(1, 6)  # Cria a fração 1/6
    frac3 = frac1 + frac2  # Soma as frações
    print(frac3)  # Resultado esperado: fração comum

    # Testando a soma de frações mistas
    fracMista1 = FracaoMista(3, 1, 2)  # Cria a fração mista 3 1/2
    fracMista2 = FracaoMista(4, 2, 3)  # Cria a fração mista 4 2/3
    fracMista3 = fracMista1 + fracMista2  # Soma as frações mistas
    print(fracMista3)  # Resultado esperado: 8 1/6

    # Testando a soma de uma fração mista com uma fração comum
    fracMista1 = FracaoMista(2, 3, 4)  # Cria a fração mista 2 3/4
    frac1 = Fracao(1, 3)  # Cria a fração 1/3
    resultado = fracMista1 + frac1  # Soma fração mista e fração comum
    print(resultado)  # Imprime o resultado
