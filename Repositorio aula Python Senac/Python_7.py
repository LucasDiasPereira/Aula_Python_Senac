cont = 0
n = int
pares = 0
while cont < 15:
    n = int(input("Digite os número da lista: "))
    if n % 2 == 0:
     pares += 1
    cont += 1
    

print("\nOs núeros pares da lista são: ", pares)


count = 0
numeros_pares = 0
print("Digite 15 números inteiros:")
# Variáveis para armazenar os números pares
par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13, par14, par15 = 0, 0, 0, 0, 0

while count < 15:
    num = int(input(f"Digite o {count+1}º número: "))
    if num % 2 == 0:
        numeros_pares += 1
        # Verificando qual variável usar para armazenar o número par
        if numeros_pares == 1:
            par1 = num
        elif numeros_pares == 2:
            par2 = num
        elif numeros_pares == 3:
            par3 = num
        elif numeros_pares == 4:
            par4 = num
        elif numeros_pares == 5:
            par5 = num
        elif numeros_pares == 6:
            par6 = num
        elif numeros_pares == 7:
            par7 = num
        elif numeros_pares == 8:
            par8 = num
        elif numeros_pares == 9:
            par9 = num
        elif numeros_pares == 10:
            par10 = num
        elif numeros_pares == 11:
            par11 = num
        elif numeros_pares == 12:
            par12 = num
        elif numeros_pares == 13:
            par13 = num
        elif numeros_pares == 14:
            par14 = num
        elif numeros_pares == 15:
            par15 = num
    count += 1
if par1 != 0 :
    print (par1)
    if par2 != 0:
        print (par2)
        if par3 !=0:
            print (par3)
            if par4 !=0:
                print (par4)
                if par5 != 0 :
                    print(par5)
                    if par6 != 0:
                        print (par6)
                        if par7 != 0 :
                            print (par7)
                            if par8 !=0 :
                                print (par8)
                                if par9 !=0 :
                                    print (par9)
                                    if par10 != 0 :
                                        print (par10)
                                        if par11 != 0 :
                                            print (par11)
                                            if par12 != 0:
                                                print (par12)
                                                if par13 != 0 :
                                                    print (par13)
                                                    if par14 != 0 :
                                                        print (par14)
                                                        if par15 !=0 :
                                                            print (par15)