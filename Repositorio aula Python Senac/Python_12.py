# Dicionario[]
# Lista[]
# Tupula[]

matrix = [
          ['nome','Lucas','Murilo','Allan'],
          ['valor', '10','20','30'],
          ['CPF','xxx','yyy','zzz'],
          ['E-mail', 'xxx','yyy','zzz'],
          ['Telefone','xxx','yyy','zzz']
]

for l in range(0,len(matrix[0])):
    linha = ''
    for i in range(0,len(matrix)):
        linha += matrix[i][l]+' '
    print(linha)


matrix = [
          ['nome','Lucas','Murilo','Allan'],
          ['valor', '10','20','30'],
          ['CPF','xxx','yyy','zzz'],
          ['E-mail', 'xxx','yyy','zzz'],
          ['Telefone','xxx','yyy','zzz']
]

for i in range(0, len(matrix)):
    linha = ''
    for l in range(0, len(matrix[i])):
        linha += matrix[i][l] + ' '
    print(linha)


