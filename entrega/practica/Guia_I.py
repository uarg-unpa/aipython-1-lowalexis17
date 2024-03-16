# a.
print("Las máquinas me sorprenden con mucha frecuencia.")

# b.
print()

# c.
print("Este es mi propio mensaje.")

# d.
print("23")  # Esto imprime el texto "23"
print(23)    # Esto imprime el número 23

# e.
print('Una computadora puede ser llamada "inteligente"\ si logra engañar a una persona haciéndole creer que es un humano.')

# f.
nombre = "Alexis"
apellido = "Low"
edad = 24
print(nombre, apellido, edad)

# g.
print(nombre, apellido, edad, sep="_")

# h.
calle = "Calle Principal"
numero = "123"
codigo_postal = "12345"
print(calle, numero, codigo_postal, sep="\t")

# i.
print(calle)
print(numero)
print(codigo_postal)

# j.
print("Feliz\nPrimavera\n2024")

# k.
print("Solo podemos ver poco del futuro,", end=" ")
print("pero lo suficiente para darnos cuenta de que hay mucho que hacer.")

# l.
print("    *")
print("   * *")
print("  * * *")
print(" * * * *")
print("*********")
print("   * *")
print("   * *")
print("  *****")

#3
# a.
nombre = "Alexis"
# b.
apellido = "Low"
# c.
edad = 24
# d.
altura = 1.80
# e.
num_vuelo = "AV123"
# f.
temp_ambiente = 25.5
# g.
salario_mensual = 0000.00
# h.
juego_terminado = True
# i.
es_par = True

#5.a
# Solicitar datos al usuario
nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Por favor ingresa tu apellido: ")
edad = input("Por favor ingresa tu edad: ")

# Mostrar mensaje creativo
print(f"¡Hola {nombre} {apellido} de {edad} años! Sé creativo.")

#b
# Solicitar datos al usuario y mostrar mensaje creativo
nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Por favor ingresa tu apellido: ")
edad = input("Por favor ingresa tu edad: ")

# Mostrar mensaje creativo
mensaje = f"¡Hola {nombre} {apellido} de {edad} años! Sé creativo."
input(mensaje)

# 6 
# Solicitar dos números enteros al usuario
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
potencia = num1 ** num2
resto = num1 % num2

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("Potencia:", potencia)
print("Resto:", resto)

#7
# Solicitar un número entero y un float al usuario
num_entero = int(input("Ingrese un número entero: "))
num_float = float(input("Ingrese un número float: "))

# Operaciones aritméticas
suma = num_entero + num_float
resta = num_entero - num_float
producto = num_entero * num_float
potencia = num_entero ** num_float
resto = num_entero % num_float

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("Potencia:", potencia)
print("Resto:", resto)

#8
import math

# Para el rectángulo
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)
area_rectangulo = base_rectangulo * altura_rectangulo

# Para la circunferencia
radio_circunferencia = float(input("Ingrese el radio de la circunferencia: "))
perimetro_circunferencia = 2 * math.pi * radio_circunferencia
area_circunferencia = math.pi * radio_circunferencia ** 2

# Mostrar resultados
print("Para el rectángulo:")
print("Perímetro:", perimetro_rectangulo)
print("Área:", area_rectangulo)

print("\nPara la circunferencia:")
print("Perímetro:", perimetro_circunferencia)
print("Área:", area_circunferencia)

#9
# Solicitar peso y estatura al usuario
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el resultado
print("Tu índice de masa corporal es:", imc)

#10
# Solicitar temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir de Celsius a Fahrenheit
fahrenheit = celsius * 9/5 + 32

# Mostrar resultado
print("La temperatura en grados Fahrenheit es:", fahrenheit)

#11
# Solicitar número de horas trabajadas y costo por hora
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
costo_por_hora = float(input("Ingrese el costo por hora: "))

# Calcular sueldo
sueldo = horas_trabajadas * costo_por_hora

# Mostrar sueldo
print("El sueldo correspondiente es:", sueldo)

#12
# Solicitar datos de la inversión al usuario
cantidad_invertida = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
num_anios = int(input("Ingrese el número de años: "))

# Calcular el capital obtenido en la inversión
capital = cantidad_invertida * (1 + interes_anual / 100) ** num_anios

# Mostrar el capital obtenido
print("El capital obtenido en la inversión es:", capital)

#13
# Inicializar una lista para almacenar los precios
precios = []

# Solicitar precios al usuario
for i in range(1, 11):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    precios.append(precio)

# Calcular el promedio de precios
promedio = sum(precios) / len(precios)

# Mostrar el promedio
print("El promedio de precios de los 10 productos es:", promedio)

#14

# Concatenar los strings
concatenacion = 'Una ambiciosa' + ' Introducción' + ' a Python' + ' Parte 1'
print(concatenacion)

#15
# a. Inicializar la variable sociedad
sociedad = 'aiPython P1'

# b. Imprimir la variable sociedad
print("Contenido de la variable sociedad:", sociedad)

# Imprimir la longitud de la variable sociedad
print("Longitud de la variable sociedad:", len(sociedad))

# c. Cambiar todos los caracteres a mayúsculas
sociedad_mayusculas = sociedad.upper()
print("Sociedad en mayúsculas:", sociedad_mayusculas)

# d. Cambiar todos los caracteres a minúsculas
sociedad_minusculas = sociedad.lower()
print("Sociedad en minúsculas:", sociedad_minusculas)

#16
texto = "sometimes it is the people no one imagines anything of who do the things that no one can imagine."

# Capitalizar la primera letra de la cadena
print("capitalize():", texto.capitalize())

# Convertir la primera letra de cada palabra a mayúsculas
print("title():", texto.title())

# Intercambiar entre mayúsculas y minúsculas
print("swapcase():", texto.swapcase())

#17
# Solicitar nombre completo al usuario
nombre_completo = input("Ingrese su nombre completo: ")

# Mostrar el nombre completo tres veces
print((nombre_completo + '\n') * 3)

#18
print("       *")
print("      ***")
print("     *****")
print("    *******")
print("   *********")
print("  ***********")
print(" *************")
print("       *")

#19
arbol = "       *\n      ***\n     *****\n    *******\n   *********\n  ***********\n *************\n       *"
print(arbol)

#20
arbol_1 = "       *"
arbol_2 = "       *"
print(arbol_1, arbol_2, sep="     ")
print("      ***", "      ***", sep="   ")
print("     *****", "     *****", sep="  ")
print("    *******", "    *******", sep=" ")
print("   *********", "   *********", sep="  ")
print("  ***********", "  ***********", sep="   ")
print(" *************", " *************", sep="    ")
print("       *", "       *", sep="     ")

#21
palabra = input("Ingrese una palabra: ")
palabra_modificada = palabra.replace('a', '😃')
print("Palabra modificada:", palabra_modificada)

#22
frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
palabras = frase.split()
primeras_dos_palabras = ' '.join(palabras[:2])
print("Las dos primeras palabras son:", primeras_dos_palabras)

#23
frase = " La ciencia es una ecuación diferencial. La religión es una condición de frontera. "
frase_sin_espacios = frase.strip()
print("Frase sin espacios en blanco al principio ni al final:", frase_sin_espacios)

#24
frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
frase_dividida = frase.split(" dos instalaciones,")
print(frase_dividida[0] + " dos instalaciones,\n" + frase_dividida[1])