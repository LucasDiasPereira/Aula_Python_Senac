valor = 0

print("Bem vindo a nossa loja \nNosso catálogo de cores: Azul, Laranja, Roxo e Marrom")
cor = input("Digite a cor desejada: ")
while cor!= "sair":
    if cor == "azul":
        print("Azul selecionado")
        valor += 20
        cor = input("Se deseja mais, digite a cor desejada ou digite sair para finalizar: ")
    elif cor == "laranja":
        print("Laranja selecionado")
        valor += 30
        cor = input("Se deseja mais, digite a cor desejada ou digite sair para finalizar: ")
    elif cor == "roxo":
        print("Roxo selecionado")
        valor += 40
        cor = input("Se deseja mais, digite a cor desejada ou digite sair para finalizar: ")
    elif cor == "marrom":
        print("Marrom selecionado")
        valor += 50
        cor = input("Se deseja mais, digite a cor desejada ou digite sair para finalizar: ")
    else:
        print("Cor não encontrada")
        cor = input("Digite a cor desejada: ")

print("O valor total da sua compra é: ", valor)