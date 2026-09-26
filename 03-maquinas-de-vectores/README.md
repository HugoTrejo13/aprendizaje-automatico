# 📊 Enterprise SVM Lab

Bienvenido al Laboratorio Visual de Máquinas de Vectores de Soporte (SVM). 
Este proyecto proporciona una suite completa y profesional para entender la teoría y aplicación de SVM en clasificación bidimensional, implementando conceptos como **Margen Máximo**, **Vectores de Soporte**, **Soft Margin (Parámetro C)** y el **Truco del Kernel (Kernel Trick)**.

## 🏗️ Arquitectura y Diseño (Enterprise-Grade)

El código ha sido refactorizado adoptando las mejores prácticas de ingeniería de software:
- **Clean Architecture (MVC):** Separación estricta entre la generación/gestión de datos (`DataManager`), el modelado de Machine Learning (`SVMAnalyzer`) y la presentación gráfica (`InfographicRenderer`, `InteractiveLab`).
- **Programación Orientada a Objetos (OOP):** Todo está estructurado en clases coherentes.
- **Tipado Estricto (Type Hinting):** Uso intensivo del módulo `typing` de Python para robustecer la mantenibilidad y predecir posibles bugs.
- **Gestión de Errores y Logging:** Sistema de log centralizado en lugar de impresiones rudimentarias de consola.
- **CLI Robusto:** Entrada gestionada dinámicamente mediante `argparse`.

## 📂 Estructura del Proyecto

```text
03-maquinas-de-vectores/
├── main.py                     # Entrypoint principal (Wrapper CLI)
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Documentación actual
└── src/
    └── svm_lab/
        ├── __init__.py
        ├── cli.py              # Parseo de comandos (static/interactive)
        ├── config.py           # Configuración (Logging, UI Colors, Constantes)
        ├── core.py             # Dataclasses, Módulo de Datos y Wrapper de scikit-learn
        └── visuals.py          # Lógica Matplotlib (OOP, Vista Dinámica y Estática)
```

## 🚀 Instalación

1. **Activar tu entorno virtual** (si aplica):
   ```bash
   source .venv/bin/activate
   ```
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Uso

Este paquete CLI soporta dos modos de operación principales:

### 1. Infografía Estática (Predeterminado)
Genera una gráfica de 4 paneles altamente didáctica que resume los pilares de SVM y guarda una copia PNG (`svm_explicacion_visual.png`).

```bash
python main.py static
```

*Opciones extras:*
- `--save <ruta>`: Especifica dónde guardar la imagen generada.
- `--no-show`: Útil en CI/CD o pruebas headless donde no se desea renderizar una ventana interactiva.

### 2. Laboratorio Interactivo
Lanza un dashboard de Matplotlib en vivo que permite experimentar manipulando Sliders para el parámetro $C$, e interruptores para distintos Datasets y Kernels.

```bash
python main.py interactive
```

## 🧠 Valor Educativo
Esta herramienta demuestra que variar el parámetro `C` en un Kernel Lineal **no** vuelve a la línea curva, sino que flexibiliza el margen de clasificación. A su vez, ilustra cómo el **Kernel Gaussiano (RBF)** transforma los ejes sin cálculo explícito en N-dimensiones para lograr separaciones no lineales en 2D.
