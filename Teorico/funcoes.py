from classe import *

def cadastrar_humano():
    print ("Vamos cadastrar um humano: ")
    nome = input("Informe o nome: ")
    tamanho = input("Informe a altura/em cm(sem espaço ou virgula): ")
    cor = input("Informe a cor: ")
    peso = input("Informe o peso do humano: ")
    humano = Humano(nome, tamanho, cor, peso)
    return humano


def cadastrar_cachorro():
    print ("Vamos cadastrar um cachorro:")
    nome = input("Informe o nome: ")
    tamanho = input("Informe o tamanho/em cm: ")
    cor = input("Informe a cor ou cores: ")
    peso = input("Informe o peso: ")
    raca = input("Informe a raça: ")
    cachorro = Cachorro(nome, tamanho, cor, peso, raca)
    return cachorro


def listar_humanos(humanos):
    print("Lista de Humanos:")
    for i, humano in enumerate(humanos):
        print(f"{i+1}. {humano.nome}")


def listar_cachorros(cachorros):
    print("Lista de Cachorros:")
    for i, cachorro in enumerate(cachorros):
        print(f"{i+1}. {cachorro.nome} - {cachorro.raca}")
