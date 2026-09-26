"""
Configuración global y constantes para el Laboratorio SVM.
"""
import logging
import matplotlib.pyplot as plt

# Configuración de Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("SVM_Lab")

# Paleta de Colores Corporativa
class Colors:
    TRIANGLE = "#2980b9"  # Azul corporativo (Clase 1)
    SQUARE = "#c0392b"    # Rojo alerta (Clase -1)
    NEW_DATA = "#27ae60"  # Verde confirmación (Dato de prueba)
    SUPPORT_VECTOR = "#d35400" # Naranja destaque

# Estilos de interfaz
def setup_plot_style() -> None:
    """Configura el estilo visual de matplotlib a un estándar limpio."""
    style_name = "seaborn-v0_8-whitegrid"
    if style_name in plt.style.available:
        plt.style.use(style_name)
    else:
        plt.style.use("default")
