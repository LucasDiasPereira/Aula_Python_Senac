valor_cripto = 200
digitado = input("Letra:")
print(f"Valor deslocamento: "{valor_cripto})
print(f"Tabela: "{ord(digitado)})
print(f"Soma deslocamento + tabela {valor_cripto + ord(digitado)}")
print(f"Valor utilizado: {(valor_cripto + ord(digitado)) % 128}")