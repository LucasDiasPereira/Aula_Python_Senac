doacao_valor = []
doacao_nome = []

def informacaoes_doacoes(valor):
    sub_opcao = int(input("Doação anonima? \n1 - Sim\n2 - Não\n"))
    if sub_opcao==1:
        print("A doação será anonima, obrigado!")
        doacao_nome.append("Doação anonima")
    else:
        nome = input("Digite seu nome: ")
        cpf = int(input("Informe seu CPF: "))
        email = input("Informe seu e-mail: ")
        doacao_nome.append(nome)
        print(f"Valor doado foi: {valor}")
    doacao_valor.append(valor)
    print("add valor a lista")
    
    

while True:    
    total = 0 
    for i in range(0,len(doacao_valor)):
        print(f"Nome:{doacao_nome[i]} valor:{doacao_valor[i]}")
        total += doacao_valor[i]  
    print(f"Bem vindo a nossa loja de doações! Doações totais: {total}")
    opcao = int(input("Escolha uma opção de doação: \n1 - R$50,00\n2 - R$100,00\n3 - R$200,00\n4 - R$300,00\n5 - Outros valores\n6 - Sair  \n"))
    if opcao == 1:
        informacaoes_doacoes(50)
    elif opcao == 2:
       informacaoes_doacoes(100)
    elif opcao == 3:
        informacaoes_doacoes(200)
    elif opcao == 4:
        informacaoes_doacoes(300)
    elif opcao == 5:
        valor = int(input("Digite o valor da doação: "))
        informacaoes_doacoes(valor)
    elif opcao == 6:
        break
    else:
        print("Opção inválida")