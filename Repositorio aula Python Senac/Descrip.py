txt = "banco_01.txt"
chave = 0
resultado = ''

descriptografar = open(txt, "r")
conteudo = descriptografar.read()
descriptografar.close()

while chave < 127:
    for letra in conteudo:
        if ord(letra) + chave > 127:
            resultado += chr((ord(letra) - chave) % 127)
        else:
            resultado += chr(ord(letra) + chave)
    print(f"Chave {chave}: {resultado}")
    if resultado.isalpha():  # Verificar se o resultado é uma string alfabética
        print(f"Chave encontrada: {chave}")
        print(f"Frase descriptografada: {resultado}")
        break
    chave += 1
    # save = open("resultados.txt","a")
    # save.write(resultado)
    # save.close()