import http.client
import json
def print_json(object):
    if type(object) is list:
        for json_ in object:
            for key in json_.keys():
                print(f"{key} : {json_[key]}")
    elif type(object) is dict:
        for key in object.keys():
            print(f"{key} : {object[key]}")


def api(url):
    http_request = http.client.HTTPSConnection('brasilapi.com.br')
    http_request.request('GET', url)
    response = http_request.getresponse()
    resposta_byte = response.read()
    # print(resposta_byte)
    json_ = json.loads(resposta_byte)
    return json_

while True:
    cep = input("Digite seu CEP: ")
    json_cep = api(f"/api/cep/v1/{cep}")
    print_json(json_cep)
