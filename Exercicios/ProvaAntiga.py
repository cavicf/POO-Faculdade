#Prova Antiga de POO - Academico

from abc import ABC, abstractmethod
#CLASSE PESSOA ABSTRATA
class Pessoa(ABC):
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

        @property
        def nome(self):
            return self._nome
        
        @property
        def email(self):
            return self._email
        
############################################################################
#CLASSE PROFESSOR FILHA
class Professor(Pessoa):
    def __init__(self, nome, email, titulacao):
        super().__init__(nome, email)
        self._titulacao = titulacao

        @property
        def titulacao(self):
            return self._titulacao
    
############################################################################
#CLASSE ALUNO FILHA
class Aluno(Pessoa):
    def __init__(self, nome, email, nroMatricula, curso):
        super().__init__(nome, email)
        self._nroMatricula = nroMatricula
        self._curso = curso

        @property
        def nroMatricula(self):
            return nroMatricula
        
        @property
        def curso(self):
            return self._curso
        
############################################################################
#CLASSE DISCIPLINA
class Disciplina:
    def __init__(self, nome, cargaHorária):
        self._nome = nome
        self._cargaHorária = cargaHorária

    @property
    def nome(self):
        return self._nome

    @property
    def cargaHoraria(self):
        return self._cargaHorária
##############################################################################
#CLASSE CURSO

class Curso:
    def __init__(self, sigla, nome):
        self._sigla = sigla
        self._nome = nome
        self._grade = []

    @property
    def sigla(self):
        return self._sigla
    
    @property
    def nome(self):
        return self._nome

    def addDiscipGrade(self, nome, cargaHoraria):
        disci = Disciplina(nome, cargaHoraria)
        self._grade.append(disci)

#############################################################################
# CLASSE TURMA
class Turma:
    def __init__(self, nome, disciplina, professor):
        self._nome = nome
        self._disciplina = disciplina
        self._professor = professor
        self._alunos = []

    @property
    def nome(self):
        return self._nome
        
    @property
    def disciplina(self):
        return self._disciplina
        
    @property
    def professor(self):
        return self._professor
        
    @property
    def alunos(self):
        return self._alunos
        
    def addAluno(self, nroMatricula, curso):
        aln = Aluno(nroMatricula, curso)
        self._alunos.append(aln)

################################################################################
qtd = 0
for i in cco.grade
    for j in turmas
        if i == j.disciplina:
            for aluno in j.alunos:
                qtd++

for tur in Turmas
    tur.professor == 'Adriana':
    print(tur.discplina)

carga = 0
for i in turmas:
    for aluno in i.alunos:
        if aluno.nome  == aluno9.nome:
            carga += i.disciplina.cargahoraria



   # Dicionário para armazenar a carga horária total por professor
carga_professores = {}

# Iterar sobre as turmas
for turma in turmas:
    professor = turma.professor
    carga_horaria = turma.disciplina.cargaHoraria

    # Se o professor já está no dicionário, somar a carga horária
    if professor.nome in carga_professores:
        carga_professores[professor.nome] += carga_horaria
    else:
        carga_professores[professor.nome] = carga_horaria

# Imprimir o nome dos professores e suas respectivas cargas horárias
for nome_professor, carga in carga_professores.items():
    print(f"Professor: {nome_professor}, Carga Horária Total: {carga}")
