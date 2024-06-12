matricula = 1
qtd_alunos_feminino_altura_superior_170 = 0
qtd_alunos_masculino_bom = 0
qtd_alunos_masculino = 0

while matricula <= 5:
    print("Matrícula: ", matricula)

    while True:
        sexo = input("Digite o sexo do aluno (M/F): ").upper()
        if sexo == "M" or sexo == "F":
            break
        else:
            print("Digite um valor válido (M ou F).")
    
    while True:        
        altura = float(input("Digite a altura do aluno em cm: "))
        break
    else:   
        print("Digite apenas números para representar a altura.") 

    while True:    
        status_fisico = int(input("Digite o status físico do aluno (1-bom, 2-regular, 3-ruim): ")) 
        if status_fisico == 1 or status_fisico == 2 or status_fisico == 3:
            break 
        else:
            print("Digite um valor válido (1, 2 ou 3) para o status físico.")
    
    if sexo == "F" and altura >= 170:
        qtd_alunos_feminino_altura_superior_170 += 1

    if sexo.upper() == "M":
        qtd_alunos_masculino += 1
        if status_fisico == 1:  
            qtd_alunos_masculino_bom += 1

    matricula += 1

print("\n           Resultados:")
print("A quantidade de alunos do sexo feminino com altura superior a 170 cm é: ", qtd_alunos_feminino_altura_superior_170)

if qtd_alunos_masculino > 0:
    porcentagem_bom = (qtd_alunos_masculino_bom / qtd_alunos_masculino) * 100
    print("A porcentagem de alunos do sexo masculino com status físico 'bom' é:", int(porcentagem_bom),"%")
else:
    print("Não há alunos do sexo masculino cadastrados para calcular a porcentagem.")



  


    
  