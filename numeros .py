#permita ingresar n numeros positivos y cuando se ingrese un numero negativo mostrar en pantalla el reporte
n = 1
par = 0
impar = 0
nrosIngresados = 0
nros20y50 = 0
nrosMe10 = 0
nrosMayores100 = 0
suma = 0

while True:
    n = int(input("Ingrese un número (-1 para salir): "))
    
    if n == -1:
        break
        
    nrosIngresados += 1
    
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    
    if n < 10:
        nrosMe10 += 1
    
    if 20 <= n < 50:
        nros20y50 += 1
    
    if n > 100:
        nrosMayores100 += 1
        suma += n

print("El total de números ingresados:", nrosIngresados)
print("El total de números pares:", par)
print("El total de números impares:", impar)
print("El total de números menores que 10:", nrosMe10)
print("El total de números entre 20 y 50:", nros20y50)
print("El total de números mayores a 100:", nrosMayores100)
if nrosMayores100 > 0:
    print("La suma de los números mayores a 100 es:", suma)