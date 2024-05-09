class Afectado:
    def __init__(self, id, identificador, afectado, source, administrador, deudor, inhabilitado, sections1_edictos_concursales=None, sections2=None, sections3=None):
        self.id = id
        self.identificador = identificador
        self.afectado = afectado
        self.source = source
        self.administrador = administrador
        self.deudor = deudor
        self.inhabilitado = inhabilitado  
        self.sections1_edictos_concursales = sections1_edictos_concursales or []  
        self.sections2 = sections2 or []  
        self.sections3 = sections3 or []  

    def agregar_section1(self, section):
        self.sections1_edictos_concursales.append(section)

    def agregar_section2(self, section):
        self.sections2.append(section)

    def agregar_section3(self, section):
        self.sections3.append(section)

    def to_dict(self):
        data = vars(self).copy()
        if self.sections1_edictos_concursales:
            data['sections1_edictos_concursales'] = [section.to_dict() for section in self.sections1_edictos_concursales],
        if self.sections2:
            data['sections2'] = [section.to_dict() for section in self.sections2],
        if self.sections3:
            data['sections3'] = [section.to_dict() for section in self.sections3],
        return data
