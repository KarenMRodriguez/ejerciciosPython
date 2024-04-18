#El centro de prevención de sismos en Colombia desea realizar un programa que le permita llevar el Registro del los sismos presentados

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sismos = []

    def agregar_sismo(self, magnitud):
        self.sismos.append(magnitud)

    def promedio_sismos(self):
        if not self.sismos:
            return 0
        return sum(self.sismos) / len(self.sismos)


def registrar_ciudad(ciudades):
    nombre = input("Ingrese el nombre de la ciudad: ")
    ciudad = Ciudad(nombre)
    ciudades.append(ciudad)


def registrar_sismo(ciudades):
    nombre = input("Ingrese el nombre de la ciudad: ")
    ciudad = next((c for c in ciudades if c.nombre == nombre), None)
    if ciudad is None:
        print("La ciudad no está registrada.")
        return
    try:
        magnitud = float(input("Ingrese la magnitud del sismo (o '0' para cancelar): "))
        if magnitud == 0:
            print("Registro de sismo cancelado.")
            return
    except ValueError:
        print("Por favor, ingrese un número válido para la magnitud del sismo.")
        return
    ciudad.agregar_sismo(magnitud)
    print("Sismo registrado con éxito en {}.".format(ciudad.nombre))

def informe_riesgo(ciudades):
    for ciudad in ciudades:
        promedio = ciudad.promedio_sismos()
        if promedio < 2.5:
            print("{}: Amarillo (Sin riesgo)".format(ciudad.nombre))
        elif 2.6 <= promedio <= 4.5:
            print("{}: Naranja (Riesgo medio)".format(ciudad.nombre))
        else:
            print("{}: Rojo (Riesgo alto)".format(ciudad.nombre))

def buscar_sismos(ciudades):
    nombre = input("Ingrese el nombre de la ciudad: ")
    ciudad = next((c for c in ciudades if c.nombre == nombre), None)
    if ciudad is None:
        print("La ciudad no está registrada.")
        return
    sismos = ciudad.sismos
    if not sismos:
        print("No se han registrado sismos en {}.".format(ciudad.nombre))
    else:
        print("Sismos registrados en {}: {}".format(ciudad.nombre, sismos))
        promedio = ciudad.promedio_sismos()

def main():
    ciudades = []
    while True:
        print("\nMenú:")
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar promedio de sismos por ciudad")
        print("4. Informe de riesgo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_ciudad(ciudades)
        elif opcion == "2":
            registrar_sismo(ciudades)
        elif opcion == "3":
            buscar_sismos(ciudades)
        elif opcion == "4":
            informe_riesgo(ciudades)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()