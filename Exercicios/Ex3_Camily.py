# Camily Victal Finamor - 2024001197

from abc import ABC, abstractmethod

# Classe base abstrata que representa um funcionário
class Funcionario(ABC):
    def __init__(self, codigo, nome, cargo):
        self._codigo = codigo  # Código do funcionário
        self._nome = nome  # Nome do funcionário
        self._cargo = cargo  # Cargo do funcionário
        self._pontos = []  # Lista que armazenará os pontos (faltas e atrasos)

    # Propriedade para acessar o código do funcionário
    @property
    def codigo(self):
        return self._codigo

    # Propriedade para acessar o nome do funcionário
    @property
    def nome(self):
        return self._nome

    # Propriedade para acessar o cargo do funcionário
    @property
    def cargo(self):
        return self._cargo

    # Propriedade para acessar os pontos do funcionário
    @property
    def pontos(self):
        return self._pontos

    # Método para adicionar um ponto (faltas e atrasos) ao funcionário
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        self._pontos.append(PontoFunc(mes, ano, faltas, atrasos))

    # Método para registrar faltas de um funcionário em um determinado mês e ano
    def lancaFaltas(self, mes, ano, nroFaltas):
        for ponto in self._pontos:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.faltas = nroFaltas  # Atualiza o número de faltas

    # Método para registrar atrasos de um funcionário em um determinado mês e ano
    def lancaAtrasos(self, mes, ano, nroAtrasos):
        for ponto in self._pontos:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.atrasos = nroAtrasos  # Atualiza o número de atrasos

    # Método para obter o ponto correspondente a um determinado mês e ano
    def getPonto(self, mes, ano):
        for ponto in self._pontos:
            if ponto.mes == mes and ponto.ano == ano:
                return ponto  # Retorna o ponto encontrado
        return PontoFunc(mes, ano, 0, 0)  # Retorna um ponto com 0 faltas e atrasos se não encontrado

    # Método abstrato que deve ser implementado pelas subclasses para calcular o salário
    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    # Método abstrato que deve ser implementado pelas subclasses para calcular o bônus
    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass

    # Método que imprime a folha de pagamento do funcionário para um determinado mês e ano
    def imprimeFolha(self, mes, ano):
        salarioLiquido = self.calculaSalario(mes, ano)  # Calcula o salário líquido
        bonus = self.calculaBonus(mes, ano)  # Calcula o bônus
        # Imprime os detalhes do funcionário
        print(f"Código: {self.codigo}\nNome: {self.nome}\nSalário Líquido: R${salarioLiquido:.2f}\nBônus: R${bonus:.2f}")

##########################################################################################

# Classe concreta que representa um professor, derivada da classe Funcionario
class Professor(Funcionario):
    def __init__(self, codigo, nome, cargo, salarioHora, nroAulas):
        super().__init__(codigo, nome, cargo)  # Chama o construtor da classe mãe
        self._salarioHora = salarioHora  # Atributo privado para armazenar o salário por hora
        self._nroAulas = nroAulas  # Atributo privado para armazenar o número de aulas

    # Propriedade para acessar o salário por hora
    @property
    def salarioHora(self):
        return self._salarioHora

    # Propriedade para acessar o número de aulas
    @property
    def nroAulas(self):
        return self._nroAulas

    # Implementação do método para calcular o salário do professor
    def calculaSalario(self, mes, ano):
        ponto = self.getPonto(mes, ano)  # Obtém os pontos do mês e ano
        salarioBruto = self.salarioHora * self.nroAulas  # Calcula o salário bruto
        descontoFaltas = self.salarioHora * ponto.faltas  # Desconto das faltas
        salarioLiquido = salarioBruto - descontoFaltas  # Salário líquido
        return salarioLiquido

    # Implementação do método para calcular o bônus do professor
    def calculaBonus(self, mes, ano):
        ponto = self.getPonto(mes, ano)  # Obtém os pontos do mês e ano
        salarioLiquido = self.calculaSalario(mes, ano)  # Calcula o salário líquido
        bonus = 0.1 * salarioLiquido  # Bônus padrão de 10%
        bonus -= 0.01 * salarioLiquido * ponto.atrasos  # Desconto de 1% do bônus por atraso
        if bonus < 0:
            bonus = 0  # Garante que o bônus não fique negativo
        return bonus

