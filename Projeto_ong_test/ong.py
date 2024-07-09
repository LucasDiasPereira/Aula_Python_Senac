class ONG():
    def __init__(self, nome):
        self.nome = nome
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projeto = projeto
        projeto = input("Adicione um projeto a ONG: ")
        self.projetos.append(projeto)

    def listar_projetos(self):
        print(self.projeto)

    def buscar_projeto(self, nome):
        projeto_nome = input("Pesquisa de ong por nome: ")
        for projeto in self.projeto:
            if projeto_nome == nome:
                return projeto
        return None    

class Projeto():
    def __init__(self, nome,descricao,responsavel,status):
        self.nome = nome
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status

class Gerenciador():
    def __init__(self):
        self.ongs = []
    def criacao_ong(self,nome):
        self.ongs.append(ONG(nome))
    def listar_ongs(self):
        for i in range(0,len(gerenciador.ongs)):
            print(f"{i+1} - {gerenciador.ongs[i].nome}")
    def buscar_ongs(self):
        ong_busca = input("Digite o nome da ONG que deseja buscar: ").capitalize()
        for ong in self.ongs:
            if ong_busca == ong.nome:
                print("Ong selecionada")
                return ong
            else:
                print("Ong não encontrada")
        
gerenciador = Gerenciador()



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
        gerenciador.criacao_ong(nome)
        print("Ong cadastrada com sucesso!")

    elif opcao == 2:
        print("Em qual ONG vamos cadastrar o projeto? ")
        gerenciador.listar_ongs()
        ong_do_projeto = int(input("\nSelecione: \n")) - 1
        if ong_do_projeto < 0 or ong_do_projeto > len(gerenciador.ongs):
            print("Ong não encontrada")
        else:
            novo_projeto = Projeto
            novo_projeto = input("Digite o nome do projeto: ")
            ong = ONG.adicionar_projeto(nome,descricao,responsavel,status)
            print(f"O projeto {nome} foi cadastrado com sucesso!")

    elif opcao == 3:
        gerenciador.listar_ongs()
                
    elif opcao == 4:
       ong = gerenciador.buscar_ongs() 
       print(ong.nome) 
        
    elif opcao == 5:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, selecione uma das opções do menu.")
