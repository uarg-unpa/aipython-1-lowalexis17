#1
def multiplicacion(num1, num2):
    return num1 * num2

# Ejemplo
resultado = multiplicacion(3, 5)
print("El resultado de la multiplicación es:", resultado)

#2
def multiplicacion(num1=1, num2=1):
    return num1 * num2

# Ejemplo
resultado = multiplicacion()
print("El resultado de la multiplicación es:", resultado)

#3
def mensaje_creativo(nombre):
    return f"Hola {nombre}, bienvenido al mundo de la programación creativa!"

# Ejemplo
nombre = input("Ingrese su nombre: ")
mensaje = mensaje_creativo(nombre)
print(mensaje)

#4
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejemplo
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#5
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Ejemplo
num = int(input("Ingrese un número: "))
resultado = es_par_o_impar(num)
print(f"El número {num} es {resultado}.")

#6
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Ejemplo 
num = int(input("Ingrese un número entero: "))
resultado = factorial(num)
print(f"El factorial de {num} es {resultado}.")

#7
def maximo_de_tres(num1, num2, num3):
    return max(num1, num2, num3)

# Ejemplo
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
resultado = maximo_de_tres(a, b, c)
print(f"El máximo de los tres números es {resultado}.")

#8
def invertir_string(cadena):
    return cadena[::-1]

# Ejemplo
cadena = input("Ingrese una cadena de texto: ")
resultado = invertir_string(cadena)
print("El string invertido es:", resultado)

#9
def es_palindromo(cadena):
    return cadena == cadena[::-1]

# Ejemplo
palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

#10
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Ejemplo 
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius:.2f} grados Celsius.")