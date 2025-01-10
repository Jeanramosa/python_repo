# Cajero automático

print("Bienvenido al cajero automático")
price = input("Introduce el precio del producto: ")
money = input("¿Con cuanto dinero pagas? ")

if not price.isdigit():
    print("Por favor, introduce un número entero.")
    exit()

if not money.isdigit():
    print("Por favor, introduce un número entero.")
    exit()

change = money - price

bills_100 = 100
bills_50 = 50
bills_20 = 20
bills_10 = 10

count = int(change // bills_100)
if count != 0:
    print(f"Hay que devolver {count} billetes de 100")

change = round(change % bills_100, 2)
count = int(change // bills_50)
if count != 0:
    print(f"Hay que devolver {count} billetes de 50")

change = round(change % bills_50, 2)
count = int(change // bills_20)
if count != 0:
    print(f"Hay que devolver {count} billetes de 20")

change = round(change % bills_20, 2)
count = int(change // bills_10)
if count != 0:
    print(f"Hay que devolver {count} billetes de 10")

if count == 0:
    print("Entonces no hay cambio")