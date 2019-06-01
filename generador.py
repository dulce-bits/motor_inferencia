from Regla import Regla

#Reglas y base de conocimiento de ejemplo para una computadora que no sirve

class Generador:

    def GenerarBC(self,n):   #Aqui se definen las reglas X->Y|-Conclusion
        """
        contador = 1  # el indice de la regla
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
            reglas.append(Regla(aux2,[aux[-1],contador]))
            contador = contador + 1 
            print(aux2, aux[-1])
            """
        reglas=[]
 
        reglas.append(Regla(['A','B'],['C'],1))
        reglas.append(Regla(['A'],['D'],2))
        reglas.append(Regla(['C','D'],['E'],3))
        reglas.append(Regla(['B','E','F'],['G'],4))
        reglas.append(Regla(['A','E'],['H'],5))
        reglas.append(Regla(['D','E','H'],['I'],6))

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