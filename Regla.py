class Regla:
    def __init__(self, premisas, conclusion, index):
        self.premisas = premisas
        self.conclusion = conclusion
        self.index = index

    def getPremisas(self):
        return self.premisas

    def getConclusion(self):
        return self.conclusion

    def getIndex(self):
        return self.index

    def checkPremisa(self, premisa):
        return premisa in self.premisas

    def checkIndex(self, index):
        return index in self.index
