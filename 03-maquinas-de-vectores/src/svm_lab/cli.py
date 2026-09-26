"""
Interfaz de Línea de Comandos (CLI) usando argparse.
"""
import argparse
import sys
import os

from .config import logger
from .visuals import InfographicRenderer, InteractiveLab

def parse_args():
    parser = argparse.ArgumentParser(
        description="SVM Enterprise Lab: Laboratorio visual interactivo de Máquinas de Vectores de Soporte."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando Estático
    static_parser = subparsers.add_parser("static", help="Genera la infografía visual de 4 paneles.")
    static_parser.add_argument("--save", type=str, default="svm_explicacion_visual.png", help="Ruta de guardado del PNG.")
    static_parser.add_argument("--no-show", action="store_true", help="Si se especifica, no despliega la GUI (útil para CI/CD).")

    # Comando Interactivo
    interactive_parser = subparsers.add_parser("interactive", help="Abre el dashboard de experimentación en tiempo real.")
    interactive_parser.add_argument("--no-show", action="store_true", help="Validación de ejecución (Testing).")

    return parser.parse_args()

def main():
    args = parse_args()

    # Fallback si no hay comandos
    if args.command is None:
        logger.info("No se proporcionó un comando. Ejecutando la vista 'static' por defecto. Usa -h para ayuda.")
        args.command = "static"
        args.save = "svm_explicacion_visual.png"
        args.no_show = False

    if args.command == "static":
        logger.info("Configurando infografía estática...")
        renderer = InfographicRenderer()
        renderer.generate(save_path=args.save, show=not args.no_show)
        
    elif args.command == "interactive":
        logger.info("Configurando laboratorio interactivo...")
        lab = InteractiveLab()
        lab.launch(show=not args.no_show)

if __name__ == "__main__":
    main()
