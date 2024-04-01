import random

def lanzar_dado(caras):
    return random.randint(1, caras)

def lanzar_dados(cantidad, caras):
    resultados = []
    for _ in range(cantidad):
        resultados.append(lanzar_dado(caras))
    return resultados

def calcular_total(resultados):
    return sum(resultados)

def calcular_estadisticas(resultados):
    estadisticas = {
        'Mínimo': min(resultados),
        'Máximo': max(resultados),
        'Promedio': sum(resultados) / len(resultados)
    }
    return estadisticas

def mostrar_resultados_lanzamiento(numero_lanzamiento, resultados, total, estadisticas, puntuacion):
    print(f"\nLanzamiento {numero_lanzamiento}: {resultados}")
    print(f"Total: {total}")
    print("Estadísticas:")
    for stat, value in estadisticas.items():
        print(f"{stat}: {value}")
    print(f"Puntuacion del lanzamiento: {puntuacion}")

print("Bienvenido al simulador de lanzamientos de dados")
caras_dado = int(input("Ingrese el numero de caras de cada dado (por ejemplo, 6 para un dado estandar): "))
cantidad_lanzamientos = int(input("Ingrese la cantidad de lanzamientos: "))

for i in range(1, cantidad_lanzamientos + 1):
    cantidad_dados = int(input(f"Ingrese la cantidad de dados a lanzar en el lanzamiento {i}: "))
    resultados = lanzar_dados(cantidad_dados, caras_dado)
    total = calcular_total(resultados)
    estadisticas = calcular_estadisticas(resultados)
    
    # Sistema de puntos básico: sumamos todos los resultados para obtener la puntuación del lanzamiento
    puntuacion = sum(resultados)
    
    mostrar_resultados_lanzamiento(i, resultados, total, estadisticas, puntuacion)