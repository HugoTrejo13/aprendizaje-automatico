"""
Módulo de Presentación: Visualizaciones Estáticas e Interactivas.
Responsable exclusivamente de la interfaz gráfica usando Matplotlib (MVC: View).
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from matplotlib.lines import Line2D

from .config import Colors, setup_plot_style, logger
from .core import DataManager, SVMAnalyzer, Dataset

class InfographicRenderer:
    """Clase responsable de renderizar la infografía educativa estática de 4 paneles."""
    
    def __init__(self):
        setup_plot_style()
        self.fig, self.axes = plt.subplots(2, 2, figsize=(16, 12))
        self.fig.suptitle(
            "MÁQUINAS DE VECTORES DE SOPORTE (SVM) - GUÍA VISUAL COMPLETA\n"
            "De la Intuición Geométrica (Triángulos vs Cuadrados) al Hiperplano Óptimo y el Kernel",
            fontsize=16, fontweight="bold", y=0.98
        )

    def _plot_dataset(self, ax, dataset: Dataset):
        """Grafica los puntos base del dataset."""
        ax.scatter(dataset.X[dataset.y == 1, 0], dataset.X[dataset.y == 1, 1], 
                   marker="^", s=95, color=Colors.TRIANGLE, edgecolors="k", linewidth=1.2, label="Triángulos")
        ax.scatter(dataset.X[dataset.y == -1, 0], dataset.X[dataset.y == -1, 1], 
                   marker="s", s=85, color=Colors.SQUARE, edgecolors="k", linewidth=1.2, label="Cuadrados")

    def _draw_decision_boundary(self, ax, analyzer: SVMAnalyzer, X: np.ndarray, colors_contour: list):
        """Dibuja la frontera, los márgenes y resalta los vectores de soporte."""
        x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
        y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))
        
        Z = analyzer.get_decision_boundary(xx, yy)
        
        # Franja de margen
        ax.contourf(xx, yy, Z, levels=[-1, 1], colors=[colors_contour[0]], alpha=0.85)
        # Líneas
        ax.contour(xx, yy, Z, levels=[-1, 0, 1], colors=[colors_contour[1], colors_contour[2], colors_contour[1]],
                   linestyles=["--", "-", "--"], linewidths=[2, 2.8, 2])
        
        # Vectores de soporte
        sv = analyzer.get_support_vectors()
        ax.scatter(sv[:, 0], sv[:, 1], s=200, facecolors="none", edgecolors=Colors.SUPPORT_VECTOR, 
                   linewidth=2.2, label=f"Vectores ({len(sv)})")

    def render_panel_1(self, ax):
        """Renderiza el Panel 1: Infinitas Líneas."""
        dataset = DataManager.get_separable_data()
        self._plot_dataset(ax, dataset)
        
        p_nuevo = np.array([[3.35, 2.2]])
        ax.scatter(p_nuevo[0, 0], p_nuevo[0, 1], marker="o", s=170, color=Colors.NEW_DATA, edgecolors="black", zorder=5)
        ax.annotate("¿Triángulo o\nCuadrado?", xy=(p_nuevo[0, 0], p_nuevo[0, 1]), xytext=(p_nuevo[0, 0] - 1.4, p_nuevo[0, 1] + 0.7),
                    arrowprops=dict(facecolor="black", shrink=0.08, width=1.5, headwidth=7),
                    fontsize=10, fontweight="bold", bbox=dict(boxstyle="round", facecolor="#d5f5e3", edgecolor=Colors.NEW_DATA))

        x_vals = np.linspace(0.8, 5.8, 200)
        ax.plot(x_vals, 0.82 * x_vals - 0.45, color="#e67e22", linestyle="--", linewidth=2.2, label="Línea 1")
        ax.plot(x_vals, 1.75 * x_vals - 4.10, color="#8e44ad", linestyle=":", linewidth=2.5, label="Línea 2")
        ax.plot(x_vals, 0.38 * x_vals + 1.25, color="#16a085", linestyle="-.", linewidth=2.2, label="Línea 3")

        ax.set_title("1. El Dilema: Infinitas Líneas Válidas", fontsize=12, fontweight="bold")
        ax.legend(loc="upper left", fontsize=8.5)

    def render_panel_2(self, ax):
        """Renderiza el Panel 2: Margen Máximo SVM."""
        dataset = DataManager.get_separable_data()
        analyzer = SVMAnalyzer(kernel="linear", C=100.0)
        analyzer.train(dataset)
        
        self._plot_dataset(ax, dataset)
        self._draw_decision_boundary(ax, analyzer, dataset.X, ["#fef9e7", "#7f8c8d", "#2c3e50"])
        ax.set_title("2. Margen Máximo y Vectores de Soporte", fontsize=12, fontweight="bold")
        ax.legend(loc="upper left", fontsize=8.5)

    def render_panel_3(self, ax):
        """Renderiza el Panel 3: Soft Margin."""
        dataset = DataManager.get_overlapping_data()
        analyzer = SVMAnalyzer(kernel="linear", C=0.5)
        analyzer.train(dataset)
        
        self._plot_dataset(ax, dataset)
        self._draw_decision_boundary(ax, analyzer, dataset.X, ["#ebf5fb", "#2980b9", "#1b4f72"])
        
        # Hard margin para comparar
        hard_analyzer = SVMAnalyzer(kernel="linear", C=100.0)
        hard_analyzer.train(dataset)
        x_min, x_max = dataset.X[:, 0].min() - 0.5, dataset.X[:, 0].max() + 0.5
        y_min, y_max = dataset.X[:, 1].min() - 0.5, dataset.X[:, 1].max() + 0.5
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
        Z_hard = hard_analyzer.get_decision_boundary(xx, yy)
        ax.contour(xx, yy, Z_hard, levels=[0], colors=["#e74c3c"], linestyles=["-."], linewidths=[2.2])
        
        custom_lines = [
            Line2D([0], [0], color="#1b4f72", lw=2.5, label="C=0.5 (Tolerante)"),
            Line2D([0], [0], color="#e74c3c", lw=2.2, linestyle="-.", label="C=100 (Estricto)")
        ]
        handles, _ = ax.get_legend_handles_labels()
        ax.legend(handles=handles + custom_lines, loc="upper left", fontsize=8.2)
        ax.set_title("3. Datos Solapados: El Parámetro C", fontsize=12, fontweight="bold")

    def render_panel_4(self, ax):
        """Renderiza el Panel 4: Truco del Kernel RBF."""
        dataset = DataManager.get_circular_data()
        analyzer = SVMAnalyzer(kernel="rbf", C=10.0)
        analyzer.train(dataset)
        
        self._plot_dataset(ax, dataset)
        self._draw_decision_boundary(ax, analyzer, dataset.X, ["#fef5e7", "#d35400", "#962d00"])
        ax.set_title("4. El Truco del Kernel (RBF)", fontsize=12, fontweight="bold")
        ax.legend(loc="upper left", fontsize=8.5)

    def generate(self, save_path: str = None, show: bool = True):
        """Construye y exporta la visualización."""
        logger.info("Renderizando paneles...")
        self.render_panel_1(self.axes[0, 0])
        self.render_panel_2(self.axes[0, 1])
        self.render_panel_3(self.axes[1, 0])
        self.render_panel_4(self.axes[1, 1])
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            logger.info(f"Infografía guardada en: {save_path}")
            
        if show:
            plt.show()

class InteractiveLab:
    """Laboratorio en tiempo real usando Widgets de Matplotlib."""
    
    def __init__(self):
        setup_plot_style()
        self.datasets = DataManager.get_all_datasets()
        
        self.fig = plt.figure(figsize=(14, 8))
        plt.subplots_adjust(left=0.08, bottom=0.22, right=0.72, top=0.90)
        self.ax_main = self.fig.add_subplot(111)
        
        # Controles
        self.ax_slider_c = plt.axes([0.15, 0.08, 0.50, 0.03])
        self.ax_radio_kernel = plt.axes([0.76, 0.55, 0.20, 0.25], facecolor="#f8f9f9")
        self.ax_radio_data = plt.axes([0.76, 0.20, 0.20, 0.25], facecolor="#f8f9f9")
        
        self.slider_c = Slider(self.ax_slider_c, "log10(C)", -2.0, 3.0, valinit=1.0, valstep=0.1)
        self.radio_kernel = RadioButtons(self.ax_radio_kernel, ("linear", "rbf", "poly"), active=0)
        self.radio_data = RadioButtons(self.ax_radio_data, list(self.datasets.keys()), active=0)
        
        self.slider_c.on_changed(self._update)
        self.radio_kernel.on_clicked(self._update)
        self.radio_data.on_clicked(self._update)
        
    def _update(self, val=None):
        self.ax_main.clear()
        c_val = 10 ** self.slider_c.val
        kernel = self.radio_kernel.value_selected
        dataset = self.datasets[self.radio_data.value_selected]
        
        analyzer = SVMAnalyzer(kernel=kernel, C=c_val)
        analyzer.train(dataset)
        
        # Puntos
        self.ax_main.scatter(dataset.X[dataset.y == 1, 0], dataset.X[dataset.y == 1, 1], marker="^", s=90, color=Colors.TRIANGLE, edgecolors="k", label="Triángulos")
        self.ax_main.scatter(dataset.X[dataset.y == -1, 0], dataset.X[dataset.y == -1, 1], marker="s", s=80, color=Colors.SQUARE, edgecolors="k", label="Cuadrados")
        
        # Superficie
        x_min, x_max = dataset.X[:, 0].min() - 0.7, dataset.X[:, 0].max() + 0.7
        y_min, y_max = dataset.X[:, 1].min() - 0.7, dataset.X[:, 1].max() + 0.7
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
        
        try:
            Z = analyzer.get_decision_boundary(xx, yy)
            self.ax_main.contourf(xx, yy, Z, levels=[-1, 1], colors=["#fef9e7"], alpha=0.85)
            self.ax_main.contour(xx, yy, Z, levels=[-1, 0, 1], colors=["#7f8c8d", "#2c3e50", "#7f8c8d"], linestyles=["--", "-", "--"], linewidths=[2, 3, 2])
        except Exception:
            pass # Tolerancia ante fallos matemáticos al inicio
            
        sv = analyzer.get_support_vectors()
        self.ax_main.scatter(sv[:, 0], sv[:, 1], s=220, facecolors="none", edgecolors=Colors.SUPPORT_VECTOR, linewidth=2.5, label=f"Vectores ({len(sv)})")
        
        acc = analyzer.get_accuracy(dataset)
        self.ax_main.set_xlim(x_min, x_max)
        self.ax_main.set_ylim(y_min, y_max)
        self.ax_main.set_title(f"SVM Interactivo | Dataset: {dataset.name} | Kernel: '{kernel}' | C = {c_val:.3f} | Exactitud: {acc:.1f}%", fontweight="bold")
        self.ax_main.legend(loc="upper left")
        self.fig.canvas.draw_idle()

    def launch(self, show: bool = True):
        """Inicia el dashboard interactivo."""
        logger.info("Iniciando Laboratorio Interactivo...")
        self._update()
        if show:
            plt.show()
