lista_nomes = []

for cont in range(5):
    nome = input("Digite um nome para a lista: ").capitalize()
    lista_nomes.append(nome)
    
for nome in lista_nomes:
    if nome.startswith("B"):
       print("O nome: ", nome, " não será adicionado")
       lista_nomes.remove(nome)
    if nome.startswith("A"):
        print(nome, " Esse vai pra lista de A")

print(lista_nomes)
