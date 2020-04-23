class flabianos:
    """ Lista de invitados a la cena del señor en el laboratorio """

    def __init__(self):
        self.Invitados=['Ruben']

    def TuSiTuNo(self,EllosSi):        
        if EllosSi in self.Invitados:
            return('Aceptado')
        else:
            return('Denegado')
