import random

numeroSecreto = random.randint(1, 100)

intentos = 1
numeroDeIntentos = 10
tiradas = []

while intentos < numeroDeIntentos:
    numero = int(input("Introduce el número que piensas que es: "))
    tiradas.append(numero)
    if numero == numeroSecreto:
        print(f"Has acertado el número secreto en solamente {intentos} intentos. Felicidades!")
        break
    elif numero < numeroSecreto:
        print(f"No es correcto. El numero secreto es mayor que el que has introducido. Te quedan {numeroDeIntentos- intentos} intentos.")
    elif numero > numeroSecreto:
        print(f"No es correcto. El numero secreto es menor que el que has introducido. Te quedan {numeroDeIntentos- intentos} intentos.")
    intentos += 1
else:
    print(f"Se han acabado las oportunidades y no lo has conseguido. El número secreto era: {numeroSecreto}")

print(f"Tus tiradas han sido: {tiradas}")