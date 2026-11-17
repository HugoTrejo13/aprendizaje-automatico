from sklearn.svm import SVC #Support Vector Classifier # sklearn análisis predictivo de datos

historial = [
    ("Tachi",    45,  5, 1), ("Luis",   38, 10, 1), ("Sofía",  30,  8, 1),
    ("Pedro",  50, 15, 1), ("María",  28,  4, 1), ("Bello",  35, 12, 1),
    ("Carlos", 12, 25, 0), ("Elena",  15, 30, 0), ("Tacho",    8, 10, 0),
    ("Diana",  20, 28, 0), ("Tomás",  10, 20, 0), ("Lucía",  18, 22, 0),
]

X = []#lista entrada del modelo, ingreso deuda

y = []#lista entrada del modelo, 0 y 1, aprobado/rechazado

print("Clientes anteriores del banco:")

for i in range(0, len(historial)):
    cliente = historial[i]
    nombre = cliente[0]
    ingreso = cliente[1]
    deuda = cliente[2]
    aprobado = cliente[3]

    X.append([ingreso, deuda])
    y.append(aprobado)

    if (aprobado == 1):
        resultado = "APROBADO"
    else:
        resultado = "RECHAZADO"

    print("  " + nombre + ": ingreso " + str(ingreso) + " mil, deuda " + str(deuda) + " mil -> " + resultado)

# C=1: qué tan estricto es con los errores; C más alto = menos errores, pero margen más angosto.
# fit(X, y): entrena el modelo; aprende de los ejemplos la línea con el mayor margen entre las dos clases.
modelo = SVC(kernel="linear", C=1)
modelo.fit(X, y)

continuar = True

while (continuar == True):
    nombre = input("\nTú nombre: ")

    if (nombre.lower() == "salir"):
        continuar = False
    else:
        ingreso = float(input("Cual es tu ingreso mensual ? "))
        deuda = float(input("Cuánta deuda tienes ? "))

        # predict(): clase del cliente (1 = aprobado, 0 = rechazado); devuelve una lista, por eso el [0].
        aprobado = modelo.predict([[ingreso, deuda]])[0]
        # decision_function(): distancia con signo a la línea (+ aprobado, − rechazado); más lejos = más seguro.
        distancia = modelo.decision_function([[ingreso, deuda]])[0]

        if (aprobado == 1):
            resultado = "APROBADA"
        else:
            resultado = "RECHAZADA"

        if (abs(distancia) > 1):
            seguridad = "segura"
        else:
            seguridad = "dudosa (estás cerca de la línea)"

        print(nombre + ", tu tarjeta está " + resultado + ". Decisión " + seguridad + ".")
