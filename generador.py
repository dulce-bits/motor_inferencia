from Regla import Regla

#Reglas y base de conocimiento de ejemplo para una computadora que no sirve

class Generador:

    def GenerarBC(self,filename):   #Aqui se definen las reglas X->Y|-Conclusion
        contador = 1  # el indice de la regla
        f = open(filename,'r')
        reglas=[]
        for r in f:#Lee renglon por renglon en el archivo f
            aux = r.split() # lista con cada palabra
            aux2 = [] # guarda la premisa
            for p in aux:
                if p == '->':
                    break
                aux2.append(p)            
            reglas.append(Regla(aux2,[aux[-1]],contador))
            contador += 1 
        f.close()
        return reglas  

    def GenerarBH(self,n): 
        hechos=[]
        for i in range(n):
            print('Ingrese hecho')
            hechos.append(input())

        return hechos