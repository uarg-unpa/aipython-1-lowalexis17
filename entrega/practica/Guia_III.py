#1
i = 0
while i <= 100:
    print(i)
    i += 1

#2
for i in range(101):
    print(i, end=" ")

#3
# Bucle while
i = 10
while i >= 0:
    print(i)
    i -= 1

# Bucle for
for i in range(10, -1, -1):
    print(i)

#4
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

for num in range(inicio + 1, fin):
    print(num, end=" ")

#5
for i in range(1, 8):
    print("#" * i)

#6
for i in range(7):
    print("#" * 8)
#7
nombre = input("Ingrese su nombre: ")
num_veces = int(input("Ingrese un número entero: "))

for i in range(num_veces):
    print(nombre)

#8
num = int(input("Ingrese un número entero mayor a 3: "))

for i in range(1, num + 1, 2):
    print(i)

#9
for i in range(11):
    resultado = i * i
    print(f"{i} x {i} = {resultado}")

#10
for i in range(7):
    for j in range(i, 7):
        print(f"{i} {j}")

#11
n = int(input("Ingrese un número entero: "))
for i in range(1, n + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()

#12
N = int(input("Ingrese un número natural: "))
suma = 0
for i in range(1, N + 1):
    suma += i
    if i == N:
        print(i, end=" = ")
    else:
        print(i, end=" + ")
print(suma)

#13
N = int(input("Ingrese un número natural: "))
suma_pares = 0
for i in range(2, N * 2 + 1, 2):
    suma_pares += i
print(f"La suma de los primeros {N} números pares es: {suma_pares}")

#14
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
if num1 % 2 == 0:
    inicio = num1
else:
    inicio = num1 + 1
for i in range(inicio, num2 + 1, 2):
    print(i)

#15
num = int(input("Ingrese un número entero: "))
if num < 2:
    print("El número no es primo.")
else:
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")