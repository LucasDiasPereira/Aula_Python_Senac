import part1 as i

while True:
    um = "part12.txt"
    dois = input("\n\nBem vindo ao meu de criptografia: \n\n1-Criptografar\n2-Descriptografar\n3-Sair\n\n")
    tres = 10
    if dois == "1":
        quatro = input("Digite o texto a ser criptografado: ")
        i.embaralhe(um,quatro,tres)
    elif dois == "2":
        i.desembaralhe(um,tres)
    elif dois == "3":
        fechar = input("Deseja fechar?(Sim ou Não)").upper
        if fechar == "SIM":
            break
        if fechar == "NÃO":
            continue
        else:
            print("Opção inválida")
    else:
        print("Opção inválida. Escolha uma opção entre 1 e 3.")