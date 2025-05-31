# peliculas_utils.py
import os

def pedir_lista_peliculas():
    while True:
        entrada = input("¿Cuántas películas quieres ingresar? (mínimo 2): ")
        try:
            n = int(entrada)
            if n < 2:
                print(" Debes ingresar al menos 2 películas para continuar con el proceso de ordenarlas o buscarlas.")
                continue
            break
        except ValueError:
            print("  Entrada inválida. Debes ingresar un número entero.")

    lista = []
    for i in range(n):
        print(f"\nPelícula {i+1}:")
        titulo = input("  Título: ")

        while True:
            anio_str = input("  Año: ")
            if anio_str.isdigit():
                anio = int(anio_str)
                break
            else:
                print(" El año debe ser un número entero.")

        director = input("  Director: ")
        lista.append({"titulo": titulo, "anio": anio, "director": director})
    return lista

def bubble_sort_peliculas(lista, clave="titulo"):
    """
    Ordena la lista de películas usando Bubble Sort según el campo indicado.
    """
    n = len(lista)
    pasos = []
    comparaciones = 0
    intercambios = 0
    a = lista.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if str(a[j][clave]).lower() > str(a[j+1][clave]).lower():
                a[j], a[j+1] = a[j+1], a[j]
                intercambios += 1
                pasos.append([x[clave] for x in a])
    return a, pasos, comparaciones, intercambios

def merge_sort_peliculas(lista, clave="titulo"):
    """
    Ordena la lista de películas usando Merge Sort según el campo indicado.
    """
    pasos = []
    comparaciones = [0]
    intercambios = [0]

    def merge(left, right):
        resultado = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparaciones[0] += 1
            if str(left[i][clave]).lower() <= str(right[j][clave]).lower():
                resultado.append(left[i])
                i += 1
            else:
                resultado.append(right[j])
                j += 1
                intercambios[0] += 1
        resultado.extend(left[i:])
        resultado.extend(right[j:])
        pasos.append([x[clave] for x in resultado])
        return resultado

    def sort(subarr):
        if len(subarr) <= 1:
            return subarr
        mid = len(subarr) // 2
        left = sort(subarr[:mid])
        right = sort(subarr[mid:])
        return merge(left, right)

    resultado = sort(lista.copy())
    return resultado, pasos, comparaciones[0], intercambios[0]

def quicksort_peliculas(lista, clave="titulo"):
    """
    Ordena la lista de películas usando QuickSort según el campo indicado.
    """
    pasos = []
    comparaciones = [0]
    intercambios = [0]

    def sort(a):
        if len(a) <= 1:
            return a
        pivot = a[0]
        menores = []
        mayores = []
        for x in a[1:]:
            comparaciones[0] += 1
            if str(x[clave]).lower() < str(pivot[clave]).lower():
                menores.append(x)
            else:
                mayores.append(x)
        resultado = sort(menores) + [pivot] + sort(mayores)
        pasos.append([item[clave] for item in resultado])
        intercambios[0] += len(menores) + len(mayores)
        return resultado

    resultado = sort(lista.copy())
    return resultado, pasos, comparaciones[0], intercambios[0]

def linear_search_peliculas(lista, valor, clave="titulo"):
    pasos = []
    comparaciones = 0
    for i, pelicula in enumerate(lista):
        comparaciones += 1
        pasos.append(f"Comparando '{pelicula[clave]}' en posición {i}")
        if str(pelicula[clave]).lower() == str(valor).lower():
            pasos.append(f"¡Elemento '{valor}' encontrado en posición {i}!")
            return i, pasos, comparaciones
    pasos.append(f"Elemento '{valor}' no encontrado en la lista.")
    return -1, pasos, comparaciones

# Búsqueda binaria.


def binary_search_peliculas(lista, valor, clave="titulo"):
    """
    Busca un valor en la lista ordenada de películas por el campo dado usando búsqueda binaria.
    Devuelve: índice, pasos, comparaciones.
    """
    pasos = []
    comparaciones = 0
    # Es importante que la lista esté ordenada previamente por el campo clave.
    izq, der = 0, len(lista) - 1
    while izq <= der:
        mid = (izq + der) // 2
        comparaciones += 1
        pasos.append(f"Comparando '{lista[mid][clave]}' en posición {mid}")
        if str(lista[mid][clave]).lower() == str(valor).lower():
            pasos.append(f"¡Elemento '{valor}' encontrado en posición {mid}!")
            return mid, pasos, comparaciones
        elif str(lista[mid][clave]).lower() < str(valor).lower():
            pasos.append(f"'{lista[mid][clave]}' < '{valor}' → Buscar a la derecha")
            izq = mid + 1
        else:
            pasos.append(f"'{lista[mid][clave]}' > '{valor}' → Buscar a la izquierda")
            der = mid - 1
    pasos.append(f"Elemento '{valor}' no encontrado en la lista.")
    return -1, pasos, comparaciones

def guardar_ordenamiento_en_archivo(lista, clave, metodo):
    """
    Guarda el resultado de la ordenación en un archivo dentro de resultados/.
    """
    carpeta = "resultados"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    nombre_archivo = f"{carpeta}/orden_{metodo.lower().replace(' ', '_')}_por_{clave}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"Películas ordenadas por {clave} usando {metodo}:\n")
        for i, p in enumerate(lista):
            f.write(f"{i+1}. {p['titulo']} ({p['anio']}) - {p['director']}\n")
    print(f"\nResultado de la ordenación guardado en '{nombre_archivo}'.")
