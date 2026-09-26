#!/usr/bin/env python3
"""
Punto de Entrada Principal - Laboratorio de SVM (Enterprise Edition)
"""
import sys
import os

# Asegurar que la ruta src/ está en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from svm_lab.cli import main

if __name__ == "__main__":
    main()
