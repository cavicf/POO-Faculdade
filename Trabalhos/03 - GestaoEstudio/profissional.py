#Camily Victal Finamor - 2024001197
import tkinter as tk 
from tkinter import messagebox
#MODEL----------------------------------------------------------------------------
class Profissional:
    def __init__(self, cpf, nome, email, valorPilates, valorFuncional):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__valorPilates = float(valorPilates)
        self.__valorFuncional = float(valorFuncional)

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
    def valorPilates(self):
        return self.__valorPilates
    
    @property
    def valorFuncional(self):
        return self.__valorFuncional

#VIEWCADASTRAR-------------------------------------------------------------------
class ViewCadastrar(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('Cadastrar Professor:')

        self.framecpf = tk.Frame(self)
        self.framenome = tk.Frame(self)
        self.frameemail = tk.Frame(self)
        self.framepilates = tk.Frame(self)
        self.framefuncional = tk.Frame(self)
        self.framebotao = tk.Frame(self)
        self.framecpf.pack()
        self.framenome.pack()
        self.frameemail.pack()
        self.framepilates.pack()
        self.framefuncional.pack()
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

        self.labelpilates = tk.Label(self.framepilates, text='Valor Pilates:')
        self.labelpilates.pack(side='left')
        self.inputpilates = tk.Entry(self.framepilates, width=20)
        self.inputpilates.pack(side='left',padx=5)

        self.labelfuncional = tk.Label(self.framefuncional, text='Valor Funcional:')
        self.labelfuncional.pack(side='left')
        self.inputfuncional = tk.Entry(self.framefuncional, width=20)
        self.inputfuncional.pack(side='left',padx=5)

        self.botaoCadastrar = tk.Button(self.framebotao, text='Cadastrar', command=self.controlador.salvarProfissional)
        self.botaoCadastrar.pack(side='left',pady=5, padx=5)
        self.botaoClear = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparCampos)
        self.botaoClear.pack(side='left', pady=5)

#VIEWLISTAR----------------------------------------------------------------------
class ViewListar:
    def __init__(self, mensagem):
        messagebox.showinfo('Professores Cadastrados:', mensagem)

#VIEWFATURAMENTO----------------------------------------------------------------------
class ViewFaturamento(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry( '300x250')
        self.title('Faturamento:')

        self.frameconsulta = tk.Frame(self)
        self.frameconsulta.pack()
        self.labelconsulta = tk.Label(self.frameconsulta, text='Digite o cpf:')
        self.labelconsulta.pack(side='left')
        self.inputconsulta = tk.Entry(self.frameconsulta, width=20)
        self.inputconsulta.pack(side='left')
        self.framebotao = tk.Frame(self)
        self.framebotao.pack()
        self.botaoconsulta = tk.Button(self.framebotao, text='Consultar', command= self.controlador.faturamentoProfessor)
        self.botaoconsulta.pack(side='left')
        self.botaolimpa = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparCampoConsulta)
        self.botaolimpa.pack(side='left')      

#CONTROLADORPROFISSIONAL--------------------------------------------------------
class ControladorProfissional:
    def __init__(self, controladorPrincipal):
        self.listaProfissionais = []
        self.controladorPrincipal = controladorPrincipal

    def cadastrarProfissional(self):
        self.ViewCadastrar = ViewCadastrar(self)
        

    def listarProfissional(self):
        mensagem = ''
        for prof in self.listaProfissionais:
            mensagem += f'Professor: {prof.nome}\nCPF: {prof.cpf}\nEmail: {prof.email}\n Valor Pilates: {prof.valorPilates}\nValor Funcional: {prof.valorFuncional}\n'
            mensagem+='-------------------------------------------------------------------\n'
        self.ViewListar = ViewListar(mensagem)

    def faturamentoProfissional(self):
        self.ViewFaturamento = ViewFaturamento(self)
        

    def salvarProfissional(self):
        cpf = self.ViewCadastrar.inputcpf.get()
        nome = self.ViewCadastrar.inputnome.get()
        email = self.ViewCadastrar.inputemail.get()
        valorPilates = self.ViewCadastrar.inputpilates.get()
        valorFuncional = self.ViewCadastrar.inputfuncional.get()
        if not cpf or not nome or not email or not valorPilates or not valorFuncional:
            messagebox.showerror('ERRO:', 'Todos os campos devem ser preenchidos!')
            return
        if len(cpf) != 14:
            messagebox.showerror('ERRO:', 'CPF deve estar no formato ___.___.___-__')
            return
        for profissional in self.listaProfissionais:
            if profissional.nome == nome or profissional.cpf == cpf:
                messagebox.showerror('ERRO:', 'Professor ja cadastrado!')
                return
        professor = Profissional(cpf, nome, email, valorPilates, valorFuncional)
        self.listaProfissionais.append(professor)
        messagebox.showinfo('SUCESSO:', 'Professor cadastrado com sucesso!')
        self.ViewCadastrar.destroy()

    def getlistaprof(self):
        listaprof = []
        for prof in self.listaProfissionais:
            listaprof.append(prof.nome)
        return listaprof
    
    def getlista(self):
        listaprofgeral = []
        for prof in self.listaProfissionais:
            listaprofgeral.append(prof)
        return listaprofgeral
    
    def getprof(self, cpf):
        for prof in self.listaProfissionais:
            if prof.cpf == cpf:
                return prof

    
    def faturamentoProfessor(self):
        cpf = self.ViewFaturamento.inputconsulta.get()
        if not cpf:
            messagebox.showerror('ERRO:', 'Todos os campos devem ser preenchidos!')
            return
        if len(cpf) != 14:
            messagebox.showerror('ERRO:', 'CPF deve estar no formato ___.___.___-__')
            return
        prof = self.getprof(cpf)
        if not prof:
            messagebox.showerror('ERRO:', 'professor não cadastrado!')
            return
        listaaluno = self.controladorPrincipal.ControladorAluno.getlistaAluno()
        faturamentoPilates = 0
        faturamentoFuncional = 0
        mensalidadeAluno = None
        for aluno in listaaluno:
            if aluno.professor == prof.nome:
                if aluno.tipoAula == 'Pilates':
                    custoProf = prof.valorPilates
                    if aluno.nmrAulas == '2 aulas':
                        mensalidadeAluno = custoProf
                    elif aluno.nmrAulas == '3 aulas':
                        mensalidadeAluno = custoProf * 1.4
                    else:
                        mensalidadeAluno = custoProf * 1.8
                    faturamentoPilates += mensalidadeAluno
                else:
                    custoProf = prof.valorFuncional
                    if aluno.nmrAulas == '2 aulas':
                        mensalidadeAluno = custoProf
                    elif aluno.nmrAulas == '3 aulas':
                        mensalidadeAluno = custoProf * 1.4
                    else:
                        mensalidadeAluno = custoProf * 1.8
                    faturamentoFuncional += mensalidadeAluno
        mensagem = f'Faturamento de: {prof.nome}\nPilates: R${faturamentoPilates}\nFuncional: R${faturamentoFuncional}'
        messagebox.showinfo('FATURAMENTO:', mensagem)
        self.ViewFaturamento.destroy()    

    def limparCampos(self):
        self.ViewCadastrar.inputcpf.delete(0, tk.END)
        self.ViewCadastrar.inputnome.delete(0, tk.END)
        self.ViewCadastrar.inputemail.delete(0, tk.END)
        self.ViewCadastrar.inputpilates.delete(0, tk.END)
        self.ViewCadastrar.inputfuncional.delete(0, tk.END)

    def limparCampoConsulta(self):
        self.ViewFaturamento.inputconsulta.delete(0, tk.END)