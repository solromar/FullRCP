import json
from flask import Flask, jsonify, request
from utils.jsonProcessor import procesar_afectado_from_json
from utils.cargarJsonFile import cargar_json
from classes.afectadoClass import Afectado
from classes.sectionClass import Section1

app = Flask(__name__)

@app.route('/process', methods=['GET'])
def process_data():
    # Carga el JSON
    data = cargar_json('filesJson/jsonPrueba1.json')

    # Lista para almacenar los datos procesados
    afectados_procesados = []

    # Procesa los datos
    for registro in data['data']['afectado']:
        for section in data['data']['section1']:  # Asumiendo que quieres procesar todas las secciones
            print(registro)
            afectado = procesar_afectado_from_json(registro, section)
            if afectado:
                # Agrega el diccionario del afectado procesado a la lista
                afectados_procesados.append(afectado.to_dict())

    # Devuelve los afectados procesados como parte de la respuesta JSON
    return jsonify({"message": "Datos procesados con éxito", "data": afectados_procesados})

if __name__ == '__main__':
    app.run(debug=True)
