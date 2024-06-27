catalogo = []
import funcoes as f
while True:
    print("\n\nBem vindo ao menu, escolha uma das opções abaixo: \n\n")
    print("1 - Cadastrar ONG\n")
    print("2 - Cadastrar Projeto\n")
    print("3 - Listar ONGs\n")
    print("4 - Listar Projetos\n")
    print("5 - Sair\n")
    opcao = int(input(""))
    if opcao == 1:
        nome = input("Digite o nome da Ong: \n")
        tipo = input("Digite o tipo da Ong: \n")
        CNPJ = input("Digite o CNPJ da Ong: \n")
        ong = f.criacao_ong(nome,tipo,CNPJ)
        catalogo.append(ong)
    elif opcao == 2:
        ong_do_projeto = input("Digite o nome da Ong do projeto: \n")
        ong = f.localizar_ong(ong_do_projeto,catalogo)
        if ong is None:
            print("Ong não encontrada")
            break        
        nome = input("Digite o nome do projeto: \n")
        descricao = input("Digite a descrição do projeto: \n")        
        ong['projetos'].append(f.criacao_projeto(nome,descricao))
    elif opcao == 3:
        print(catalogo)
    elif opcao == 4:
        print(f.lista_projeto(nome,ong))
    elif opcao == 5:
        print("Fechando o menu!")
        break
    else:
        print("Opção inválida, tente novamente!")
