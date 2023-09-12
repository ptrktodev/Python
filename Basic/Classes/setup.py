class carro():
    def __init__(self, marca, cor, motor):
        self.marca = marca
        self.cor = cor
        self.motor = motor

    def InfosModel(self):
        print(self.marca, self.motor, self.cor)


car = carro('Onix', 'Vermelho', '2.0')

print(car.cor)
car.InfosModel()
