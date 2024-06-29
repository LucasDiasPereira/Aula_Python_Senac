class Carro ():
    marca = ''
    modelo = ''
    ano = 2001
    cor = ''
    motor = False
    velocidade = 0

    def __init__(self,cor):
        self.cor = cor
    # def __init__(self,_marca,_modelo,_ano,_cor):
    #     self._marca = ''
    #     self._modelo = ''
    #     self._ano = ''
    #     self._cor = ''
    def ligar_motor(self):
        print('Motor ligado')
        self.motor = True
    def desligar_motor(self):
        print('Motor desligado')
        self.motor = False
    def status_motor(self):
        print(self.motor)
    def acelerar(self):
        if self.motor == True:
            print('Acelerando')
            while self.velocidade < 100:
                self.velocidade += 5
        else:
            print('Motor esta desligado')

    
# carro_1 = Carro("Peugrot","3008",2019,"Cinza")
# print(carro_1)
# print(carro_1.marca)
# print(carro_1.modelo)
# print(carro_1.ano)
# print(carro_1.cor)

carro_2 = Carro('Cinza')
print(carro_2)
print(carro_2.marca)
print(carro_2.modelo)
print(carro_2.ano)
print(carro_2.cor)

carro_2.ligar_motor()
carro_2.status_motor()
carro_2.desligar_motor()
carro_2.status_motor()
