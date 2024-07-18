import http.client
import json

class ONG:
    def __init__(self, nome):
        self.nome = nome.capitalize()
        self.projetos = []

class Projeto:
    def __init__(self, nome):
        self.nome = nome.capitalize()

class Gerenciado:
    def __init__(self):
        self.ongs = self.api()

    def api(self):
        ongs = []

        http_request = http.client.HTTPSConnection('api.jsonbin.io')
        http_request.request('GET', '/v3/b/66985766acd3cb34a8679cdf')['record']
        response = http_request.getresponse()
        resposta_byte = response.read()
        json_ = json.loads(resposta_byte)
        
        for ong in json_:
            ong = ONG(ong['nome'])
            for projeto in ong['projetos']:
                ong.projetos.append(Projeto(projeto['nome']))
                ong.adicionar_projeto(projeto)
            self.adcionar_ong(ong)
    
    def adicionar_ong(self, ong):
        self.ongs.append(ong)

    def imprimir(self):
        for ong in self.ongs:
            print(f"ONG: {ong.nome}")
            for projeto in ong.projetos:
                print(f"  - {projeto.nome}")
            print()

gerenciado = Gerenciado()
gerenciado.imprimir()
