#Camily Victal Finamor - 2024001197
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
#MODEL----------------------------------------------------------------------------
class Aluno:
    def __init__(self, cpf, nome, email, tipoAula, professor, nmrAulas):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__tipoAula = tipoAula
        self.__professor = professor
        self.__nmrAulas = nmrAulas

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def tipoAula(self):
        return self.__tipoAula
    
    @property
    def professor(self):
        return self.__professor
    
    @property
    def nmrAulas(self):
        return self.__nmrAulas

#VIEWCADASTRAR-------------------------------------------------------------------
class ViewCadastrar(tk.Toplevel):
    def __init__(self, controlador, listaProfessor):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('Cadastrar Aluno')

        self.framecpf = tk.Frame(self)
        self.framenome = tk.Frame(self)
        self.frameemail = tk.Frame(self)
        self.frametpaula = tk.Frame(self)
        self.frameprof = tk.Frame(self)
        self.framenmraula = tk.Frame(self)
        self.framebotao = tk.Frame(self)
        self.framecpf.pack()
        self.framenome.pack()
        self.frameemail.pack()
        self.frametpaula.pack()
        self.frameprof.pack()
        self.framenmraula.pack()
        self.framebotao.pack()

        self.labelcpf = tk.Label(self.framecpf, text='CPF:')
        self.labelcpf.pack(side='left')
        self.inputcpf = tk.Entry(self.framecpf, width=20)
        self.inputcpf.pack(side='left', padx=5)

        self.labelnome = tk.Label(self.framenome, text='Nome:')
        self.labelnome.pack(side='left')
        self.inputnome = tk.Entry(self.framenome, width=20)
        self.inputnome.pack(side='left',padx=5)

        self.labelemail = tk.Label(self.frameemail, text='Email:')
        self.labelemail.pack(side='left')
        self.inputemail = tk.Entry(self.frameemail, width=20)
        self.inputemail.pack(side='left',padx=5)

        self.labeltipo = tk.Label(self.frametpaula, text='Selecione o tipo:')
        self.labeltipo.pack(side='left')
        self.escolhatipo = tk.StringVar()
        self.combotipo = Combobox(self.frametpaula, width=15, textvariable=self.escolhatipo)
        self.combotipo.config(values=('--Selecione--','Pilates', 'Funcional'))
        self.combotipo.current(0)
        self.combotipo.pack(side='left')

        self.labelprof = tk.Label(self.frameprof, text='Selecione o prof:')
        self.labelprof.pack(side='left')
        self.escolhaprof = tk.StringVar()
        self.comboprof = Combobox(self.frameprof, width=15, textvariable=self.escolhaprof)
        self.comboprof.config(values=['--Selecione--'] + listaProfessor)
        self.comboprof.current(0)
        self.comboprof.pack(side='left')

        self.labelnmr = tk.Label(self.framenmraula, text='Número de aulas:')
        self.labelnmr.pack(side='left')
        self.escolhanmr = tk.StringVar()
        self.combonmr = Combobox(self.framenmraula, width=15, textvariable=self.escolhanmr)
        self.combonmr.config(values=('--Selecione--','2 aulas', '3 aulas', '4 aulas'))
        self.combonmr.current(0)
        self.combonmr.pack(side='left')

        self.botaoCadastrar = tk.Button(self.framebotao, text='Cadastrar', command=self.controlador.salvarAluno)
        self.botaoCadastrar.pack(side='left',pady=5, padx=5)
        self.botaoClear = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparCampos)
        self.botaoClear.pack(side='left', pady=5)

#VIEWCCONSULTAR----------------------------------------------------------------------
class ViewConsultar(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('Consultar Aluno')

        self.frameconsulta = tk.Frame(self)
        self.frameconsulta.pack()
        self.labelconsulta = tk.Label(self.frameconsulta, text='Digite o cpf:')
        self.labelconsulta.pack(side='left')
        self.inputconsulta = tk.Entry(self.frameconsulta, width=20)
        self.inputconsulta.pack(side='left')
        self.framebotao = tk.Frame(self)
        self.framebotao.pack()
        self.botaoconsulta = tk.Button(self.framebotao, text='Consultar', command= self.controlador.procurarAluno)
        self.botaoconsulta.pack(side='left')
        self.botaolimpa = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparCampoConsulta)
        self.botaolimpa.pack(side='left')