##########################################################################################

# Classe concreta que representa um técnico administrativo, derivada da classe Funcionario
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, cargo, salarioMensal):
        super().__init__(codigo, nome, cargo)  # Chama o construtor da classe mãe
        self._salarioMensal = salarioMensal  # Atributo privado para armazenar o salário mensal

    # Propriedade para acessar o salário mensal
    @property
    def salarioMensal(self):
        return self._salarioMensal

    # Implementação do método para calcular o salário do técnico administrativo
    def calculaSalario(self, mes, ano):
        ponto = self.getPonto(mes, ano)  # Obtém os pontos do mês e ano
        descontoFaltas = (self.salarioMensal / 30) * ponto.faltas  # Desconto proporcional por faltas
        salarioLiquido = self.salarioMensal - descontoFaltas  # Salário líquido
        return salarioLiquido

    # Implementação do método para calcular o bônus do técnico administrativo
    def calculaBonus(self, mes, ano):
        ponto = self.getPonto(mes, ano)  # Obtém os pontos do mês e ano
        salarioLiquido = self.calculaSalario(mes, ano)  # Calcula o salário líquido
        bonus = 0.08 * salarioLiquido  # Bônus padrão de 8%
        bonus -= 0.01 * salarioLiquido * ponto.atrasos  # Desconto de 1% do bônus por atraso
        if bonus < 0:
            bonus = 0  # Garante que o bônus não fique negativo
        return bonus

##########################################################################################

# Classe que representa os pontos de frequência de um funcionário
class PontoFunc:
    def __init__(self, mes, ano, faltas, atrasos):
        self._mes = mes  # Mês do ponto
        self._ano = ano  # Ano do ponto
        self._faltas = faltas  # Número de faltas
        self._atrasos = atrasos  # Número de atrasos

    # Propriedade para acessar o mês do ponto
    @property
    def mes(self):
        return self._mes

    # Propriedade para acessar o ano do ponto
    @property
    def ano(self):
        return self._ano

    # Propriedade para acessar o número de faltas
    @property
    def faltas(self):
        return self._faltas

    # Setter para modificar o número de faltas
    @faltas.setter
    def faltas(self, value):
        self._faltas = value

    # Propriedade para acessar o número de atrasos
    @property
    def atrasos(self):
        return self._atrasos

    # Setter para modificar o número de atrasos
    @atrasos.setter
    def atrasos(self, value):
        self._atrasos = value

##########################################################################################

# Bloco principal para criar instâncias de funcionários e calcular suas folhas de pagamento
if __name__ == "__main__":
    funcionarios = []  # Lista para armazenar os funcionários
    # Criação de um professor com dados fictícios
    prof = Professor(1, "João", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)  # Adiciona ponto sem faltas ou atrasos
    prof.lancaFaltas(4, 2021, 2)  # Lança 2 faltas para abril de 2021
    prof.lancaAtrasos(4, 2021, 3)  # Lança 3 atrasos para abril de 2021
    funcionarios.append(prof)  # Adiciona o professor à lista de funcionários

    # Criação de um técnico administrativo com dados fictícios
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)  # Adiciona ponto sem faltas ou atrasos
    tec.lancaFaltas(4, 2021, 3)  # Lança 3 faltas para abril de 2021
    tec.lancaAtrasos(4, 2021, 4)  # Lança 4 atrasos para abril de 2021
    funcionarios.append(tec)  # Adiciona o técnico à lista de funcionários

    # Imprime a folha de pagamento para cada funcionário
    for func in funcionarios:
        func.imprimeFolha(4, 2021)  # Imprime a folha de pagamento para abril de 2021
        print()  # Linha em branco para separar a impressão
