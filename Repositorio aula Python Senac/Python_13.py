
estacionamento =[
        ["Disponivel ","Disponivel ","Disponivel ","Disponivel ","Disponivel ",],
        ["Disponivel ","Disponivel ","Disponivel ","Disponivel ","Disponivel ",],
        ["Disponivel ","Disponivel ","Disponivel ","Disponivel ","Disponivel ",]

]
def status():
    print("\n\n\033[33m                  Status atual da garagem: \n".center(200,'-'))
    for setor in range(0,len(estacionamento)):
        espaco = (f"\033[31m\n\033[31mSetor {setor+1}: \033[39m \n\n")
        for vaga in range(0,len(estacionamento[setor])):
            espaco += (f"\033[90mVaga {vaga+1}- {estacionamento[setor][vaga]} ")
        print(espaco)
def menu():
        print("\n\033[34m   Lista de opções:")
        print("1. Adicionar um carro")
        print("2. Remover um carro")
        print("3. Sair")
        print("4. Adicionar setor")
        print("5. Remover setor")
while True:
    status()
    menu()
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        setor = int(input("Digite o setor: "))
        vaga = int(input("Digite a vaga: "))
        if estacionamento[setor-1][vaga-1] == "Ocupado":
             print("\n\n\033[31mVaga ocupada\033[39m\n\n")
        else: 
            estacionamento[setor-1][vaga-1] = "\033[31mOcupado\033[39m"
            print("\n\n\033[39m\033[32mEstacionando...\033[39m\n\n")

    if opcao == 2:
        setor = int(input("Digite o setor: "))
        vaga = int(input("Digite a vaga: "))
        if estacionamento[setor-1][vaga-1] == "Disponivel":
              print("\033[39m\033[32m\n\nVaga disponivel\033[39m\n\n")
        else:
            estacionamento[setor-1][vaga-1] = "\033[32mDisponivel\033[39m"
            print("\n\n\033[39m\033[32mVaga liberada!\033[39m\n\n")
    if opcao == 3:
        print("Fechando")      
        break
    if opcao == 4:
        estacionamento.append(["Disponivel ","Disponivel ","Disponivel ","Disponivel ","Disponivel ",])
        print("Adicionado um setor novo")
        break
    if opcao == 5:
        setor_ = int(input("Informe o setor a ser removido ou '0' para sair: ")) - 1
        if setor_ > len(estacionamento):
                print("Setor não existe")
        elif setor == "0":
                break
        for vaga in range(0, len(estacionamento[setor_])):   
            if estacionamento[setor_][vaga] == "Ocupado":
                print("A vagas ocupadas dentro desse setor, remova o veiculo primeiro!")
            else:
                estacionamento.pop(setor_)
                print("Setor removido")
            
                
    

    

