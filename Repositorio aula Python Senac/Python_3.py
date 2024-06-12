peso = float(input("Digite o peso do seu peixe "))
multa = 0
while peso>50:
    pesoSobrando = peso-50
    multa = pesoSobrando*4
    break
print("O valor da multa é: R$", multa)
