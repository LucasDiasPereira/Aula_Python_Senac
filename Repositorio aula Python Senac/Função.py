banco = "Função.txt"
chave = 10
def preenchido():
    txt = open(banco, "a")
    frase = ''
    for letra in entrada:
        frase += chr((ord(letra) + chave) % 127)
    txt.write(frase + "\n") 
    for linha in txt.readlines():
        acesso(linha.strip())
    txt.close()
    return frase

def acesso():
    txt = open(banco, "r")
    conteudo = txt.read()
    frase = ''
    for letra in conteudo:
        frase += chr((ord(letra) - chave) % 127)
    print(frase)
    txt.close()
    return frase

while True:
    entrada = input("Digite a frase para guardar: ")
    if entrada == "sair":
        break
    preenchido()
    acesso()
    for frase in nomes_descriptografados:
        print(frase)
    



