"""
Módulos de Dominio: Gestión de Datos y Modelado SVM.
Implementa el patrón de repositorio para los datos y un wrapper tipado para SVC.
"""
import numpy as np
from dataclasses import dataclass
from typing import Tuple, Dict
from sklearn.svm import SVC
from sklearn.datasets import make_blobs, make_circles

@dataclass
class Dataset:
    """Estructura de datos tipada para características y etiquetas."""
    X: np.ndarray
    y: np.ndarray
    name: str

class DataManager:
    """Gestor encargado de la generación y provisión de datos sintéticos."""
    
    @staticmethod
    def get_separable_data() -> Dataset:
        np.random.seed(42)
        X_tri = np.random.randn(20, 2) * 0.55 + [2.2, 3.4]
        X_sqr = np.random.randn(20, 2) * 0.55 + [4.6, 1.2]
        X = np.vstack([X_tri, X_sqr])
        y = np.array([1]*len(X_tri) + [-1]*len(X_sqr))
        return Dataset(X=X, y=y, name="Triángulos vs Cuadrados")

    @staticmethod
    def get_overlapping_data() -> Dataset:
        np.random.seed(15)
        X, y_raw = make_blobs(n_samples=55, centers=[[2.5, 3.1], [3.9, 2.1]], cluster_std=0.78, random_state=10)
        y = np.where(y_raw == 0, 1, -1)
        return Dataset(X=X, y=y, name="Datos Solapados")

    @staticmethod
    def get_circular_data() -> Dataset:
        X, y_raw = make_circles(n_samples=130, factor=0.42, noise=0.11, random_state=42)
        X = X * 2.0 + [3.0, 3.0] # Escalar para mantener ejes positivos
        y = np.where(y_raw == 0, 1, -1)
        return Dataset(X=X, y=y, name="Círculos Concéntricos")

    @classmethod
    def get_all_datasets(cls) -> Dict[str, Dataset]:
        """Devuelve un diccionario con todos los conjuntos de datos disponibles."""
        return {
            "1. Triángulos vs Cuadrados": cls.get_separable_data(),
            "2. Datos Solapados": cls.get_overlapping_data(),
            "3. Círculos Concéntricos": cls.get_circular_data()
        }

class SVMAnalyzer:
    """Wrapper encapsulado para el modelo SVC de scikit-learn con validación."""
    
    def __init__(self, kernel: str = 'linear', C: float = 1.0):
        self.kernel = kernel
        self.C = C
        self.model = SVC(kernel=self.kernel, C=self.C, gamma="scale", degree=3)
        self.is_fitted = False

    def train(self, dataset: Dataset) -> None:
        """Entrena el clasificador con los datos proporcionados."""
        self.model.fit(dataset.X, dataset.y)
        self.is_fitted = True

    def get_decision_boundary(self, xx: np.ndarray, yy: np.ndarray) -> np.ndarray:
        """Calcula la superficie de decisión para una malla generada."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser entrenado antes de calcular la frontera.")
        xy = np.c_[xx.ravel(), yy.ravel()]
        return self.model.decision_function(xy).reshape(xx.shape)

    def get_support_vectors(self) -> np.ndarray:
        """Retorna las coordenadas de los vectores de soporte."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser entrenado primero.")
        return self.model.support_vectors_

    def get_accuracy(self, dataset: Dataset) -> float:
        """Retorna la exactitud (accuracy) del modelo sobre los datos."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser entrenado primero.")
        return self.model.score(dataset.X, dataset.y) * 100
