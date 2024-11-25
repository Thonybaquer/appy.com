import matplotlib.pyplot as plt
import numpy as np

def graficar_funcion(funcion, rango):
    """Grafica una función en un rango dado."""
    x = np.linspace(rango[0], rango[1], 100)
    y = eval(funcion)  # Asegúrate de que 'funcion' sea segura
    plt.plot(x, y)
    plt.title(f'Gráfica de {funcion}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()

def graficar_3d(funcion, rango):
    """Grafica una función en 3D."""
    x = np.linspace(rango[0], rango[1], 100)
    y = np.linspace(rango[0], rango[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = eval(funcion)  # Asegúrate de que 'funcion' sea segura
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    plt.title(f'Gráfica 3D de {funcion}')
    plt.show()

def graficar_histograma(data):
    """Grafica un histograma de los datos."""
    plt.hist(data, bins=30, alpha=0.7, color='blue')
    plt.title('Histograma de Datos')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.show()

def graficar_pie(data):
    """Grafica un gráfico de pastel."""
    plt.pie(data, labels=[f'Parte {i+1}' for i in range(len(data))], autopct='%1.1f%%')
    plt.title('Gráfico de Pastel')
    plt.show()

def graficar_lineas(x, y):
    """Grafica líneas a partir de dos listas de datos."""
    plt.plot(x, y)
    plt.title('Gráfica de Líneas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid()
    plt.show()

def graficar_barras(x, y):
    """Grafica un gráfico de barras."""
    plt.bar(x, y)
    plt.title('Gráfico de Barras')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.show() 