valor_cripto = 3
lista = "Lista de pessoas.txt"
discritor = open(lista,"a")
pessoa = ''
frase = input("Digite \nNome: ")
for letra in frase:
    pessoa += chr((ord(letra) + valor_cripto) % 127)
discritor.write(pessoa)

discritor = open(lista, "r")
pessoa = ''
for letra in discritor.read():
    pessoa += chr((ord(letra) - valor_cripto) % 127)
    
print(pessoa)