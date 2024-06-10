def analizar_numero(numero):
    resultado = {
        'Par o impar': 'Par' if numero % 2 == 0 else 'Impar',
        'Positivo, negativo o cero': 'Positivo' if numero > 0 else 'Negativo' if numero < 0 else 'Cero',
        'Divisible por 3': 'Sí' if numero % 3 == 0 else 'No',
        'Divisible por 5': 'Sí' if numero % 5 == 0 else 'No',
        'Divisible por 3 y por 5': 'Sí' if numero % 3 == 0 and numero % 5 == 0 else 'No'
    }
    return resultado
numero = 15
resultado = analizar_numero(numero)
print(resultado)