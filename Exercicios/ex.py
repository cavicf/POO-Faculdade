from abc import ABC, abstractmethod

# Importa as classes ABC e abstractmethod do módulo abc para definir uma classe abstrata.

# classe das transações
class Transacao():
    def __init__(self, valor, desc):
        # Método construtor da classe Transacao, inicializando valor e descrição.
        self._valor = valor
        self._desc = desc
    
    @property
    def valor(self):
        # Getter para o atributo valor, permitindo seu acesso de forma controlada.
        return self._valor
    
    @property
    def desc(self):
        # Getter para o atributo desc, permitindo seu acesso de forma controlada.
        return self._desc

#########################################################################

# classe mãe abstrata
class Conta(ABC):
    # Define uma classe abstrata Conta que herda de ABC.
    def __init__(self, nmr_conta, nome, saldo):
        # Construtor inicializando número da conta, nome do titular e saldo.
        self._nmr_conta = nmr_conta
        self._nome = nome
        self._saldo = saldo
        self._listaTrans = []
        # Inicializa uma lista vazia para armazenar as transações realizadas.

    @property
    def nmr_conta(self):
        # Getter para o número da conta.
        return self._nmr_conta
        
    @property
    def nome(self):
        # Getter para o nome do titular da conta.
        return self._nome
        
    @property
    def saldo(self):
        # Getter para o saldo da conta.
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        # Setter para alterar o saldo da conta.
        self._saldo = valor

    @property
    def listaTrans(self):
        # Getter para obter a lista de transações.
        return self._listaTrans
    
    def deposito(self, valor, desc):
        # Método para realizar um depósito, adicionando uma transação à lista e aumentando o saldo.
        self._listaTrans.append(Transacao(valor, desc))
        self._saldo += valor

    def saque(self, valor, desc):
        # Método para realizar um saque. Valida se o valor é positivo e se o saldo é suficiente.
        if valor > 0:
            return False
        if self._saldo + valor < 0:
            return False
        self._listaTrans.append(Transacao(valor, desc))
        self._saldo += valor
        return True

    @abstractmethod
    def imprimirExtrato(self):
        # Método abstrato que deve ser implementado pelas subclasses para imprimir o extrato.
        pass 

#######################################################################

# classe da conta corrente
class Corrente(Conta):
    def __init__(self, nmr_conta, nome, saldo, mensalidade):
        # Construtor da classe Corrente. Inicializa a conta e adiciona a mensalidade.
        super().__init__(nmr_conta, nome, saldo)
        self._mensalidade = mensalidade
    
    @property
    def mensalidade(self):
        # Getter para a mensalidade.
        return self._mensalidade
    
    def imprimirExtrato(self):
        # Método para imprimir o extrato da conta corrente, incluindo informações sobre a mensalidade.
        print(f'Nro Conta: {self.nmr_conta}')
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')
        print(f'Valor da mensalidade descontado: {self._mensalidade}')
        print(f'saldo com desconto: {self.saldo - self._mensalidade}')

########################################################################

# classe Conta Limite
class ContaLimite(Conta):
    def __init__(self, nmr_conta, nome, saldo, limite):
        # Construtor da classe ContaLimite. Inicializa a conta e define o limite.
        super().__init__(nmr_conta, nome, saldo)
        self._limite = limite
    
    @property
    def limite(self):
        # Getter para o limite.
        return self._limite
    
    def saque(self, valor, desc):
        # Método para realizar saque. Verifica se o valor e o saldo com o limite permitem o saque.
        if valor > 0:
            return False
        if self.saldo + self._limite + valor < 0:
            return False
        self.listaTrans.append(Transacao(valor, desc))
        self._saldo += valor
        return True
    
    def imprimirExtrato(self):
        # Método para imprimir o extrato da conta com limite, exibindo saldo e limite.
        print(f'Nro Conta: {self.nmr_conta}')
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')
        print(f'Saldo + limite: {self.limite + self.saldo}')

###########################################################################

# classe poupança
class Poupanca(Conta):
    def __init__(self, nmr_conta, nome, saldo, diaAnv):
        # Construtor da classe Poupanca. Inicializa a conta e define o dia de aniversário.
        super().__init__(nmr_conta, nome, saldo)
        self._diaAnv = diaAnv
    
    @property
    def diaAnv(self):
        # Getter para o dia de aniversário da poupança.
        return self._diaAnv
    
    def imprimirExtrato(self):
        # Método para imprimir o extrato da conta poupança, exibindo o saldo e o dia de aniversário.
        print(f'Nro Conta: {self.nmr_conta}')
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')
        print(f'Dia do aniversário: {self._diaAnv}')

###########################################################################
if __name__ == "__main__":
    # Bloco de código principal que cria objetos de diferentes tipos de conta e realiza operações.
    contas = []
    cl = ContaLimite(1111, 'Ana Souza', 0, 1000)
    # Cria uma conta com limite para 'Ana Souza' com saldo 0 e limite de 1000.
    
    cl.deposito(1500, 'crédito salário')
    # Realiza um depósito de 1500 na conta.
    
    if cl.saque(-1200, 'pagamento boleto'):
        # Tenta realizar um saque de 1200.
        print(f'saque de R$1200,00 na conta {cl.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$1200,00 na conta {cl.nmr_conta}')

    if cl.saque(-500, 'PIX'):
        # Tenta realizar um saque de 500.
        print(f'saque de R$500,00 na conta {cl.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$500,00 na conta {cl.nmr_conta}')

    cc = Corrente(22222, 'Pedro José', 9000, 200)
    # Cria uma conta corrente para 'Pedro José' com saldo inicial de 9000 e mensalidade de 200.
    
    cc.deposito(10000, 'salário')
    # Realiza um depósito de 10000.
    
    if cc.saque(-100, 'pagamento boleto'):
        # Tenta realizar um saque de 100.
        print(f'saque de R$100,00 na conta {cc.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$1200,00 na conta {cl.nmr_conta}')

    if cc.saque(-500, 'PIX'):
        # Tenta realizar um saque de 500.
        print(f'saque de R$500,00 na conta {cc.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$500,00 na conta {cl.nmr_conta}')

    cp = Poupanca(3333, 'Klaber da Silva', 400, '04/09')
    # Cria uma conta poupança para 'Klaber da Silva' com saldo inicial de 400 e dia de aniversário '04/09'.
    
    cp.deposito(1500, 'crédito salário')
    # Realiza um depósito de 1500.
    
    if cp.saque(-100, 'pagamento boleto'):
        # Tenta realizar um saque de 100.
        print(f'saque de R$100,00 na conta {cp.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$100,00 na conta {cp.nmr_conta}')

    if cp.saque(-300, 'PIX'):
        # Tenta realizar um saque de 300.
        print(f'saque de R$300,00 na conta {cp.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$300,00 na conta {cp.nmr_conta}')

    contas.append(cl)
    # Adiciona a conta de Ana Souza à lista de contas.
    contas.append(cc)
    # Adiciona a conta de Pedro José à lista de contas.
    contas.append(cp)
    # Adiciona a conta de Klaber da Silva à lista de contas.

    print()

    for conta in contas:
        # Itera sobre as contas e imprime o extrato de cada uma.
        conta.imprimirExtrato()
        print()
