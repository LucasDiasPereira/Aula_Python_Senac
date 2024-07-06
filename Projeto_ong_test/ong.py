class ONG():
    def __init__(self):
        self.projetos = []

    def criacao_ong(nome):
        ong = {
        'nome':nome,         
        }
        return ong

    def adicionar_projeto(self, projeto):
        self.projeto = projeto
        projeto = input("Adicione um projeto a ONG: ")
        self.projetos.append(projeto)

    def listar_projetos(self):
        print(self.projeto)

    def buscar_projeto(self, nome=None):
        projeto_nome = input("Pesquisa de ong por nome: ")
        for projeto in self.projeto:
            if projeto_nome == nome:
                return projeto
            
class Gerenciador():
    ongs = []
    def __init__(self):
        self.ong = ONG()
    def criacao_ong(self,ong):
        self.ong = ong
        self.ongs.append(ong)

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
        nome = input("Digite o nome da ONG: ")
        ong = ONG.criacao_ong(nome)
        print("Ong cadastrada com sucesso!")
    elif opcao == 2:
        projeto = input("Adicione um projeto a ONG: ")
        ong = ONG.adicionar_projeto(projeto)
        print("Projeto cadastrado com sucesso!")