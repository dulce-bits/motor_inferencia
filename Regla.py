# Regla Si X -> Y#
class Regla:
    def __init__(self, premisas, concluciones, index):
        self.premisas = premisas
        self.concluciones = concluciones
        self.index = index

    def getPremisas(self):
        return self.premisas

    def getConcluciones(self):
        return self.concluciones

    def getIndex(self):
        return self.index

    def checkPremisa(self, premisa):
        return premisa in self.premisas

    def checkConclucion(self, conclucion):
        return conclucion in self.concluciones

    def checkIndex(self, index):
        return index in self.index
