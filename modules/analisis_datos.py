import pandas as pd
import matplotlib.pyplot as plt
from modules.calculos import calcular_tendencia

def cargar_datos(archivo):
    """Carga datos desde un archivo CSV."""
    try:
        return pd.read_csv(archivo)
    except FileNotFoundError:
        return "Error: Archivo no encontrado."

def analizar_datos(df):
    """Devuelve un resumen estadístico del DataFrame."""
    return df.describe()

def filtrar_datos(df, condiciones):
    """Filtra datos en el DataFrame según condiciones dadas."""
    return df.query(condiciones)

def graficar_tendencia(df, columna_x, columna_y):
    """Grafica la tendencia de los datos usando regresión lineal."""
    coef, intercepto = calcular_tendencia(df, columna_x, columna_y)
    plt.scatter(df[columna_x], df[columna_y], color='blue')
    plt.plot(df[columna_x], coef * df[columna_x] + intercepto, color='red')
    plt.title(f'Tendencia de {columna_y} vs {columna_x}')
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.show()

def graficar_datos(df, columna_x, columna_y):
    """Grafica datos de dos columnas en un gráfico de dispersión."""
    df.plot(x=columna_x, y=columna_y, kind='scatter')
    plt.title(f'Gráfica de {columna_y} vs {columna_x}')
    plt.show()

def calcular_correlacion(df):
    """Calcula la correlación entre columnas del DataFrame."""
    return df.corr()

def graficar_caja(df, columna):
    """Grafica un gráfico de caja para una columna del DataFrame."""
    plt.boxplot(df[columna])
    plt.title(f'Gráfico de Caja de {columna}')
    plt.show()

def calcular_media(df, columna):
    """Calcula la media de una columna del DataFrame."""
    return df[columna].mean()

def calcular_varianza(df, columna):
    """Calcula la varianza de una columna del DataFrame."""
    return df[columna].var()

def graficar_histograma(df, columna):
    """Grafica un histograma de una columna del DataFrame."""
    plt.hist(df[columna], bins=30, alpha=0.7, color='blue')
    plt.title(f'Histograma de {columna}')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.show() 