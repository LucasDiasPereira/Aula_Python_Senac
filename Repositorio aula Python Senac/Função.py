banco = "Função.txt"
chave = 10

def preenchido(entrada):
    txt = open(banco, "a")
  
    frase = ''
    for letra in entrada:
        frase += chr((ord(letra) + chave) % 127)
    txt.write(frase + "\n")
    txt.close()

def acesso():
    txt = open(banco, "r")
    conteudo = txt.read()
    frase = ''
    for letra in conteudo:
        frase += chr((ord(letra) - chave) % 127)
    print(frase)
    txt.close()

while True:
    entrada = input("Digite a frase para guardar: ")
    preenchido(entrada)
    acesso()
    if entrada == "sair":
        break