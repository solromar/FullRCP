from classes.afectadoClass import Afectado
from classes.sectionClass import Section1


afectado_dict = {}
def procesar_afectado_from_json(afectado_data, section_data):
    #print(type(afectado_data))
    #print(afectado_data.keys()) 
    #print(type(section_data))
    #print(section_data.keys()) 
    
    # Extracción de la información de la persona
    id = afectado_data.get('id')
    identificador = afectado_data.get('identificador')
    afectado = afectado_data.get('afectado')
    source = afectado_data.get('source', '')
    administrador = afectado_data.get('administrador', False)
    deudor = afectado_data.get('deudor', False)
    inhabilitado = afectado_data.get('inhabilitado', False)

    # Creación de la instancia de Afectado
    if identificador not in afectado_dict:
        afectado = Afectado(
            id=id,
            identificador=identificador,
            afectado=afectado,
            source=source,
            administrador=administrador,
            deudor=deudor,
            inhabilitado=inhabilitado
        )
        afectado_dict[identificador] = afectado
    else:
        afectado = afectado_dict[identificador]

    # Creación de la instancia de Section y agregación a Afectado
    section_data = {
        #'tipoResolucionProcesal': section_data.get('tipoResolucionProcesal', {}).get('desTipoResoProcesales', ''),
        'tipo_resolucion_procesal': section_data.get('tipoResolucionProcesal', {}).get('desTipoResoProcesales', ''),
        'tipo_sentencia_firme': section_data.get('tipoSentenciaFirme', {}).get('desTipoSentenciaFirme', ''),        
        'num_procedimiento': section_data.get('numProcedimiento', None),
        'juzgado_iri': section_data.get('juzgadoIri', {}).get('nombreJuezCompleto' , ''),
        'documento_concursal': section_data.get('documentosConcursal', {}).get('fechaRecepcion' , ''),
        'contenido_edicto': section_data.get('contenidoEdicto', None),
        'fecha_resolucion': section_data.get('fechaResolucion', None)
    }
    
    # Verificación para evitar duplicados
    existente = any(
    sec.tipo_resolucion_procesal == section_data['tipo_resolucion_procesal'] and
    sec.num_procedimiento == section_data['num_procedimiento'] and
    sec.contenido_edicto == section_data['contenido_edicto'] and
    sec.fecha_resolucion == section_data['fecha_resolucion'] 
    
    for sec in afectado.sections1
)

    if not existente:
     section = Section1(**section_data)
     afectado.agregar_section1(section)

    return afectado
