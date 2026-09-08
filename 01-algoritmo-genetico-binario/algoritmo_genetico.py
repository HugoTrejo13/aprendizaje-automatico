import random

BITS = 6
POBLACION = 10
GENERACIONES = 25
PROB_CRUCE = 0.8
PROB_MUTACION = 0.05

def decodificar(cromosoma):
    cadena = "".join(str(bit) for bit in cromosoma)
    return int(cadena, 2)

def calcular_fitness(cromosoma):
    x = decodificar(cromosoma)
    return x ** 2

def cruzar(p1, p2):
    if random.random() < PROB_CRUCE:
        corte = random.randint(1, BITS - 1)
        return p1[:corte] + p2[corte:], p2[:corte] + p1[corte:]
    return p1.copy(), p2.copy()

def mutar(cromosoma):
    hijo_mutado = []
    for bit in cromosoma:
        if random.random() < PROB_MUTACION:
            hijo_mutado.append(1 - bit)
        else:
            hijo_mutado.append(bit)
    return hijo_mutado

poblacion = [[random.randint(0, 1) for _ in range(BITS)] for _ in range(POBLACION)]

for gen in range(GENERACIONES):
    fitnesses = [calcular_fitness(ind) for ind in poblacion]
    
    max_fit = max(fitnesses)
    indice_mejor = fitnesses.index(max_fit)
    mejor_actual = poblacion[indice_mejor].copy()
    
    nueva_poblacion = [mejor_actual]
    
    while len(nueva_poblacion) < POBLACION:
        padre1 = random.choices(poblacion, weights=fitnesses)[0]
        padre2 = random.choices(poblacion, weights=fitnesses)[0]
        
        hijo1, hijo2 = cruzar(padre1, padre2)
        
        nueva_poblacion.append(mutar(hijo1))
        
        if len(nueva_poblacion) < POBLACION:
            nueva_poblacion.append(mutar(hijo2))
            
    poblacion = nueva_poblacion

fitnesses = [calcular_fitness(ind) for ind in poblacion]
mejor_ind = poblacion[fitnesses.index(max(fitnesses))]
mejor_x = decodificar(mejor_ind)
mejor_fitness = calcular_fitness(mejor_ind)

print("--- RESULTADO DEL ALGORITMO GENETICO ---")
print("Mejor individuo:", mejor_ind)
print("Valor de x encontrado:    ", mejor_x)
print("Fitness f(x) = x^2:        ", mejor_fitness)
print("Optimo teorico buscado:    63 (f(63) = 3969)")
