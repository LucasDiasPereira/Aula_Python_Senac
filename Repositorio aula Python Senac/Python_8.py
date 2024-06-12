#Nome:
nome = input("Informe seu nome: ")
while len(nome)<3:
      print("Nome invalido!")
      nome = input("Informe seu nome: ")

#Idade:
idade = int(input("Informe sua idade: "))
while idade < 0 and idade > 150:
    print("Idade inválida")
    idade = input("Informe sua idade: ")

#Salario:
salario = float(input("Informe seu salario: "))
while salario < 0:
        print("Salario invalido")
        salario = input("Informe seu salario: ")

#Sexo:
sexo = input("Informe seu sexo(M/F): ").upper()
while sexo != "F" and sexo != "M":
    print("Sexo invalido")
    sexo = input("Informe seu sexo(M/F): ").upper()
 
print("Cadastro concluido: \nNome: ", nome,"\n Idade: ", idade, "\nSalario: ", salario, "\nSexo: ",sexo)







    
   

