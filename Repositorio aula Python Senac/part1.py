def embaralhe(armazenamento,frase,valor_cripto):
    leitor = open(armazenamento,"a")
    armazenado = ''
    for letra in frase:
        armazenado += chr((ord(letra) + valor_cripto) % 127)
        leitor.write((armazenado) + "\n")
    leitor.close()    
    return armazenado

def desembaralhe(armazenado,valor_cripto):
    open(armazenado,"r")
    lido = ''
    for letra in armazenado:
        if letra == '\n':
            lido += '\n'
        else: 
            lido += chr((ord(letra) - valor_cripto) % 127)
    print("Nomes descriptografados:")
    for linha in lido:
        print(lido, end='')
    armazenado.close()