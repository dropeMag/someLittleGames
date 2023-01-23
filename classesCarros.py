class Carros:
    todos = []

    def __init__(self, marca, cor, ano, preco, pais):
        self.marca = marca
        self.cor = cor
        self.ano = int(ano)
        self.preco = float(preco)
        if pais.upper() == 'BRASIL':
            self.pais = 'Nacional'
        else:
            self.pais = 'Gringo'

        Carros.todos.append(self)

    def informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        print(f'Preço: R${self.preco:.2f}')
        print(f'País: {self.pais}')

    def ligar(self):
        print('Carro ligado com sucesso.')

    def acelerar(self):
        print('Carro acelerando!')

    def freiar(self):
        print('Carro freiou!')

    def __repr__(self):
        return f"Item: {self.marca}"


carro1 = Carros('Chevolé', 'Rosa', 2018, 12000, 'brasil')
carro2 = Carros('Voudisvagney', 'Cinza', 2017, 10000, 'brasil')
carro3 = Carros('Renou', 'Azul', 2008, 69000, 'paraguai')
print(Carros.todos)
