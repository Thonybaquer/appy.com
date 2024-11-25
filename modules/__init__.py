"""Inicialización del paquete modules."""
from .animation_engine import graficar_funcion
from .calculos import (
    suma, resta, multiplicacion, division,
    resolver_ecuacion, calcular_media, calcular_varianza
)
from .busqueda import buscar
from .seguridad import autenticar_usuario
from .exportacion import exportar_a_excel

__all__ = [
    'graficar_funcion',
    'suma', 'resta', 'multiplicacion', 'division',
    'resolver_ecuacion', 'calcular_media', 'calcular_varianza',
    'buscar', 'autenticar_usuario', 'exportar_a_excel'
]
