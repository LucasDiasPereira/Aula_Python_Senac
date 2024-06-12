lista_de_nomes = []

while True:
    nome = input("Por favor, digite um nome (ou 'sair' para parar): ").capitalize()
    if nome == "Sair":
        break
    lista_de_nomes.append(nome)

print("A lista de nomes é: ", lista_de_nomes)



