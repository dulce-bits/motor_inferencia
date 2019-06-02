from Regla import Regla

#Reglas y base de conocimiento de ejemplo para una computadora que no sirve

class Generador:

    def GenerarBC(self,n):   #Aqui se definen las reglas X->Y|-Conclusion
        """
        reglasStr = []
        for i in range(n):
            reglasStr.append(input())
        reglas=[]
        for r in reglasStr:
            aux = r.split() # lista con cada palabra
            aux2 = [] # guarda la premisa
            for p in aux:
                if p == '->':
                    break
                aux2.append(p)
            reglas.append(Regla(aux2,[aux[-1]]))
            print(aux2, aux[-1])
            """
        reglas=[]
        reglas.append(Regla(['A','B'],['C']))
        reglas.append(Regla(['A'],['D']))
        reglas.append(Regla(['C','D'],['E']))
        reglas.append(Regla(['B','E','F'],['G']))
        reglas.append(Regla(['A','E'],['H']))
        reglas.append(Regla(['D','E','H'],['I']))

        return reglas

       

    def GenerarBH(self,n): 
        hechos=[]
        """
        for i in range(n):
            hechos.append(input())
            """
        hechos.append('A')
        hechos.append('B')
        hechos.append('F')
        return hechos


    def GenerarMeta(self):   #Aqui va la conclusion a llegar finalmente
        #return input()
        return 'H'