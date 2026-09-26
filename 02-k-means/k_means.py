import numpy as np
import matplotlib.pyplot as plt

K = 6
ITERACIONES = 100
rng = np.random.default_rng(42)

datos = np.vstack([rng.normal(centro, 0.6, (30, 2)) for centro in [(2, 2), (7, 3), (4, 7)]])
centroides = datos[rng.choice(len(datos), K, replace=False)]

for iteracion in range(1, ITERACIONES + 1):
    distancias = np.linalg.norm(datos[:, None] - centroides, axis=2)
    etiquetas = distancias.argmin(axis=1)
    nuevos = np.array([datos[etiquetas == k].mean(axis=0) for k in range(K)])
    if np.allclose(nuevos, centroides):
        break
    centroides = nuevos

print("--- RESULTADO DE K-MEANS ---")
print("Iteraciones hasta converger:", iteracion)
for k in range(K):
    print(f"Grupo {k}: {(etiquetas == k).sum()} puntos, centroide {centroides[k].round(2)}")

plt.scatter(datos[:, 0], datos[:, 1], c=etiquetas, cmap="viridis")
plt.scatter(centroides[:, 0], centroides[:, 1], c="red", marker="X", s=200)
plt.title("K-Means")
plt.show()
