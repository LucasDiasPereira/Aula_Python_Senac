import http.client
import json

class ONG:
    def __init__(self, nome):
        self.nome = nome.capitalize()
        self.projetos = []

class Projeto:
    def __init__(self, nome, descricao, responsavel, status):
        self.nome = nome.capitalize()
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status

class Gerenciado:
    def __init__(self):
        self.ongs = []
        self.api()

    def api(self):
        http_request = http.client.HTTPSConnection('api.jsonbin.io')
        http_request.request('GET', '/v3/b/66985766acd3cb34a8679cdf')
        response = http_request.getresponse()
        resposta_byte = response.read()
        json_ = json.loads(resposta_byte)['record']
        
        for ong in json_['ongs']:
            ong_ = ONG(ong['nome'])
            for projeto in ong['projetos']:
                ong_.projetos(Projeto(projeto['nome'], projeto['descricao'], projeto['responsavel'], projeto['status']))
                ong_.adicionar_projeto(projeto)
            self.adicionar_ong(ong_)
    
    def adicionar_ong(self, ong):
        self.ongs.append(ong)

    def adiconar_projeto(self,ong_):
        self.nome.append(ong_)
        self.descricao.append(ong_)
        self.responsavel.append(ong_)
        self.status.append(ong_)


    def printa(self):
        for ong in self.ongs:
            print(f"ONG: {ong.nome}")
            for projeto in ong.projetos:
                print(f"  - {projeto.nome}")
                print(f"    - {projeto.descricao}")
                print(f"    - {projeto.responsavel}")
                print(f"    - {projeto.status}")
            

gerenciado = Gerenciado()
gerenciado.printa()
