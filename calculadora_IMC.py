def calcular_imc(peso, altura):
    altura_metros = altura / 100
    imc = peso / (altura_metros ** 2)
    return imc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en cm: "))

imc = calcular_imc(peso, altura)
print("Su IMC es: ", imc)