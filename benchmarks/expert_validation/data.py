import numpy as np
from dataclasses import dataclass

@dataclass
class ValidationData:
    """
    Datos para validación con juicios de expertos del paper de Koudenburg et al. (2021)
    Cada distribución representa frecuencias en una escala de 1-5
    """
    # Las 15 distribuciones como array numpy
    distributions = np.array([
        [12, 20, 40, 21, 7],   # Distribución 1
        [40, 11, 28, 19, 2],   # Distribución 2
        [2, 8, 44, 9, 1],      # Distribución 3
        [20, 25, 2, 28, 25],   # Distribución 4
        [3, 11, 17, 24, 44],   # Distribución 5
        [44, 25, 16, 10, 4],   # Distribución 6
        [2, 31, 8, 29, 30],    # Distribución 7
        [7, 38, 8, 37, 10],    # Distribución 8
        [21, 19, 19, 20, 21],  # Distribución 9
        [3, 25, 44, 24, 3],    # Distribución 10
        [36, 20, 27, 11, 6],   # Distribución 11
        [1, 30, 37, 21, 11],   # Distribución 12
        [15, 21, 30, 20, 14],  # Distribución 13
        [36, 10, 8, 11, 35],   # Distribución 14
        [10, 21, 38, 29, 2],   # Distribución 15
    ])

    # Puntuaciones promedio de los expertos (0-100) para cada distribución
    expert_scores = np.array([
        16.9655,  # Distribución 1
        35.8966,  # Distribución 2
        6.6207,   # Distribución 3
        70.0517,  # Distribución 4
        26.8621,  # Distribución 5
        27.0517,  # Distribución 6
        49.5862,  # Distribución 7
        59.0517,  # Distribución 8
        28.7586,  # Distribución 9
        13.1207,  # Distribución 10
        30.5000,  # Distribución 11
        21.8103,  # Distribución 12
        22.7069,  # Distribución 13
        85.9483,  # Distribución 14
        22.8966   # Distribución 15
    ])

    def get_normalized_distributions(self):
        """Retorna las distribuciones normalizadas para sumar 100"""
        return np.array([dist / np.sum(dist) * 100 for dist in self.distributions])

    @property
    def x_values(self):
        """Valores de la escala (1-5)"""
        return np.array([1, 2, 3, 4, 5])
