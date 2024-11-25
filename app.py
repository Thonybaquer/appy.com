try:
    from flask import Flask, render_template, request, jsonify
except ImportError:
    print("Error: Flask no está instalado. Por favor, ejecuta: pip install flask")
    exit(1)

try:
    from modules.calculos import suma, resta, resolver_ecuacion
    from modules.busqueda import buscar
    from modules.seguridad import autenticar_usuario
    from modules.ai_assistant import AI_Assistant
    from modules.animation_engine import graficar_funcion
    from modules.exportacion import exportar_a_excel
except ImportError as e:
    print(f"Error al importar módulos: {e}")
    print("Por favor, asegúrate de que todos los módulos estén instalados correctamente")
    exit(1)

app = Flask(__name__)
ai_assistant = AI_Assistant()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    resultado = suma(data['a'], data['b'])
    return jsonify({'resultado': resultado})


@app.route('/buscar', methods=['POST'])
def buscar_datos():
    query = request.json['query']
    resultados = buscar(query)
    return jsonify({'resultados': resultados})


@app.route('/autenticar', methods=['POST'])
def autenticar():
    data = request.json
    exito = autenticar_usuario(data['usuario'], data['contrasena'])
    return jsonify({'exito': exito})


@app.route('/ai', methods=['POST'])
def ai():
    comando = request.json['comando']
    respuesta = ai_assistant.procesar_comando(comando)
    return jsonify({'respuesta': respuesta})


@app.route('/graficar', methods=['POST'])
def graficar():
    data = request.json
    resultado = graficar_funcion(data['funcion'], data['rango'])
    return jsonify({'resultado': resultado})


@app.route('/exportar', methods=['POST'])
def exportar():
    data = request.json
    exportar_a_excel(data['df'], data['nombre_archivo'])
    return jsonify({'mensaje': 'Exportación exitosa'})


@app.route('/cargar_datos', methods=['POST'])
def cargar_datos():
    data = request.json['data']
    ai_assistant.cargar_datos(data)
    return jsonify({'mensaje': 'Datos cargados exitosamente'})


@app.route('/cambiar_idioma', methods=['POST'])
def cambiar_idioma():
    data = request.json
    ai_assistant.cambiar_idioma(data['idioma'])
    return jsonify({'mensaje': f'Idioma cambiado a {data["idioma"]}'})


@app.route('/corregir_texto', methods=['POST'])
def corregir_texto():
    data = request.json
    texto_corregido = ai_assistant.corregir_texto(data['texto'])
    return jsonify({'texto_corregido': texto_corregido})


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
