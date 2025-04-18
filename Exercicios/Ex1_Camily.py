# Camily Victal Finamor - 2024001197
from abc import ABC, abstractmethod

# Classe base abstrata para as empregadas domésticas
class EmpDomestica(ABC):
    # Construtor que inicializa nome e telefone
    def __init__(self, nome, telefone):
        self._nome = nome  # Atributo privado para armazenar o nome da empregada
        self._telefone = telefone  # Atributo privado para armazenar o telefone da empregada

    # Propriedade para obter o nome da empregada
    @property
    def nome(self):
        return self._nome
    
    # Propriedade para obter o telefone da empregada
    @property
    def telefone(self):
        return self._telefone
    
    # Método abstrato para obter o salário, que deve ser implementado nas subclasses
    @abstractmethod
    def getSalario(self):
        pass

#########################################################################

# Classe concreta para empregadas horistas, derivada de EmpDomestica
class Horista(EmpDomestica):
    # Construtor que inicializa nome, telefone, horas trabalhadas e valor por hora
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)  # Chama o construtor da classe mãe
        self._horasTrabalhadas = horasTrabalhadas  # Atributo privado para horas trabalhadas
        self._valorPorHora = valorPorHora  # Atributo privado para valor por hora

    # Propriedade para obter as horas trabalhadas
    @property
    def horasTrabalhadas(self):
        return self._horasTrabalhadas
    
    # Propriedade para obter o valor pago por hora
    @property
    def valorPorHora(self):
        return self._valorPorHora
    
    # Implementação do método getSalario, calculando o salário da horista
    def getSalario(self):
        return self.valorPorHora * self.horasTrabalhadas  # Calcula o salário multiplicando horas trabalhadas pelo valor por hora
    
#########################################################################

# Classe concreta para diaristas, derivada de EmpDomestica
class Diarista(EmpDomestica):
    # Construtor que inicializa nome, telefone, dias trabalhados e valor por dia
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)  # Chama o construtor da classe mãe
        self._diasTrabalhados = diasTrabalhados  # Atributo privado para dias trabalhados
        self._valorPorDia = valorPorDia  # Atributo privado para valor por dia

    # Propriedade para obter os dias trabalhados
    @property
    def diasTrabalhados(self):
        return self._diasTrabalhados
    
    # Propriedade para obter o valor pago por dia
    @property
    def valorPorDia(self):
        return self._valorPorDia
    
    # Implementação do método getSalario, calculando o salário da diarista
    def getSalario(self):
        return self.diasTrabalhados * self.valorPorDia  # Calcula o salário multiplicando dias trabalhados pelo valor por dia
    
#########################################################################

# Classe concreta para mensalistas, derivada de EmpDomestica
class Mensalista(EmpDomestica):
    # Construtor que inicializa nome, telefone e valor mensal
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)  # Chama o construtor da classe mãe
        self._valorMensal = valorMensal  # Atributo privado para valor mensal

    # Propriedade para obter o valor mensal
    @property
    def valorMensal(self):
        return self._valorMensal
    
    # Implementação do método getSalario, retornando o valor fixo mensal
    def getSalario(self):
        return self.valorMensal  # Retorna o valor mensal fixo
    
#########################################################################

# Bloco principal para criar instâncias e realizar os cálculos
if __name__ == "__main__":
    # Inicializando uma instância da classe Horista
    empregada1 = Horista('Mariana', '12312-1231', 160, 12)  # 160 horas trabalhadas, R$12/hora
    
    # Inicializando uma instância da classe Diarista
    empregada2 = Diarista('Joana', '45645-4564', 20, 65)  # 20 dias trabalhados, R$65/dia
    
    # Inicializando uma instância da classe Mensalista
    empregada3 = Mensalista('Ana', '78978-7897', 1200)  # R$1200 fixos por mês
    
    # Criando uma lista com as empregadas
    empregadas = [empregada1, empregada2, empregada3]

    # Loop para imprimir o nome e o salário mensal de cada empregada
    for empregada in empregadas:
        print(f'Nome: {empregada.nome} - Salário: R${empregada.getSalario()}')

    # Usando a função min para encontrar a empregada com o menor salário
    menor_valor = min(empregadas, key=lambda empregada: empregada.getSalario())
    
    # Imprimindo a empregada mais barata para a república, com seu nome e telefone
    print(f'A opção mais barata é a {menor_valor.nome}, seu telefone é {menor_valor.telefone}')
