""" lampadas = ["Lâmpada 1", "Lâmpada 2", "Lâmpada 3", "Lâmpada 4", "Lâmpada 5", "Lâmpada 6", "Lâmpada 7", "Lâmpada 8", "Lâmpada 9", "Lâmpada 10"]

for i in range(len(lampadas)):
    if lampadas[i] == "Queimada":
        print(f"A {lampadas[i]} precisa ser trocada.")
    else:
        print(f"A {lampadas[i]} está funcionando corretamente.") """


lampadas = []
lampadas_acessas = []
lampadas_apagadas = []

while True:
    print("\nLista de opções:")
    print("1. Adicionar lâmpada acessa")
    print("2. Adicionar lâmpada apagada")
    print("3. Remover lâmpada")
    print("4. Listar lâmpadas")
    print("5. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Escolha uma opção entre 1 e 5.")
        continue

    if opcao == 1:
        lampada = input("Digite local da lâmpada acessa: ")
        if lampada not in lampadas:
            lampadas.append(lampada)
            lampadas_acessas.append(lampada)
            print(f"A lâmpada {lampada} foi adicionada à lista de lâmpadas e à lista de lâmpadas acessas.")
        else:
            print(f"A lâmpada {lampada} já existe na lista de lâmpadas.")

    elif opcao == 2:
        lampada = input("Digite o local da lâmpada apagada: ")
        if lampada not in lampadas:
            lampadas.append(lampada)
            lampadas_apagadas.append(lampada)
            print(f"A lâmpada {lampada} foi adicionada à lista de lâmpadas e à lista de lâmpadas apagadas.")
        else:
            print(f"A lâmpada {lampada} já existe na lista de lâmpadas.")

    elif opcao == 3:
        lampada = input("Digite o nome da lâmpada a ser removida: ")
        if lampada in lampadas:
            lampadas.remove(lampada)
            if lampada in lampadas_acessas:
                lampadas_acessas.remove(lampada)
            elif lampada in lampadas_apagadas:
                lampadas_apagadas.remove(lampada)
            print(f"A lâmpada {lampada} foi removida da lista de lâmpadas.")
        else:
            print(f"A lâmpada {lampada} não existe na lista de lâmpadas.")

    elif opcao == 4:
        print("\nLista de lâmpadas:")
        for i in range(len(lampadas)):
            if lampadas[i] in lampadas_acessas:
                print(f"A {lampadas[i]} está acessa.")
            elif lampadas[i] in lampadas_apagadas:
                print(f"A {lampadas[i]} está apagada.")
            else:
                print(f"A {lampadas[i]} está funcionando corretamente.")

    elif opcao == 5:
        print("Saindo...")
        break

    else:
        print("Opção inválida. Escolha uma opção entre 1 e 5.")