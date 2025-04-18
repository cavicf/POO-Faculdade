# Camily Victal Finamor - 2024001197
from datetime import date

# Classe Conta: representa uma conta bancária
class Conta():
    def __init__(self, nroConta, nome, limite, senha):
        self._nroConta = nroConta  # Número da conta
        self._nome = nome  # Nome do titular da conta
        self._limite = limite  # Limite da conta
        self._senha = senha  # Senha da conta
        self._transacoes = []  # Lista de transações realizadas na conta

    # Propriedades para acessar os atributos privados
    @property
    def nroConta(self):
        return self._nroConta
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def senha(self):
        return self._senha
    
    @property
    def transacoes(self):
        return self._transacoes
    
    # Método para adicionar um depósito à conta
    def adicionaDeposito(self, valor, data, nomeDepositante):
        deposito = Deposito(valor, data, nomeDepositante)  # Cria um objeto Deposito
        return self._transacoes.append(deposito)  # Adiciona o depósito à lista de transações
    
    # Método para adicionar um saque à conta
    def adicionaSaque(self, valor, data, senha):
        # Verifica se a senha está correta e se há saldo suficiente para o saque
        if senha != self._senha or self.calculaSaldo() < valor:
            return False  # Retorna False se a operação não puder ser realizada
        saque = Saque(valor, data, senha)  # Cria um objeto Saque
        self._transacoes.append(saque)  # Adiciona o saque à lista de transações
    
    # Método para adicionar uma transferência entre contas
    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        # Verifica se a senha está correta e se há saldo suficiente para a transferência
        if senha != self._senha or self.calculaSaldo() < valor:
            return False  # Retorna False se a operação não puder ser realizada
        transf = Transferencia(valor, data, senha, "D")  # Cria um objeto Transferência para a conta de origem
        transf2 = Transferencia(valor, data, senha, "C")  # Cria um objeto Transferência para a conta de destino
        contaFavorecido._transacoes.append(transf2)  # Adiciona a transferência à conta do favorecido
        self._transacoes.append(transf)  # Adiciona a transferência à lista de transações da conta de origem
    
    # Método para calcular o saldo da conta
    def calculaSaldo(self):
        saldoFinal = 0  # Inicializa o saldo final
        # Itera sobre as transações para calcular o saldo
        for i in self._transacoes:
            if isinstance(i, Deposito) or (isinstance(i, Transferencia) and i.tipoTransf == "C"): #verifica o tipo do objeto
                saldoFinal += i.valor  # Adiciona o valor de depósitos e transferências recebidas
            elif isinstance(i, Saque) or (isinstance(i, Transferencia) and i.tipoTransf == "D"):
                saldoFinal -= i.valor  # Subtrai o valor de saques e transferências enviadas
        return saldoFinal + self._limite  # Retorna o saldo total considerando o limite
    
###################################################################################################
# Classe Mãe Transacao: representa uma transação genérica
class Transacao:
    def __init__(self, valor, data):
        self._valor = valor  # Valor da transação
        self._data = data  # Data da transação

    # Propriedades para acessar os atributos privados
    @property
    def valor(self):
        return self._valor
    
    @property
    def data(self):
        return self._data

#####################################################################################################
# Classe filha Saque: representa uma transação de saque
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)  # Chama o construtor da classe mãe
        self._senha = senha  # Senha para o saque

    @property
    def senha(self):
        return self._senha

#####################################################################################################
# Classe filha Deposito: representa uma transação de depósito
class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)  # Chama o construtor da classe mãe
        self._nomeDepositante = nomeDepositante  # Nome do depositante

    @property
    def nomeDepositante(self):
        return self._nomeDepositante

####################################################################################################
# Classe filha Transferencia: representa uma transação de transferência
class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)  # Chama o construtor da classe mãe
        self._senha = senha  # Senha para a transferência
        self._tipoTransf = tipoTransf  # Tipo da transferência: "D" para débito, "C" para crédito

    @property
    def senha(self):
        return self._senha
    
    @property
    def tipoTransf(self):
        return self._tipoTransf
    
####################################################################################################
# Bloco principal para criar instâncias de contas e testar o sistema
if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')  # Cria a conta de Jose
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')  # Adiciona um depósito à conta de Jose
    # Tenta realizar saques e verifica se são bem-sucedidos
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False:  # Deve falhar devido à senha errada
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')  # Cria a conta de Joao
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')  # Adiciona um depósito à conta de Joao
    # Tenta realizar saques e transferências, verificando os resultados
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False:  # Deve falhar devido ao saldo insuficiente
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')

    # Exibe os saldos finais das contas
    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo()))  # Deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo()))  # Deve imprimir 1700
