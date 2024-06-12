dicionario = [
          {'nome':'Lucas', 'valor': '10', 'CPF': 'xxx', 'E-mail': 'xxx', 'Telefone': 'xxx'},
          {'nome':'Murilo', 'valor': '20', 'CPF': 'yyy', 'E-mail': 'yyy', 'Telefone': 'yyy'},
          {'nome':'Allan', 'valor': '30', 'CPF': 'zzz', 'E-mail': 'zzz', 'Telefone': 'zzz'}
]

for i in dicionario[0].keys():
    linha = i + ': '
    for dados in dicionario:
        linha += str(dados[i]) + ' '
    print(linha)


dicionario = [
          {'nome':'Lucas', 'valor': '10', 'CPF': 'xxx', 'E-mail': 'xxx', 'Telefone': 'xxx'},
          {'nome':'Murilo', 'valor': '20', 'CPF': 'yyy', 'E-mail': 'yyy', 'Telefone': 'yyy'},
          {'nome':'Allan', 'valor': '30', 'CPF': 'zzz', 'E-mail': 'zzz', 'Telefone': 'zzz'}
]

for i in range(0,len(dicionario)):
    for key in dicionario[i].keys():
        print(f"{key}: {dicionario[i][key]}")