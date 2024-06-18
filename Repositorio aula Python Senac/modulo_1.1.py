valor_cripto = 200
lista = "Lista de pessoas.txt"

def criptografar(frase):
    pessoa = ''
    for letra in frase:
        pessoa += chr((ord(letra) + valor_cripto) % 127)
    return pessoa

def descriptografar(pessoa):
    frase = ''
    for letra in pessoa:
        frase += chr((ord(letra) - valor_cripto) % 127)
    return frase

while True:
    frase = input("Digite o nome ou 'sair' para fechar: ")
    if frase == "sair":
            print("Saindo...")
            break
    discritor = open(lista, "a")
    discritor.write(criptografar(frase) + "\n")  
    discritor.close()

    discritor = open(lista, "r")

    print("Nomes descriptografados:")
    for linha in discritor.readlines():
         print(descriptografar(linha.strip()))
    discritor.close()