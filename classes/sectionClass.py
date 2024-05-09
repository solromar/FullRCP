class Section1:
    def __init__(self, tipo_resolucion_procesal=None, tipo_seccion=None, datos_resolucion_s1=None,tipo_sentencia_firme=None, num_procedimiento=None, nombre_juez=None, juzgado=None, documento_concursal=None, contenido_edicto=None, fecha_resolucion=None):
        self.tipo_resolucion_procesal = tipo_resolucion_procesal
        self.tipo_seccion = tipo_seccion
        self.tipo_sentencia_firme = tipo_sentencia_firme
        self.num_procedimiento = num_procedimiento
        self.nombre_juez = nombre_juez 
        self.juzgado = juzgado
        self.documento_concursal = documento_concursal 
        self.contenido_edicto = contenido_edicto
        self.fecha_resolucion = fecha_resolucion
        self.datos_resolucion_s1=datos_resolucion_s1
        

    def to_dict(self):
        data = vars(self).copy()
        return data


class Section2:
    def __init__(self, tipo_sentencia_firme=None,tipo_operacion=None, source=None, tomo=None, fecha_resolucion=None, num_procedimiento=None, datos_resolucion_s2=None, nombre_juez=None, juzgado=None, numero_juzgado=None, documento_concursal=None, folio=None, tipo_resolucion_concursal=None, cesa_limitaciones=None ):
        self.tipo_sentencia_firme = tipo_sentencia_firme        
        self.tipo_operacion = tipo_operacion
        self.source = source
        self.tomo = tomo
        self.fecha_resolucion = fecha_resolucion
        self.num_procedimiento = num_procedimiento
        self.datos_resolucion_s2=datos_resolucion_s2
        self.nombre_juez = nombre_juez 
        self.juzgado = juzgado
        self.numero_juzgado = numero_juzgado
        self.documento_concursal = documento_concursal
        self.folio = folio
        self.tipo_resolucion_concursal = tipo_resolucion_concursal
        self.cesa_limitaciones = cesa_limitaciones       
        

    def to_dict(self):
        data = vars(self).copy()
        return data