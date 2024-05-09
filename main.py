from flask import Flask, jsonify, request
from utils.cargarJsonFile import cargar_json
from utils.jsonProcessor import procesar_afectado_from_json
from classes.afectadoClass import Afectado
from classes.sectionClass import Section1

app = Flask(__name__)

@app.route('/process', methods=['GET'])
def process_data():
    # Carga el JSON
    data = cargar_json('filesJson/jsonPrueba1.json')

    # Procesa los datos
    for registro in data['data']['afectado']:
        afectado = procesar_afectado_from_json(registro, data['data']['section1'])

    # Devuelve los afectados procesados como parte de la respuesta JSON
    afectados_procesados = [afectado.to_dict() for afectado in afectado_dict.values()]
    return jsonify({"message": "Datos procesados con éxito", "data": afectados_procesados})


afectado_dict = {}
def procesar_afectado_from_json(afectado_data, sections_data):
    identificador = afectado_data['identificador']

    # Crear o recuperar la instancia de Afectado
    if identificador not in afectado_dict:
        afectado = Afectado(
            id=afectado_data['id'],
            identificador=identificador,
            afectado=[afectado_data['afectado']],
            source=afectado_data['source'],
            administrador=afectado_data['administrador'],
            deudor=afectado_data['deudor'],
            inhabilitado=afectado_data['inhabilitado'],
            sections1_edictos_concursales=[]
        )
        afectado_dict[identificador] = afectado
    else:
        afectado = afectado_dict[identificador]
        if afectado_data['afectado'] not in afectado.afectado:
            afectado.afectado.append(afectado_data['afectado'])

    # Procesar cada sección
    for section_data in sections_data:
        datos_resolucion_s1_extracted={
                'Cese_Administrador_Concursal': section_data.get('datosResolucionS1', {}).get('ceseAdministradorConcursal', None),
                'Concurso': section_data.get('datosResolucionS1', {}).get('tipoConcurso', {}).get('desTipoConcurso', None),
                'Cesa_Limita_Facultades_Administrativas': section_data.get('datosResolucionS1', {}).get('autoConclusionConcurso', {}).get('tipoCesaLimitFacuAdmin', {}).get('desTipoCesaLimitFacuAdmin', None),
                'Conclusion': section_data.get('datosResolucionS1', {}).get('autoConclusionConcurso', {}).get('tipoConclusion', {}).get('desTipoConclusion', None),
                'nombra_Administrador_Concursales': section_data.get('datosResolucionS1', {}).get('nombraAdministradorConcursales', None),
                'Procedimiento': section_data.get('datosResolucionS1', {}).get('tipoProcedimiento', {}).get('desTipoProcedimiento', None)
            }
        section = Section1(
            tipo_resolucion_procesal=section_data.get('tipoResolucionProcesal', {}).get('desTipoResoProcesales', ''),
            tipo_seccion=section_data.get('tipoSeccion', {}).get('descripcion', ''),
            tipo_sentencia_firme=section_data.get('tipoSentenciaFirme', {}).get('desTipoSentenciaFirme', ''),
            num_procedimiento=section_data.get('numProcedimiento'),
            nombre_juez=section_data.get('juzgadoIri', {}).get('nombreJuezCompleto', ''),
            juzgado=section_data.get('juzgadoIri', {}).get('nombre', ''),
            documento_concursal=section_data.get('documentosConcursal', {}).get('fechaRecepcion', ''),
            contenido_edicto=section_data.get('contenidoEdicto'),
            fecha_resolucion=section_data.get('fechaResolucion'),
            datos_resolucion_s1=datos_resolucion_s1_extracted
        )

        # Verificar duplicados
        existente = any(
        sec.tipo_resolucion_procesal == section.tipo_resolucion_procesal and
        sec.num_procedimiento == section.num_procedimiento and
        sec.contenido_edicto == section.contenido_edicto and
        sec.fecha_resolucion == section.fecha_resolucion
        for sec in afectado.sections1_edictos_concursales
    )

        if not existente:
            afectado.sections1_edictos_concursales.append(section)

    return afectado


if __name__ == '__main__':
    app.run(debug=True)
