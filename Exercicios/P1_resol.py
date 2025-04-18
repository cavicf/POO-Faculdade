from abc import ABC, abstractmethod
from datetime import datetime
from abc import ABC

class Paciente:
    def __init__(self, nome, tipo):
        self.__nome = nome
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

class TipoCirurgia:
    def __init__(self, desc, valorCir, valorAnest, valorInst):
        self.__desc = desc
        self.__valorCir = valorCir
        self.__valorAnest = valorAnest
        self.__valorInst = valorInst

    @property
    def desc(self):
        return self.__desc
    
    @property
    def valorCir(self):
        return self.__valorCir
    
    @property
    def valorAnest(self):
        return self.__valorAnest

    @property
    def valorInst(self):
        return self.__valorInst
    
class ProfSaude(ABC):
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
 
class Medico(ProfSaude):
    def __init__(self, nome, cpf, crm, especialidade):
        super().__init__(nome, cpf)
        self.__crm = crm
        self.__especialidade = especialidade

    @property
    def crm(self):
        return self.__crm
    
    @property
    def especialidade(self):
        return self.__especialidade

    
class Instrumentador(ProfSaude):
    def __init__(self, nome, cpf, coren):
        super().__init__(nome, cpf)
        self.__coren = coren

    @property
    def coren(self):
        return self.__coren   

class Cirurgia:
    def __init__(self, data, paciente, tipoCir):
        self.__data = data
        self.__paciente = paciente
        self.__tipoCir = tipoCir

        self.__equipe = []

    @property
    def data(self):
        return self.__data

    @property
    def paciente(self):
        return self.__paciente
    
    @property
    def tipoCir(self):
        return self.__tipoCir
    
    @property
    def equipe(self):
        return self.__equipe

    def adicionaProf(self, prof):
        self.__equipe.append(prof)

    def equipeValida(self):
        nroCir = 0
        nroAnest = 0
        nroInst = 0
        for prof in self.__equipe:
            if type(prof) is Medico:                                
                if prof.especialidade == 'Cirurgião':                    
                    nroCir += 1
                elif prof.especialidade == 'Anestesista':
                    nroAnest += 1
            if type(prof) is Instrumentador:
                nroInst += 1
        if nroCir > 0 and nroAnest > 0 and nroInst > 0:
            return True
        else:
            return False
    
    def calculaCustoCir(self):
        custo = 0
        if not self.equipeValida():
            return 0
        for prof in self.__equipe:
            if type(prof) is Medico:
                if prof.especialidade == 'Cirurgião':
                    custo += self.__tipoCir.valorCir
                elif prof.especialidade == 'Anestesista':
                    custo += self.__tipoCir.valorAnest
            if type(prof) is Instrumentador:
                custo += self.__tipoCir.valorInst
        if self.__paciente.tipo == 'Convênio':
            custo = custo * 0.8
        return custo

if __name__ == "__main__":
    tipo1 = TipoCirurgia('Oncológica', 8000, 2000, 1000)
    tipo2 = TipoCirurgia('Cardíaca', 9000, 2000, 1200)
    tipo3 = TipoCirurgia('Ortopédica', 7000, 2000, 900)
    pac1 = Paciente('Luiz Silva', 'Particular')
    pac2 = Paciente('José Cruz', 'Convênio')
    pac3 = Paciente('Márcia Reis', 'Particular')
    medCir1 = Medico('Luis Lima', '1234', 'crm1234', 'Cirurgião')
    medCir2 = Medico('Marcos Lopes', '9876', 'crm9876', 'Cirurgião')
    medAnest1 = Medico('Marisa Lins', '4321', 'crm4321', 'Anestesista')
    inst1 = Instrumentador('Ana Souza', '4567', 'coren4567')
    inst2 = Instrumentador('Joel Santos', '7890', 'coren7890')
    cirurgia1 = Cirurgia(datetime(2023, 10, 30), pac1, tipo1)
    cirurgia1.adicionaProf(medCir1)
    cirurgia1.adicionaProf(inst1)
    custo1 = cirurgia1.calculaCustoCir()
    if custo1 == 0:
        print('Equipe não está completa.')
    else:
        print('O valor da cirurgia do paciente {} é {}'.format(pac1.nome, custo1))
    #Saída esperada: 'Equipe não está completa'
    print()    

    cirurgia2 = Cirurgia(datetime(2023, 11, 10), pac2, tipo1)
    cirurgia2.adicionaProf(medCir1)
    cirurgia2.adicionaProf(medAnest1)
    cirurgia2.adicionaProf(inst1)
    custo2 = cirurgia2.calculaCustoCir()
    if custo2 == 0:
        print('Equipe não está completa.')
    else:
        print('O valor da cirurgia do paciente {} é {}'.format(pac2.nome, custo2))
    #Saída esperada: 'O valor da cirurgia do paciente José Cruz é 8800.0'
    print()

    cirurgia3 = Cirurgia(datetime(2023, 11, 20), pac3, tipo2)
    cirurgia3.adicionaProf(medCir1)
    cirurgia3.adicionaProf(medAnest1)
    cirurgia3.adicionaProf(inst2)
    custo3 = cirurgia3.calculaCustoCir()
    if custo3 == 0:
        print('Equipe não está completa.')
    else:
        print('O valor da cirurgia da paciente {} é {}'.format(pac3.nome, custo3))




