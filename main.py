# main.py

from peliculas_utils import (
    pedir_lista_peliculas, bubble_sort_peliculas, merge_sort_peliculas,
    quicksort_peliculas, linear_search_peliculas, binary_search_peliculas,
    guardar_ordenamiento_en_archivo
)

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
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
