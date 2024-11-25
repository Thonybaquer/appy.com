from modules.calculos import (
    resolver_ecuacion,
    graficar_funcion,
    calcular_media,
    calcular_varianza,
)
from modules.analisis_datos import analizar_datos
from modules.exportacion import (
    exportar_a_excel,
    exportar_a_pdf,
    exportar_a_csv,
    exportar_a_json,
    exportar_a_txt,
    exportar_a_word
)
from modules.busqueda import buscar
from modules.seguridad import autenticar_usuario
import requests
import sqlite3

class AI_Assistant:
    def __init__(self):
        self.data = None
        self.conn = sqlite3.connect('knowledge_base.db')

    def buscar_en_wikipedia(self, query):
        """Busca información en Wikipedia."""
        url = f"https://es.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
        response = requests.get(url)
        data = response.json()
        if data['query']['search']:
            return data['query']['search'][0]['snippet']
        return "No se encontró información."

    def buscar_en_base_de_datos(self, query):
        """Busca información en la base de datos."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM knowledge WHERE topic LIKE ?", ('%' + query + '%',))
        results = cursor.fetchall()
        return results if results else "No se encontró información."

    def procesar_comando(self, comando):
        """Procesa un comando dado y devuelve la respuesta."""
        if "resolver" in comando:
            ecuacion = comando.split("resolver ")[1]
            return resolver_ecuacion(ecuacion)
        elif "graficar" in comando:
            funcion = comando.split("graficar ")[1]
            return graficar_funcion(funcion, (-10, 10))
        elif "analizar" in comando:
            return "Análisis en progreso..."
        elif "media" in comando:
            return f"La media es: {calcular_media(self.data)}"
        elif "varianza" in comando:
            return f"La varianza es: {calcular_varianza(self.data)}"
        elif "buscar" in comando:
            query = comando.split("buscar ")[1]
            return buscar(query)
        elif "buscar en Wikipedia" in comando:
            query = comando.split("buscar en Wikipedia ")[1]
            return self.buscar_en_wikipedia(query)
        elif "buscar en la base de datos" in comando:
            query = comando.split("buscar en la base de datos ")[1]
            return self.buscar_en_base_de_datos(query)
        return "Comando no reconocido."

    def aprender_de_usuario(self, usuario_input):
        """Lógica para aprender de las interacciones del usuario."""
        with open('user_interactions.txt', 'a') as f:
            f.write(usuario_input + '\n')

    def sugerir_funciones(self, usuario_input):
        """Sugerir funciones basadas en el input del usuario."""
        pass

    def cargar_datos(self, datos):
        """Carga datos que ISA puede usar para cálculos."""
        self.data = datos 