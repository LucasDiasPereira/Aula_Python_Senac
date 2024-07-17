ongs: list['ONG'] = []

class ONG():
    def __init__(self, nome):
        self.nome = nome.capitalize()
        self.projetos: list['Projeto'] = []

    def listar_projetos(self):
        print(self.projetos)

    def buscar_projeto(self, nome):
        projeto_nome = input("Pesquisa de ong por nome: ").capitalize()
        for projeto in self.projetos:
            if projeto_nome == nome:
                return projeto
        return None


class Projeto():
    def __init__(self, nome, descricao, responsavel, status):
        self.nome = nome.capitalize()
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status


def listar_ongs():
    for i, ong in enumerate(ongs, 1):
        print(f"{i} - {ong.nome}")


def buscar_ongs():
    ong_busca = input("Digite o nome da ONG que deseja buscar: ").capitalize()
    for ong in ongs:
        if ong_busca == ong.nome:
            print("Ong selecionada")
            return ong
        else:
            print("Ong não encontrada")
    

while True:
    print("\n\nBem vindo ao menu, escolha uma das opções abaixo: \n\n")
    print("1 - Cadastrar ONG\n")
    print("2 - Cadastrar Projeto\n")
    print("3 - Listar ONGs\n")
    print("4 - Buscar Ong por nome\n")
    print("5 - Sair\n")
    opcao = int(input(""))

    if opcao == 1:
        nome = input("Digite o nome da ONG: ").capitalize()
        ongs.append(ONG(nome))
        print("Ong cadastrada com sucesso!")

    elif opcao == 2:
        print("Em qual ONG vamos cadastrar o projeto? ")
        listar_ongs()
        ong_do_projeto = int(input("\nSelecione: \n")) - 1
        if ong_do_projeto < 0 or ong_do_projeto > len(ongs):
            print("Ong não encontrada")
        else:
            nome = input("Digite o nome do projeto: ")
            descricao = input("Digite a descrição do projeto: ")
            responsavel = input("Digite o nome do responsável pelo projeto: ")
            status = input("Digite o status do projeto: ")
            ong = ongs[ong_do_projeto]
            ong.projetos.append(Projeto(nome, descricao, responsavel, status))
            print(f"O projeto {nome} foi cadastrado com sucesso!")
            

    elif opcao == 3:
        listar_ongs()

    elif opcao == 4:
       ong = buscar_ongs() 
       print(ong.nome)
        
    elif opcao == 5:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, selecione uma das opções do menu.")
