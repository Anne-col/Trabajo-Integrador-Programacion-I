﻿# Proyecto: Algoritmos de Búsqueda y Ordenamiento con Películas (Python)

Este proyecto es una aplicación educativa por consola que permite experimentar, visualizar y comparar **algoritmos de ordenamiento** y **búsqueda** sobre una lista de películas en Python puro, **con soporte para guardar los resultados y realizar búsqueda binaria**.

---

## 📋 Descripción

El programa permite:

* **Ingresar películas** por título, año y director.
* Ordenar la lista usando **Bubble Sort**, **Merge Sort** y **QuickSort** por el campo que elijas (título, año o director).
* Buscar una película usando **búsqueda lineal** o **búsqueda binaria**.
* **Visualizar y explicar cada algoritmo** con pasos, comparaciones y swaps/intercambios.
* **Guardar los resultados de la ordenación** en un archivo de texto dentro de la carpeta `resultados/`.

---

## 📁 Estructura del proyecto

```
busqueda_peliculas/
├── main.py
├── peliculas_utils.py
├── resultados/
│   └── (aquí se guardan los resultados de las ordenaciones)
└── README.md
```

---

## 🚀 Cómo ejecutar el proyecto

1. Descarga o clona este repositorio.
2. Ubica todos los archivos en la misma carpeta.
3. Asegúrate de tener **Python 3** instalado.
4. Abre la terminal y ejecuta:

   ```bash
   python main.py
   ```
5. Sigue el **menú interactivo**.

---

## 🖥️ Menú de ejemplo

```
=== Menú de Películas ===
1. Ingresar lista de películas
2. Ordenar películas
3. Buscar película
4. Guardar último resultado de ordenación
0. Salir
Elige una opción:
```

---

## 🔍 Métodos disponibles

### Ordenamiento

* **Bubble Sort:** Explicado antes de ejecutar; compara e intercambia elementos adyacentes.
* **Merge Sort:** Divide y combina sublistas ordenadas.
* **QuickSort:** Usa pivote y particiones recursivas.
* Puedes ordenar por **título**, **año** o **director**.

### Búsqueda

* **Lineal:** Recorre la lista desde el inicio hasta encontrar el elemento.
* **Binaria:** Requiere lista ordenada; compara con el medio y descarta mitades.

---

## 💾 Guardado de resultados

* Después de realizar una ordenación, elige la opción `4` para **guardar el resultado** en la carpeta `resultados/`.
* El archivo generado tendrá un nombre del estilo `orden_bubble_sort_por_titulo.txt`.

---

## 📑 Ejemplo de guardado

Después de ordenar por título con Bubble Sort, se guardará algo como:

```
Películas ordenadas por titulo usando Bubble Sort:
1. El Padrino (1972) - Francis Ford Coppola
2. Interestelar (2014) - Christopher Nolan
3. Pulp Fiction (1994) - Quentin Tarantino
```

---

## 📚 Referencias y fuentes consultadas

* Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms.
* [Documentación oficial de Python](https://docs.python.org)
* [GeeksForGeeks](https://www.geeksforgeeks.org)
* Notas de cátedra UTN

---

## Video explicativo en YouTube

- [Video explicativo en YouTube](https://www.youtube.com/watch?v=CfZ9XJE4VgA)

---

## 👨‍💻 Autoría

Trabajo desarrollado por Eliud Campos y Rebeca Coletti para la cátedra de Programación I - UTN.

