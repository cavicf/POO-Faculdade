from datetime import datetime


class ProfSaude:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
###############################################################
class Medico(ProfSaude):
    def __init__(self, nome, cpf, crm, especialidade):
        super().__init__(nome, cpf)
        self._crm = crm
        self._especialidade = especialidade

    @property
    def crm(self):
        return self._crm
    
    @property
    def especialidade(self):
        return self._especialidade
    
#########################################################################
class Instrumentador(ProfSaude):
    def __init__(self, nome, cpf, coren):
        super().__init__(nome, cpf)
        self._coren = coren

    @property
    def coren(self):
        return self._coren
    
#########################################################################
class TipoCirurgia:
    def __init__(self, descricao, valorCirurgiao, valorAnest, valorInstrum):
        self._descricao = descricao
        self._valorCirurgiao = valorCirurgiao
        self._valorAnest = valorAnest
        self._valorInstrum = valorInstrum

    @property
    def descricao(self):
        return self._descricao

    @property
    def valorCirurgiao(self):
        return self._valorCirurgiao 
    
    @property
    def valorAnest(self):
        return self._valorAnest
    
    @property
    def valorInstrum(self):
        return self._valorInstrum
#############################################################################
class Paciente:
    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo
##############################################################################
class Cirurgia:
    def __init__(self, data, paciente, tipoCirurgia):
        self._data = data
        self._paciente = paciente
        self._tipoCirurgia = tipoCirurgia
        self._equipe = []

    @property
    def data(self):
        return self._data

    @property
    def paciente(self):
        return self._paciente

    @property
    def tipoCirurgia(self):
        return self._tipoCirurgia

    @property
    def equipe(self):
        return self._equipe
    
    def adicionaProf(self, prof):
        self._equipe.append(prof)

    def equipeValida(self):
        cirurgiao = 0
        instrumentador = 0
        anestesista = 0
        for prof in self._equipe:
            if isinstance(prof, Medico) and prof.especialidade == 'Cirurgião':
                cirurgiao += 1
            if isinstance(prof, Medico) and prof.especialidade == 'Anestesista':
                anestesista += 1
            if isinstance(prof, Instrumentador):
                instrumentador += 1
        if cirurgiao > 0 and instrumentador > 0 and anestesista > 0:
            return True
        else:
            return False
        
    def calculaCustoCir(self):
        custocirurgia = 0
        if self.equipeValida() == False:
            return 0
        for prof in self._equipe:
            if isinstance(prof, Medico) and prof.especialidade == 'Cirurgião':
                custocirurgia += self._tipoCirurgia.valorCirurgiao
            if isinstance(prof, Medico) and prof.especialidade == 'Anestesista':
                custocirurgia += self._tipoCirurgia.valorAnest
            if isinstance(prof, Instrumentador):
                custocirurgia += self._tipoCirurgia.valorInstrum
        if self._paciente.tipo == 'Convênio':
            custocirurgia = custocirurgia - (custocirurgia * 0.20)
            return custocirurgia
        else:
            return custocirurgia


#################################################################################


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
    #Saída esperada: 'O valor da cirurgia da paciente Márcia Reis é 12200'