#VIEWMOSTAR---------------------------------------------------------------------
class ViewMostrar:
    def __init__(self, mensagem):
        messagebox.showinfo('Aluno encontrado:', mensagem)

#CONTROLADORPROFISSIONAL--------------------------------------------------------
class ControladorAluno:
    def __init__(self, controladorPrincipal):
        self.controladorPrincipal = controladorPrincipal
        self.listaAlunos = []

    def cadastrarAluno(self):
        listaprofessor = self.controladorPrincipal.ControladorProfissional.getlistaprof()
        self.ViewCadastrar = ViewCadastrar(self, listaprofessor)
    
    def consultarAluno(self):
        self.ViewConsultar = ViewConsultar(self)

    def salvarAluno(self):
        cpf = self.ViewCadastrar.inputcpf.get()
        nome = self.ViewCadastrar.inputnome.get()
        email = self.ViewCadastrar.inputemail.get()
        tipoAula = self.ViewCadastrar.escolhatipo.get()
        professor = self.ViewCadastrar.escolhaprof.get()
        nmraulas = self.ViewCadastrar.escolhanmr.get()
        if not cpf or not nome or not email or not tipoAula or not professor or not nmraulas:
            messagebox.showerror('ERRO:', 'Todos os campos devem ser preenchidos!')
            return
        if len(cpf) != 14:
            messagebox.showerror('ERRO:', 'CPF deve estar no formato ___.___.___-__')
            return
        if tipoAula == '--Selecione--' or professor == '--Selecione--' or nmraulas == '--Selecione--':
            messagebox.showerror('ERRO:', 'Todos os campos devem ser preenchidos!')
            return
        for alun in self.listaAlunos:
            if alun.nome == nome or alun.cpf == cpf:
                messagebox.showerror('ERRO:', 'O aluno ja está cadastrado!')
                return
        aluno = Aluno(cpf, nome, email, tipoAula, professor, nmraulas)
        self.listaAlunos.append(aluno)
        messagebox.showinfo('SUCESSO:', 'Aluno cadastrado com sucesso!')
        self.ViewCadastrar.destroy()

    def getAluno(self, cpf):
        for alun in self.listaAlunos:
            if alun.cpf == cpf:
                return alun
            
    def getlistaAluno(self):
        listaaluno = []
        for alun in self.listaAlunos:
            listaaluno.append(alun)
        return listaaluno

    def getcustoProf(self, professor, aluno):
        custoProf = None
        for prof in professor:
            if aluno.professor == prof.nome:
                if aluno.tipoAula == 'Pilates':
                    custoProf = prof.valorPilates
                else:
                    custoProf = prof.valorFuncional
        return custoProf

    def procurarAluno(self):
        cpf = self.ViewConsultar.inputconsulta.get()
        if not cpf:
            messagebox.showerror('ERRO:', 'Todos os campos devem ser preenchidos!')
            return
        aluno = self.getAluno(cpf)
        if not aluno:
            messagebox.showerror('ERRO:', 'Aluno não encontrado')
            return
        professor = self.controladorPrincipal.ControladorProfissional.getlista()
        custoProf = self.getcustoProf(professor, aluno)
        mensalidadeAluno = None
        aulas3 = custoProf * 1.4
        aulas4 = custoProf * 1.8
        if aluno.nmrAulas == '2 aulas':
            mensalidadeAluno = custoProf + (custoProf/2)
        elif aluno.nmrAulas == '3 aulas':
            mensalidadeAluno = aulas3 + (aulas3/2)
        else:
            mensalidadeAluno = aulas4 + (aulas4/2)
        mensagem = f'Aluno: {aluno.nome}\nCPF: {aluno.cpf}\nEmail: {aluno.email}\nTipo de Aula: {aluno.tipoAula}\nProfessor: {aluno.professor}\nNúmero de aulas: {aluno.nmrAulas}\nMensalidade: {mensalidadeAluno}'
        self.mostraAluno = ViewMostrar(mensagem)
        self.ViewConsultar.destroy()

    def limparCampoConsulta(self):
        self.ViewConsultar.inputconsulta.delete(0, tk.END)

    def limparCampos(self):
        self.ViewCadastrar.inputcpf.delete(0, tk.END)
        self.ViewCadastrar.inputemail.delete(0, tk.END)
        self.ViewCadastrar.inputnome.delete(0, tk.END)
        self.ViewCadastrar.combotipo.current(0)
        self.ViewCadastrar.comboprof.current(0)
        self.ViewCadastrar.combonmr.current(0)