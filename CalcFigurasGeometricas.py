import math

# Función para el cuadrado
def area_perimetro_cuadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    return area, perimetro
# Funciones para rectangulo
def area_perimetro_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro
# Funciones para triangulos
def area_perimetro_triangulo_equilatero(lado):
    area = (math.sqrt(3) / 4) * lado ** 2
    perimetro = 3 * lado
    return area, perimetro
def area_perimetro_triangulo_rectangulo(base, altura):
    area = (base * altura) / 2
    perimetro = base + altura + math.sqrt(base ** 2 + altura ** 2)
    return area, perimetro
def area_perimetro_triangulo_isosceles(lado_base, lado_igual):
    altura = math.sqrt(lado_igual ** 2 - (lado_base / 2) ** 2)
    area = (lado_base * altura) / 2
    perimetro = 2 * lado_igual + lado_base
    return area, perimetro
# Funcion para circulo
def area_perimetro_circulo(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

# ejemplo de uso para cuadrado
lado_cuadrado = 5
area_cuadrado, perimetro_cuadrado = area_perimetro_cuadrado(lado_cuadrado)
print("Área del cuadrado:", area_cuadrado)
print("Perímetro del cuadrado:", perimetro_cuadrado)