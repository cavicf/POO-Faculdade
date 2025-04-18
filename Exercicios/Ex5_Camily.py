# Camily Victal Finamor - 2024001197

from abc import ABC, abstractmethod
from datetime import date

# Classe abstrata Venda: representa uma venda genérica
class Venda(ABC):
    def __init__(self, nroNF, dtEmissao):
        # Número da Nota Fiscal e data de emissão
        self._nroNF = nroNF
        self._dtEmissao = dtEmissao
        self._itens = []  # Lista para armazenar os itens da venda

    @property
    def nroNF(self):
        return self._nroNF
    
    @property
    def dtEmissao(self):
        return self._dtEmissao
    
    @property
    def itens(self):
        return self._itens
    
    # Método para adicionar um item à venda
    def adicionaItem(self, codProd, quant, precoUnit):
        item = Item_Venda(codProd, quant, precoUnit)  # Cria um novo Item_Venda
        self._itens.append(item)  # Adiciona o item à lista de itens

    # Método para calcular o total vendido
    def calculaTotalVendido(self):
        return sum([p.precoUnit * p.quant for p in self._itens]) #filtro oq vou pesquiser na lista
    #posso fazer contas tbm com esse filtro
    # Métodos abstratos que devem ser implementados nas subclasses
    @abstractmethod
    def geraNF(self):
        pass

    @abstractmethod
    def calculaImposto(self):
        pass

#########################################################################
# Classe concreta da venda a pessoa física
class VendaPF(Venda):
    def __init__(self, nroNF, dtEmissao, cpf, nome):
        super().__init__(nroNF, dtEmissao)  # Chama o construtor da classe mãe
        self._cpf = cpf  # CPF do cliente
        self._nome = nome  # Nome do cliente

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    # Implementação do método para gerar a nota fiscal (vazia por enquanto)
    def geraNF(self):
        pass

    # Método para calcular o imposto para venda a pessoa física
    def calculaImposto(self):
        total = self.calculaTotalVendido()  # Calcula o total vendido
        return (9/100) * total  # Aplica a alíquota de 9%

######################################################################
# Classe concreta de venda a pessoa jurídica
class VendaPJ(Venda):
    def __init__(self, nroNF, dtEmissao, cnpj, nomeFantasia):
        super().__init__(nroNF, dtEmissao)  # Chama o construtor da classe mãe
        self._cnpj = cnpj  # CNPJ do cliente
        self._nomeFantasia = nomeFantasia  # Nome fantasia do cliente

    @property
    def cnpj(self):
        return self._cnpj
    
    @property
    def nomeFantasia(self):
        return self._nomeFantasia
    
    # Implementação do método para gerar a nota fiscal (vazia por enquanto)
    def geraNF(self):
        pass

    # Método para calcular o imposto para venda a pessoa jurídica
    def calculaImposto(self):
        total = self.calculaTotalVendido()  # Calcula o total vendido
        return (6/100) * total  # Aplica a alíquota de 6%
    
#######################################################################
# Classe dos itens que é agregada à venda
class Item_Venda:
    def __init__(self, codProd, quant, precoUnit):
        self._codProd = codProd  # Código do produto
        self._quant = quant  # Quantidade do produto
        self._precoUnit = precoUnit  # Preço unitário do produto

    @property
    def codProd(self):
        return self._codProd
    
    @property
    def quant(self):
        return self._quant
    
    @property
    def precoUnit(self):
        return self._precoUnit

######################################################################
# Testando tudo com o main fornecido
if __name__ == "__main__":
    totalFaturado = 0  # Inicializa o total faturado
    totalImposto = 0  # Inicializa o total de imposto
    vendas = []  # Lista para armazenar as vendas

    # Criação de uma venda para pessoa física
    vendapf = VendaPF(1000, date.today(), '123456789', 'Joao') 
    vendapf.adicionaItem(100, 10, 10)  # Adiciona itens à venda
    vendapf.adicionaItem(100, 10, 20) 
    vendapf.adicionaItem(100, 10, 30) 
    vendas.append(vendapf)  # Adiciona a venda à lista de vendas

    # Criação de uma venda para pessoa jurídica
    vendapj = VendaPJ(1001, date.today(), '987654321', 'Silva Ltda') 
    vendapj.adicionaItem(200, 100, 10) 
    vendapj.adicionaItem(201, 100, 20) 
    vendas.append(vendapj)  # Adiciona a venda à lista de vendas

    # Cálculo do total faturado e do total de imposto para todas as vendas
    for venda in vendas: 
        totalFaturado += venda.calculaTotalVendido() 
        totalImposto += venda.calculaImposto() 

    # Impressão dos resultados
    print('Total faturado: {}'.format(totalFaturado)) 
    print('Total pago em impostos: {}'.format(totalImposto))
