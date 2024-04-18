#registrar 20 estudiantes y poder determinar el estado de salud de la cominidad estudiantil

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso_ideal = 0
obesidadI = 0
obesidadII = 0
obesidadIII = 0
sobrepeso = 0

for _ in range(20):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad de {}:".format(nombre)))
    peso = float(input("Ingrese el peso en Kg de {}:".format(nombre)))
    altura = float(input("Ingrese la altura en metros de {}:".format(nombre)))

    imc = calcular_imc(peso, altura)

    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 24.9:
        categoria = "Peso normal (Peso ideal)"
        peso_ideal += 1
    elif imc < 29.9:
        categoria = "Sobrepeso"
        sobrepeso += 1
    elif imc < 34.9:
        categoria = "Obesidad grado I"
        obesidadI += 1
    elif imc < 39.9:
        categoria = "Obesidad grado II"
        obesidadII += 1
    else:
        categoria = "Obesidad grado III (Obesidad mórbida)"
        obesidadIII += 1

    print("Nombre: {}, Edad: {}, IMC: {:.2f}, Categoría IMC: {}".format(nombre, edad, imc, categoria))

print("\nReporte:")
print("Estudiantes en peso ideal: {}".format(peso_ideal))
print("Estudiantes en obesidad grado I: {}".format(obesidadI))
print("Estudiantes en obesidad grado II: {}".format(obesidadII))
print("Estudiantes en obesidad grado III: {}".format(obesidadIII))
print("Estudiantes en sobrepeso: {}".format(sobrepeso))