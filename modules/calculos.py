import sympy as sp
import numpy as np
from sklearn.linear_model import LinearRegression

def suma(a, b):
    """Suma dos números."""
    return a + b

def resta(a, b):
    """Resta dos números."""
    return a - b

def multiplicacion(a, b):
    """Multiplica dos números."""
    return a * b

def division(a, b):
    """Divide dos números, manejando la división por cero."""
    if b != 0:
        return a / b
    return "Error: División por cero"

def resolver_ecuacion(ecuacion):
    """Resuelve una ecuación dada."""
    x = sp.symbols('x')
    solucion = sp.solve(ecuacion, x)
    return solucion

def calcular_derivada(funcion):
    """Calcula la derivada de una función."""
    x = sp.symbols('x')
    derivada = sp.diff(funcion, x)
    return derivada

def calcular_integral(funcion):
    """Calcula la integral de una función."""
    x = sp.symbols('x')
    integral = sp.integrate(funcion, x)
    return integral

def calcular_limite(funcion, punto):
    """Calcula el límite de una función en un punto."""
    x = sp.symbols('x')
    limite = sp.limit(funcion, x, punto)
    return limite

def calcular_series(funcion, n):
    """Calcula la serie de Taylor de una función."""
    x = sp.symbols('x')
    serie = sp.series(funcion, x, n)
    return serie

def validar_entrada(entrada):
    """Valida si la entrada es un número."""
    try:
        float(entrada)
        return True
    except ValueError:
        return False

def calcular_media(lista):
    """Calcula la media de una lista de números."""
    return sum(lista) / len(lista) if lista else 0

def calcular_varianza(lista):
    """Calcula la varianza de una lista de números."""
    media = calcular_media(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista) if lista else 0

def calcular_desviacion_estandar(lista):
    """Calcula la desviación estándar de una lista de números."""
    return calcular_varianza(lista) ** 0.5

def calcular_moda(lista):
    """Calcula la moda de una lista de números."""
    from statistics import mode
    return mode(lista)

def calcular_mediana(lista):
    """Calcula la mediana de una lista de números."""
    from statistics import median
    return median(lista)

def calcular_determinante(matriz):
    """Calcula el determinante de una matriz."""
    return np.linalg.det(matriz)

def calcular_inversa(matriz):
    """Calcula la inversa de una matriz."""
    return np.linalg.inv(matriz)

def resolver_ecuaciones_lineales(A, b):
    """Resuelve un sistema de ecuaciones lineales Ax = b."""
    return np.linalg.solve(A, b)

def realizar_regresion_lineal(X, y):
    """Realiza una regresión lineal y devuelve el modelo."""
    model = LinearRegression()
    model.fit(X, y)
    return model

def predecir(model, nuevos_datos):
    """Realiza predicciones usando el modelo de regresión."""
    return model.predict(nuevos_datos)

def calcular_tendencia(df, columna_x, columna_y):
    """Calcula la tendencia de los datos usando regresión lineal."""
    X = df[[columna_x]].values
    y = df[columna_y].values
    modelo = realizar_regresion_lineal(X, y)
    return modelo.coef_[0], modelo.intercept_  # Devuelve la pendiente y la intersección 