class Animal:
    def __init__(self, nome, tamanho, cor, peso, coracao, racional):
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.peso = peso
        self.coracao = coracao
        self.racional = racional

    def info(self):
        return {
            'nome': self.nome,
            'tamanho': self.tamanho,
            'cor': self.cor,
            'peso': self.peso,
            'coracao': self.coracao,
            'racional': self.racional,
        }

    def andar(self):
        return f'{self.nome} está andando'


class Humano(Animal):
    def __init__(self, nome, tamanho, cor, peso):
        super().__init__(nome, tamanho, cor, peso, True, True)


class Cachorro(Animal):
    def __init__(self, nome, tamanho, cor, peso, raca):
        super().__init__(nome, tamanho, cor, peso, True, False)
        self.raca = raca
