# main.py

from peliculas_utils import (
    pedir_lista_peliculas, bubble_sort_peliculas, merge_sort_peliculas,
    quicksort_peliculas, linear_search_peliculas, binary_search_peliculas,
    guardar_ordenamiento_en_archivo
)

import time  # Importamos el modulo 'time' para poder medir cuanto tarda cada proceso (ordenar y buscar)

def ejecutar_ejemplo_lista_larga():
    print("\n=== EJEMPLO CON LISTA LARGA ===")  # Indicamos el inicio de este ejemplo especial
    print(" Generando automáticamente 100 películas...")  # Le informamos al usuario lo que vamos a hacer

    # Generamos una lista con 100 peliculas. Cada pelicula es un diccionario con titulo, año y director.
    # El titulo va de 'Pelicula 001' a 'Pelicula 100'
    # El año va de 1980 y 2019
    # El director va de la A-Z 
    peliculas = [
        {"titulo": f"Pelicula {i+1:03}", "anio": 1980 + (i % 40), "director": f"Director {chr(65 + i % 26)}"}
        for i in range(100)
    ]

    # Definimos con que clave/dato vamos a trabajar: en este caso, el 'titulo' de las peliculas
    clave = "titulo"

    print(" Por el tamaño de la lista, se ordenará automáticamente con QuickSort.")  # Le explicamos al usuario por qué QuickSort

    # MEDICIÓN DEL TIEMPO DE ORDENAMIENTO
    start_sort = time.time()  # Empezamos a contar el tiempo antes de ordenar

    # Ordenamos la lista usando QuickSort (definido en peliculas_utils.py), guardamos:
    # la lista ordenada
    # los pasos
    # la cantidad de comparaciones
    # la cantidad de intercambios realizados
    ordenadas, pasos, comps, intercambios = quicksort_peliculas(peliculas, clave)

    end_sort = time.time()  # Terminamos de contar el tiempo
    tiempo_sort = end_sort - start_sort  # Calculamos cuanto tiempo tarda el proceso de ordenamiento

    # Mostramos las primeras 10 peliculas ordenadas, como una vista previa (elegimos que sean 10 ya que la lista entera es muy larga)
    print(f"\n Primeras 10 películas ordenadas por {clave}:")
    for i, p in enumerate(ordenadas[:10]):
        print(f"{i+1}. {p['titulo']} ({p['anio']}) - {p['director']}")

    # vamos a mostrar cuantas comparaciones e intercambios se hicieron al ordenar
    print(f"\nComparaciones: {comps} | Intercambios: {intercambios}")

    print("\n Ahora se buscará una película con búsqueda binaria (Pelicula 050)...")  # Informamos qué va a hacer el programa ahora

    # MEDICIÓN DEL TIEMPO DE BÚSQUEDA
    start_search = time.time()  # Empezamos a contar el tiempo antes de buscar

    # Realizamos la busqueda binaria sobre la lista ordenada.
    # Buscamos la pelicula 'Pelicula 050'
    # Nos devuelve el índice donde está, los pasos realizados y la cantidad de comparaciones
    idx, pasos_busq, comps_busq = binary_search_peliculas(ordenadas, "Pelicula 050", clave)

    end_search = time.time()  # Finalizamos la medición de tiempo
    tiempo_search = end_search - start_search  # Calculamos cuanto tarda la busqueda

    # Si se encontró la película, el programa la mostrara completa; si no, indicara que no fue hallada
    if idx != -1:
        peli = ordenadas[idx]
        print(f"\n Película encontrada: {peli['titulo']} ({peli['anio']}) - {peli['director']}")
    else:
        print("\n Película no encontrada.")

    # tambien vamos a mostramos cuantas comparaciones fueron necesarias en la busqueda
    print(f"Comparaciones en búsqueda: {comps_busq}")

    # Mostramos el detalle de los pasos realizados durante la búsqueda
    print("Pasos del algoritmo:")
    for paso in pasos_busq:
        print(paso)

    # POR ULTIMO PASAMOS A UN RESUMEN FINAL: esta parte nos parecio importante para explicar por qué elegimos QuickSort y búsqueda binaria en este caso
    print("\n RESUMEN:")
    print("Se ordenó con el método QuickSort porque la lista es muy grande (100 elementos),")
    print("lo cual lo hace más eficiente que otros algoritmos como Bubble Sort.")
    print("Se realizó la búsqueda con el método binario porque es más rápido que la búsqueda lineal en listas ordenadas.")

    # Finalmente, mostramos cuánto tiempo tardó cada uno de los dos procesos (ordenar y buscar)
    print(f"\n Tiempo de ordenamiento: {tiempo_sort:.6f} segundos")
    print(f" Tiempo de búsqueda: {tiempo_search:.6f} segundos")


def mostrar_peliculas(lista):
    print("\nLista de películas:")
    for i, p in enumerate(lista):
        print(f"{i+1}. {p['titulo']} ({p['anio']}) - {p['director']}")

