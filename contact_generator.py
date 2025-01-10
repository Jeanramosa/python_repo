import csv
import os


archivo_contactos = 'contactos.csv'


def inicializar_archivo():
    if not os.path.exists(archivo_contactos):
        with open(archivo_contactos, mode='w', newline='') as archivo:
            campos = ['nombre', 'edad', 'ciudad']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()


def agregar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    edad = input("Introduce la edad del contacto: ")
    ciudad = input("Introduce la ciudad del contacto: ")

    with open(archivo_contactos, mode='a', newline='') as archivo:
        campos = ['nombre', 'edad', 'ciudad']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writerow({'nombre': nombre, 'edad': edad, 'ciudad': ciudad})
    print(f"Contacto de {nombre} agregado correctamente.")


def ver_contactos():
    with open(archivo_contactos, mode='r', newline='') as archivo:
        lector = csv.DictReader(archivo)
        contactos = list(lector)
        if not contactos:
            print("No hay contactos guardados.")
        else:
            print("Lista de contactos:")
            for contacto in contactos:
                print(f"Nombre: {contacto['nombre']}, Edad: {contacto['edad']}, Ciudad: {contacto['ciudad']}")


def buscar_contacto():
    nombre_buscar = input("Introduce el nombre del contacto a buscar: ")
    encontrado = False
    with open(archivo_contactos, mode='r', newline='') as archivo:
        lector = csv.DictReader(archivo)
        for contacto in lector:
            if contacto['nombre'].lower() == nombre_buscar.lower():
                print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Edad: {contacto['edad']}, Ciudad: {contacto['ciudad']}")
                encontrado = True
                break
    if not encontrado:
        print(f"No se encontró ningún contacto con el nombre {nombre_buscar}.")


def eliminar_contacto():
    nombre_eliminar = input("Introduce el nombre del contacto a eliminar: ")
    contactos_actuales = []
    encontrado = False


    with open(archivo_contactos, mode='r', newline='') as archivo:
        lector = csv.DictReader(archivo)
        contactos_actuales = [contacto for contacto in lector]


    contactos_nuevos = [contacto for contacto in contactos_actuales if contacto['nombre'].lower() != nombre_eliminar.lower()]


    if len(contactos_actuales) != len(contactos_nuevos):
        with open(archivo_contactos, mode='w', newline='') as archivo:
            campos = ['nombre', 'edad', 'ciudad']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(contactos_nuevos)
        print(f"Contacto {nombre_eliminar} eliminado correctamente.")
    else:
        print(f"No se encontró el contacto con el nombre {nombre_eliminar}.")


def mostrar_menu():
    print("\nGestor de Contactos")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")


def gestionar_contactos():
    inicializar_archivo()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            ver_contactos()
        elif opcion == '3':
            buscar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            print("Saliendo del gestor de contactos.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")


if __name__ == "__main__":
    gestionar_contactos()
