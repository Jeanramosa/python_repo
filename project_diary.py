class Entry:
    def __init__(self, description, score_of_the_day, day):
        self.description = description
        self.score_of_the_day = score_of_the_day
        self.day = day

    def __str__(self):
        return f"Día: {self.day}, Nota: {self.score_of_the_day}, Descripción: {self.description}"


class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self):
        day = input("Introduce el día (formato YYYY-MM-DD): ")
        description = input("Describe tu día: ")
        score_of_the_day = float(input("¿Qué nota le das a tu día? (0-10): "))
        entry = Entry(description, score_of_the_day, day)
        self.entries.append(entry)
        print("Entrada añadida con éxito.")

    def view_entries(self):
        if not self.entries:
            print("El diario está vacío.")
        else:
            for idx, entry in enumerate(self.entries, start=1):
                print(f"{idx}. {entry}")

    def edit_entry(self):
        self.view_entries()
        index = int(input("Selecciona el número de la entrada que deseas editar: ")) - 1
        if 0 <= index < len(self.entries):
            print("Introduce los nuevos datos para la entrada:")
            day = input("Nuevo día (formato YYYY-MM-DD): ")
            description = input("Nueva descripción: ")
            score_of_the_day = float(input("Nueva nota del día (0-10): "))
            self.entries[index] = Entry(description, score_of_the_day, day)
            print("Entrada editada con éxito.")
        else:
            print("Índice inválido.")

    def delete_entry(self):
        self.view_entries()
        index = int(input("Selecciona el número de la entrada que deseas eliminar: ")) - 1
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
            print("Entrada eliminada con éxito.")
        else:
            print("Índice inválido.")

    def calculate_average_score(self):
        if not self.entries:
            print("No hay entradas para calcular la nota promedio.")
        else:
            average = sum(entry.score_of_the_day for entry in self.entries) / len(self.entries)
            print(f"La nota promedio de tus días es: {average:.2f}")


def main():
    diary = Diary()

    while True:
        print("\n--- Menú del Diario ---")
        print("1) Añadir una nueva entrada")
        print("2) Leer todas las entradas")
        print("3) Editar una entrada")
        print("4) Eliminar una entrada")
        print("5) Calcular la nota promedio")
        print("6) Salir")

        choice = input("Selecciona una opción (1-6): ")

        if choice == '1':
            diary.add_entry()
        elif choice == '2':
            diary.view_entries()
        elif choice == '3':
            diary.edit_entry()
        elif choice == '4':
            diary.delete_entry()
        elif choice == '5':
            diary.calculate_average_score()
        elif choice == '6':
            print("Gracias por usar el Diario. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
