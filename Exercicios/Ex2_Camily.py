# Camily Victal Finamor / 2024001197
from abc import ABC, abstractmethod

# Classe base abstrata dos terrenos
class Terreno(ABC):
    # Construtor que inicializa a localização e o preço do terreno
    def __init__(self, localizacao, preco):
        self._localizacao = localizacao  # Atributo privado para armazenar a localização do terreno
        self._preco = preco  # Atributo privado para armazenar o preço do terreno
    
    # Propriedade para acessar a localização do terreno
    @property
    def localizacao(self):
        return self._localizacao
    
    # Setter para modificar a localização do terreno
    @localizacao.setter
    def localizacao(self, nova):
        self._localizacao = nova
    
    # Propriedade para acessar o preço do terreno
    @property
    def preco(self):
        return self._preco
    
    # Setter para modificar o preço do terreno
    @preco.setter
    def preco(self, valor):
        self._preco = valor
    
    # Método abstrato que deve ser implementado pelas subclasses para calcular o peso do terreno
    @abstractmethod
    def calcula_peso(self):
        pass


##########################################################################

# Classe concreta: Terreno circular, derivada de Terreno
class Circular(Terreno):
    # Construtor que inicializa a localização, preço e o raio do terreno circular
    def __init__(self, localizacao, preco, raio):
        super().__init__(localizacao, preco)  # Chama o construtor da classe mãe
        self._raio = raio  # Atributo privado para armazenar o raio do terreno circular

    # Propriedade para acessar o raio do terreno circular
    @property
    def raio(self):
        return self._raio
    
    # Implementação do método calcula_peso para terrenos circulares
    # O peso é o preço por metro quadrado da área circular (usando a fórmula da área de um círculo)
    def calcula_peso(self):
        area = 3.14 * (self._raio**2)  # Calcula a área do terreno circular (π * r²)
        return self.preco / area  # Retorna o preço por metro quadrado (peso)
    
##########################################################################

# Classe concreta: Terreno retangular, derivada de Terreno
class Retangular(Terreno):
    # Construtor que inicializa a localização, preço, comprimento (maior lado) e largura (menor lado)
    def __init__(self, localizacao, preco, maior, menor):
        super().__init__(localizacao, preco)  # Chama o construtor da classe mãe
        self._maior = maior  # Atributo privado para armazenar o comprimento (maior lado)
        self._menor = menor  # Atributo privado para armazenar a largura (menor lado)
    
    # Propriedade para acessar o comprimento do terreno
    @property
    def maior(self):
        return self._maior
    
    # Propriedade para acessar a largura do terreno
    @property
    def menor(self):
        return self._menor
    
    # Implementação do método calcula_peso para terrenos retangulares
    # O peso é o preço por metro quadrado da área retangular (comprimento * largura)
    def calcula_peso(self):
        area = self._maior * self._menor  # Calcula a área do terreno retangular (comprimento * largura)
        return self._preco / area  # Retorna o preço por metro quadrado (peso)
    
###########################################################################

# Bloco principal para criar instâncias de terrenos e determinar o melhor custo-benefício
if __name__ == "__main__":
    # Inicializando instâncias das classes Terreno Circular e Retangular com dados fictícios
    terreno1 = Circular('Brasília', 70000, 15)  # Terreno circular em Brasília, preço R$70.000, raio 15 metros
    terreno2 = Retangular('Itajubá', 75000, 35, 20)  # Terreno retangular em Itajubá, preço R$75.000, 35x20 metros
    terreno3 = Circular('Córrego', 110000, 20)  # Terreno circular em Córrego, preço R$110.000, raio 20 metros
    
    # Criando uma lista com os terrenos
    terrenos = [terreno1, terreno2, terreno3]

    # Loop para imprimir os dados de cada terreno antes de calcular o melhor custo
    for terreno in terrenos:
        print(f'Localização: {terreno.localizacao} - Preço: R${terreno.preco} - Peso: {terreno.calcula_peso()}')

    # Encontrando o terreno com o menor custo por metro quadrado usando a função min
    # O cálculo do custo é feito usando o método calcula_peso, que retorna o preço por metro quadrado
    melhor_custo = min(terrenos, key=lambda terreno: terreno.calcula_peso())
    
    # Imprimindo o terreno com o melhor custo-benefício, ou seja, o menor preço por metro quadrado
    print(f'\nO melhor custo benefício é o terreno localizado em {melhor_custo.localizacao}, com preço de R${melhor_custo.preco} e peso de {melhor_custo.calcula_peso()}')
