matricula = 1
qtd_alunos_feminino_altura_superior_170 = 0
qtd_alunos_masculino_bom = 0
qtd_alunos_masculino = 0

while matricula <= 4:
    print("Matrícula: ", matricula)
    sexo = input("Digite o sexo do aluno (M/F): ")
    altura = float(input("Digite a altura do aluno em cm: "))
    status_fisico = int(input("Digite o status físico do aluno (1-bom, 2-regular, 3-ruim): "))

    if sexo.upper() == "F" and altura >= 170:
        qtd_alunos_feminino_altura_superior_170 += 1

    if sexo.upper() == "M":
        qtd_alunos_masculino += 1
        if status_fisico == 1:  
            qtd_alunos_masculino_bom += 1

    if sexo != "M" and sexo != "F":
            print("Digite um valor valido:")

    matricula += 1

print("\nResultados:")
print("A quantidade de alunos do sexo feminino com altura superior a 170 cm é: ", qtd_alunos_feminino_altura_superior_170)

if qtd_alunos_masculino > 0:
    porcentagem_bom = (qtd_alunos_masculino_bom / qtd_alunos_masculino) * 100
    print("A porcentagem de alunos do sexo masculino com status físico 'bom' é:", int(porcentagem_bom),"%")
else:
    print("Não há alunos do sexo masculino cadastrados para calcular a porcentagem.")
