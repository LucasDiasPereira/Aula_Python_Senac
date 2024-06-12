valor_cripto = 200
nome = "banco_01.txt"
discritor = open(nome,"a")
frase = input("Digite: ")
new_frase = ''
for letra in frase:
    new_frase += chr((ord(letra)+valor_cripto) % 127)
discritor.write(new_frase)
discritor.close()

nome = "banco_01.txt"
discritor = open(nome, "r")
new_frase = ''
for letra in discritor.read():
    new_frase += chr((ord(letra)-valor_cripto) % 127)
print(new_frase)