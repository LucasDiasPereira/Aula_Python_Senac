preco_azul = 20.00
preco_laranja = 30.00
preco_roxo = 40.00
preco_marrom = 50.00
preco_total = 0.00
contagem_azul = 0
contagem_laranja = 0
contagem_roxo = 0
contagem_marrom = 0


print("Bem-vindo à locadora de CDs!")
print("Por favor, insira a quantidade de CDs por cor.")

entrada = "sim"
while entrada =="sim":
    #CD azul:
    qtd_azul = int(input("Quantidade de CDs 🔵: "))
    total_azul = qtd_azul * preco_azul
    preco_total += total_azul
    if qtd_azul > 0:
        print("Valor total no carrinho: ", preco_total)
    #CD laranja:
    qtd_laranja = int(input("Quantidade de CDs 🟠: "))
    total_laranja = qtd_laranja * preco_laranja
    preco_total += total_laranja
    if qtd_laranja > 0:
        print("Valor total no carrinho: ", preco_total)
    #CD roxo:
    qtd_roxo = int(input("Quantidade de CDs 🟣: "))
    total_roxo = qtd_roxo * preco_roxo
    preco_total += total_roxo
    if qtd_roxo > 0:
        print("Valor total no carrinho: ", preco_total)
    #CD marrom:
    qtd_marrom = int(input("Quantidade de CDs 🟤: "))
    total_marrom = qtd_marrom * preco_marrom
    preco_total += total_marrom
    if qtd_marrom > 0:
        print("Valor total no carrinho: ", preco_total)
    #Loop
    entrada = input("Deseja inserir mais?(sim/nao) ")

 
print("\nPreço total dos CDs: R$",preco_total)

