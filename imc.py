# calcula el IMC de los estudiantes nuevos
estudiante=""
edad= 0
imc=0
peso=0.0
altura=0.0

estudiante=(input("ingrese su nombre: "))
edad=int(input("ingrese su edad: "))
peso=float(input("ingrese su peso (kg):"))
altura=float(input("ingrse su estatura (m): "))

imc=(peso/altura**2)

if(imc>=18.5) and (imc<24.9):
    print(f"el estudiante {estudiante} tiene {edad} años de edad")
    print (f"tiene el imc de {imc}: peso es normal")
elif(imc>=25) and (imc<29.9):
    print(f"el estudiante {estudiante}tiene {edad} años de edad")
    print (f"tiene el imc de {imc}:sobrepeso")
elif(imc>=30) and (imc<34.9):
    print(f"el estudiante {estudiante} tiene{edad} años de edad")
    print (f"tiene el imc de {imc}:obesidad I")
elif(imc>=35) and (imc<39.9):
    print(f"el estudiante {estudiante} tiene{edad} años de edad")
    print (f"tiene el imc de {imc}:obesidad II")
elif(imc>40):
    print(f"el estudiante {estudiante} tiene {edad} años de edad")
    print (f"tiene el imc de {imc}obesidad III")

           
