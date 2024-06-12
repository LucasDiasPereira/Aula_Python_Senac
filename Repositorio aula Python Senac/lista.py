# while True:
#     nome = "carro_do_leite.txt"
#     f = open(nome, "a")
#     frase = input("\nAdicione algo: ")
#     new_frase = ""
#     for letra in frase:
#         new_frase += chr(ord(letra)+1) 
#     f.write(new_frase + "\n")

#     nome = "carro_do_leite.txt"
#     f = open(nome, "r")
#     print(f.read())
# print(ord('|')-1)
# print(chr(124))

def lista():
    a = 0
    while True:
        a += 1
        print(chr(a)+1)
        if a == 126:
            break

lista()-1