def explicar_bubble_sort():
    print("""
--- Bubble Sort (Ordenamiento Burbuja) ---
Compara elementos de a dos y los intercambia si están en el orden incorrecto. 
Repite este proceso hasta que la lista esté ordenada.
Es fácil de entender pero lento para listas grandes.
""")

def explicar_merge_sort():
    print("""
--- Merge Sort (Ordenamiento por mezcla) ---
Divide la lista en partes más pequeñas, las ordena por separado y luego las une.
Es eficiente incluso para listas grandes, aunque usa más memoria.
""")

def explicar_quicksort():
    print("""
--- QuickSort ---
Elige un elemento pivote, separa los menores y mayores, y repite el proceso en cada grupo.
Muy rápido en la práctica, aunque depende de la elección del pivote.
""")

def explicar_binary_search():
    print("""
--- Búsqueda Binaria ---
Requiere que la lista esté ordenada por el campo que se va a buscar.
Compara el elemento buscado con el del medio y va descartando la mitad en cada paso.
Es muy eficiente para listas grandes.
""")

def elegir_clave():
    print("\n¿Según qué campo deseas ordenar o buscar?")
    print("1. Título")
    print("2. Año")
    print("3. Director")
    clave_op = input("Opción: ")
    if clave_op == "1":
        return "titulo"
    elif clave_op == "2":
        return "anio"
    elif clave_op == "3":
        return "director"
    else:
        print("Opción inválida. Usando 'titulo' por defecto.")
        return "titulo"

def menu():
    lista = []
    ordenada = []
    ultimo_metodo = ""
    ultima_clave = ""
    while True:
        print("\n=== Menú de Películas ===")
        print("1. Ingresar lista de películas")
        print("2. Ordenar películas")
        print("3. Buscar película")
        print("4. Guardar último resultado de ordenación")
        print("5. Ejecutar ejemplo con lista larga (100 películas precargadas)")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            lista = pedir_lista_peliculas()
            mostrar_peliculas(lista)
        elif opcion == "2":
            if not lista:
                print("Primero ingresa una lista de películas.")
                continue
            print("\nElige el método de ordenamiento:")
            print("1. Bubble Sort")
            print("2. Merge Sort")
            print("3. QuickSort")
            metodo = input("Opción: ")
            clave = elegir_clave()
            if metodo == "1":
                explicar_bubble_sort()
                ordenada, pasos, comps, intercambios = bubble_sort_peliculas(lista, clave)
                metodo_nombre = "Bubble Sort"
            elif metodo == "2":
                explicar_merge_sort()
                ordenada, pasos, comps, intercambios = merge_sort_peliculas(lista, clave)
                metodo_nombre = "Merge Sort"
            elif metodo == "3":
                explicar_quicksort()
                ordenada, pasos, comps, intercambios = quicksort_peliculas(lista, clave)
                metodo_nombre = "QuickSort"
            else:
                print("Opción inválida.")
                continue
            print(f"\nPelículas ordenadas por {clave}:")
            mostrar_peliculas(ordenada)
            print(f"\nComparaciones: {comps}, Intercambios: {intercambios}")
            print("Pasos principales del algoritmo:")
            for i, paso in enumerate(pasos):
                print(f"Paso {i+1}: {paso}")
            # Guardamos último resultado y datos para poder escribir a archivo si el usuario quiere
            ultimo_metodo = metodo_nombre
            ultima_clave = clave
        elif opcion == "3":
            if not lista:
                print("Primero ingresa una lista de películas.")
                continue
            print("\nElige el tipo de búsqueda:")
            print("1. Búsqueda lineal")
            print("2. Búsqueda binaria (requiere lista ordenada)")
            tipo_busq = input("Opción: ")
            clave = elegir_clave()
            valor = input(f"¿Qué {clave} deseas buscar? ")
            if tipo_busq == "1":
                idx, pasos, comps = linear_search_peliculas(lista, valor, clave)
                if idx != -1:
                    print(f"\n¡Película encontrada: {lista[idx]}")
                else:
                    print("\nPelícula no encontrada.")
                print(f"Comparaciones: {comps}")
                print("Pasos del algoritmo:")
                for paso in pasos:
                    print(paso)
            elif tipo_busq == "2":
                explicar_binary_search()
                # Aseguramos que la lista esté ordenada por el campo elegido
                ordenada, _, _, _ = bubble_sort_peliculas(lista, clave)
                idx, pasos, comps = binary_search_peliculas(ordenada, valor, clave)
                if idx != -1:
                    print(f"\n¡Película encontrada: {ordenada[idx]}")
                else:
                    print("\nPelícula no encontrada.")
                print(f"Comparaciones: {comps}")
                print("Pasos del algoritmo:")
                for paso in pasos:
                    print(paso)
            else:
                print("Opción inválida.")
        elif opcion == "4":
            if not ordenada or not ultimo_metodo or not ultima_clave:
                print("Primero debes ordenar una lista.")
                continue
            guardar_ordenamiento_en_archivo(ordenada, ultima_clave, ultimo_metodo)
        elif opcion == "5":
            ejecutar_ejemplo_lista_larga()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
