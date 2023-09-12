def retangulo(comprimento, largura):
    area = comprimento * largura
    print(f"A área desse retângulo é {area:.0f} unidades quadradas.")


def triangulo(base, altura):
    area = (base * altura) / 2
    print(f"A área desse triangulo é {area:.0f} unidades quadradas.")


def trapezio(baseMenor, baseMaior, altura):
    area = (baseMenor + baseMaior) * altura / 2
    print(f"A área desse trapezio é {area:.0f} unidades quadradas.")


retangulo(45, 65)
triangulo(20, 27)
trapezio(12, 8, 5)
