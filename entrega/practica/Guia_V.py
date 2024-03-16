#1
lista_vacia = []
#2
lista_mas_siete = [1, 2, 3, 4, 5, 6, 7, 8]
#3
mi_lista = [1, 2, 3, 4, 5]
longitud = len(mi_lista)
print("La longitud de la lista es:", longitud)
#4
frutas_favoritas = ["manzana", "banana", "uva", "kiwi"]

# a. Imprimir la longitud
print("La longitud de la lista de frutas es:", len(frutas_favoritas))

# b. Eliminar el primer elemento de la lista
frutas_favoritas.pop(0)

# c. Agregar un elemento al final de la lista
frutas_favoritas.append("pera")

# d. Imprimir los resultados anteriores
print("Lista de frutas después de eliminar el primer elemento y agregar 'pera':", frutas_favoritas)

#5
mi_lista = [1, 2, 3, 4, 5]
primer_elemento = mi_lista[0]
elemento_del_medio = mi_lista[len(mi_lista) // 2]
ultimo_elemento = mi_lista[-1]

print("Primer elemento:", primer_elemento)
print("Elemento del medio:", elemento_del_medio)
print("Último elemento:", ultimo_elemento)

#6
datos_personales = ["Juan", 30, 1.75, "Soltero", "Calle Principal 123"]

#7
companias_favoritas = ["Apple", "Google", "Microsoft", "Amazon"]

# a. Recorrer la lista y mostrar los datos con print
print("Compañías favoritas:")
for compania in companias_favoritas:
    print(compania)

# b. Recorrer la lista y mostrar el índice más el nombre de la compañía
print("Índice y compañía:")
for indice, compania in enumerate(companias_favoritas):
    print(f"{indice}: {compania}")

# c. Modificar alguna/s de las compañía/s de la lista y luego mostrarla
companias_favoritas[0] = "Tesla"
companias_favoritas[-1] = "Facebook"
print("Lista de compañías después de la modificación:", companias_favoritas)

#8
numeros = list(range(1, 11))

# a. Imprimir los tres primeros números utilizando rebanadas
print("Los tres primeros números son:", numeros[:3])

#9
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# a. Imprimir cada segundo elemento usando rebanadas
print("Cada segundo elemento:", letras[::2])

#10
lista = [10, 20, 30, 40, 50]

# a. Imprimir la lista en forma inversa usando rebanadas
print("Lista en forma inversa:", lista[::-1])

#11
palabras_favoritas = ["amor", "felicidad", "paz", "alegría", "esperanza"]

# a. Extraer una sublista conteniendo desde la segunda hasta la cuarta palabra
sublista = palabras_favoritas[1:4]
print("Sublista desde la segunda hasta la cuarta palabra:", sublista)

#12
flores = ["rosas", "orquídea", "lirio", "tulipan", "margarita", "dalia", "hortensia"]

# a. Mostrar tres elementos desde el tercer elemento
print("Tres elementos desde el tercer elemento:", flores[2:5])

# b. Mostrar los elementos en posiciones pares desde la segunda posición
print("Elementos en posiciones pares desde la segunda posición:", flores[1::2])

# c. Mostrar todos los elementos desde la primera posición saltando de a tres elementos
print("Todos los elementos desde la primera posición saltando de a tres elementos:", flores[::3])

#13
def contar_vocales(lista):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in lista:
        if caracter in vocales:
            contador += 1
    return contador

# Ejemplo
lista_caracteres = ['a', 'b', 'c', 'e', 'i', 'o', 'u']
cantidad_vocales = contar_vocales(lista_caracteres)
print("Cantidad de vocales en la lista:", cantidad_vocales)

#14
def intercalar_listas(lista1, lista2):
    nueva_lista = []
    for elemento1, elemento2 in zip(lista1, lista2):
        nueva_lista.append(elemento1)
        nueva_lista.append(elemento2)
    return nueva_lista

# Ejemplo 
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
nueva_lista = intercalar_listas(lista1, lista2)
print("Nueva lista intercalada:", nueva_lista)

#15
def promedio(lista):
    suma = sum(lista)
    return suma / len(lista)

# Ejemplo
numeros = [10, 20, 30, 40, 50]
promedio_numeros = promedio(numeros)
print("El promedio de los números es:", promedio_numeros)
