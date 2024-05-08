class Section1:
    def __init__(self, tipo_resolucion_procesal=None, tipo_sentencia_firme=None, num_procedimiento=None, juzgado_iri=None, documento_concursal=None, contenido_edicto=None, fecha_resolucion=None):
        self.tipo_resolucion_procesal = tipo_resolucion_procesal
        self.tipo_sentencia_firme = tipo_sentencia_firme
        self.num_procedimiento = num_procedimiento
        self.juzgado_iri = juzgado_iri if isinstance(juzgado_iri, dict) else {}
        self.documento_concursal = documento_concursal 
        self.contenido_edicto = contenido_edicto
        self.fecha_resolucion = fecha_resolucion

    def to_dict(self):
        data = vars(self).copy()
        return data
