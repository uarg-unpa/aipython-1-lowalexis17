#1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Tiene edad suficiente para conducir.")
else:
    faltan_anios = 18 - edad
    print(f"Le faltan {faltan_anios} años para poder conducir.")

#2
mi_edad = 25
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario > mi_edad:
    diferencia = edad_usuario - mi_edad
    if diferencia == 1:
        print("¡Usted es mayor que yo por 1 año!")
    else:
        print(f"¡Usted es mayor que yo por {diferencia} años!")
elif edad_usuario < mi_edad:
    diferencia = mi_edad - edad_usuario
    if diferencia == 1:
        print("¡Yo soy mayor que usted por 1 año!")
    else:
        print(f"¡Yo soy mayor que usted por {diferencia} años!")
else:
    print("¡Somos de la misma edad! ¡Qué coincidencia!")

#3
contrasena_guardada = "Contraseña123"
contrasena_usuario = input("Ingrese su contraseña: ")
if contrasena_usuario.lower() == contrasena_guardada.lower():
    print("¡La contraseña es correcta!")
else:
    print("La contraseña no coincide.")

#4
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
if a > b:
    print("a es mayor que b.")
elif a < b:
    print("a es menor que b.")
else:
    print("a es igual a b.")

#5
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#6
numero = int(input("Ingrese un número del 1 al 7: "))
if 1 <= numero <= 7:
    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miércoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sábado")
    else:
        print("Domingo")
else:
    print("El número ingresado no está dentro del rango válido.")

#7
puntaje = int(input("Ingrese el puntaje del estudiante: "))
if 80 <= puntaje <= 100:
    print("A")
elif 70 <= puntaje <= 89:
    print("B")
elif 60 <= puntaje <= 69:
    print("C")
elif 50 <= puntaje <= 59:
    print("D")
elif 0 <= puntaje <= 49:
    print("F")
else:
    print("Puntaje fuera de rango.")

#8
edad_cliente = int(input("Ingrese la edad del cliente: "))
if edad_cliente < 4:
    print("El cliente puede entrar gratis.")
elif 4 <= edad_cliente <= 18:
    print("El precio de entrada es $5.")
else:
    print("El precio de entrada es $10.")

#9
# Solicitar edad e ingresos mensuales al usuario
edad = int(input("Ingrese su edad: "))
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales en dólares: "))

# Verificar si cumple con los requisitos para pagar impuestos
if edad > 18 and ingresos_mensuales >= 100000:
    print("Usted debe pagar el impuesto.")
else:
    print("Usted no tiene que pagar el impuesto.")