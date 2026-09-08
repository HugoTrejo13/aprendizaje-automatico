# Algoritmo Genético Binario

### ¿Qué es el algoritmo?
Es un método de optimización heurístico inspirado en la teoría de la evolución biológica y la selección natural de Darwin.
Trabaja con una población de cromosomas binarios que evolucionan a través de selección por ruleta, cruce y mutación para obtener mejores soluciones.

### ¿Qué problema resuelve?
Resuelve la maximización de la función matemática $f(x) = x^2$ sobre enteros codificados en cadenas binarias de 6 bits ($x \in [0, 63]$).
Permite converger de manera rápida hacia el óptimo global ($x = 63, f(63) = 3969$) sin recurrir a derivadas ni evaluar todo el espacio de búsqueda.

### ¿Para qué se usa?
Se utiliza para encontrar soluciones óptimas o aproximadas en problemas complejos de búsqueda combinatoria y optimización no lineal.
Es común en ingeniería y machine learning para ajuste de hiperparámetros, diseño de rutas y selección de características.

