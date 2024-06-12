preco_azul = 20.00
preco_laranja = 30.00
preco_roxo = 40.00
preco_marrom = 50.00
preco_total = 0.00
contador = int
contagem_azul = 0
contagem_laranja = 0
contagem_roxo = 0
contagem_marrom = 0


print("Bem-vindo à locadora de CDs!")

entrada = "sim"
while entrada =="sim":
    contador = float(input("Por favor, escolha os CDs por cor.\n1- CDs 🔵\n2- CDs 🟠:\n3- CDs 🟣: \n4- CDs 🟤: \n"))
    if contador == 1:
        contagem_azul += 1
        total_azul = contagem_azul * preco_azul
    elif contador == 2:
        contagem_laranja += 1
        total_laranja = contagem_laranja * preco_laranja
    elif    contador == 3:
        contagem_roxo += 1 
        total_roxo = contagem_roxo * preco_roxo 
    elif contador == 4:
        contagem_marrom += 1
        total_marrom = contagem_marrom * preco_marrom
    print(preco_total = preco_total + total_azul + total_laranja + total_roxo + total_marrom)

    #Loop
    print("\nPreço total no carrinho: R$",preco_total)
    entrada = input("Deseja inserir mais?(sim/nao) ")

print("\nPreço total dos CDs: R$",preco_total)
    