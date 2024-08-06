from classe import *
from funcoes import *
from view import *

humanos = []
cachorros = []


while True:
    print(menuzinho())
    opcao = int(input("Digite uma opção: "))

    if opcao == "1":
        humano = cadastrar_humano()
        humanos.append(humano)
        print("Humano cadastrado com sucesso!")

    elif opcao == "2":
        cachorro = cadastrar_cachorro()
        cachorros.append(cachorro)
        print("Cachorro cadastrado com sucesso!")

    elif opcao == "3":
        listar_humanos(humanos)

    elif opcao == "4":
        listar_cachorros(cachorros)

    elif opcao == "5":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida, escolha uma das opções.")
