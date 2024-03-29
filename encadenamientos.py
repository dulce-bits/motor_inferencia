from prettytable import PrettyTable

def Encad_Atras(parametros):
    BC,BH,meta = parametros
    t = PrettyTable(['CC','NM','Meta','R','BH'])
    t.add_row([' ',' ',meta,' ',str(BH)])
    result = verificar(BC,BH,meta,t)
    print(t)
    if result:
        print('El sistema si tiene solución')
    else:
        print('El sistema no tiene solución')

def verificar(BC,BH,meta,t):
    CC=[]
    verificado = False
    if comp(meta,BH):
        return True
    else:
        CC = equipar2(CC,BC,meta)
        while CC != [] and not verificado:
            regla = CC[0]
            t.add_row([printCC(CC), str(regla.getConclusion()), str(meta), 'R'+str(regla.getIndex()),str(BH)])
            CC.pop(0)
            NM = regla.getPremisas()
            verificado = True
            while NM != [] and verificado:
                meta = NM.pop(0)
                verificado = verificar(BC,BH,meta,t)
                if verificado and meta not in BH:
                    BH.append(meta)
        t.add_row([printCC(CC), str(regla.getConclusion()), str(meta), 'R'+str(regla.getIndex()),str(BH)])
        return verificado

def equipar2(CC,BC,meta):
    for r in BC:
        if r.getConclusion()[0] == meta:
            CC.append(r)
    for r in CC:
        if r in BC:
            BC.remove(r)
    return CC

def Encad_Adelante(parametros):
    t = PrettyTable(['CC','NH','Meta','R','BH'])
    BC,BH,meta=parametros
    t.add_row([' ',' ',meta,' ',str(BH)])
    CC=[]
    CC = equipar(CC,BC,BH)
    while CC != [] and not comp(meta,BH):
        regla = CC[0]
        if comp(regla.getPremisas(), BH) and not comp(regla.getConclusion(), BH):
             BH = BH + regla.getConclusion()
             t.add_row([printCC(CC), str(regla.getConclusion()), str(meta), 'R'+str(regla.getIndex()),str(BH)])
             CC.pop(0)
        CC= equipar(CC,BC,BH)
    print(t)
    if comp(meta,BH):
        print('El sistema si tiene solución')
    else:
        print('El sistema no tiene solución')
    return


def equipar(CC,BC,BH):
    for regla in BC:
        if comp(regla.getPremisas(), BH) and not comp(regla.getConclusion(), BH):
             CC.append(regla)
    for r in CC:
        if r in BC:
            BC.remove(r)
    return CC

def printCC(CC):
    imp=[]
    for r in CC:
        imp.append('R'+str(r.getIndex()))
    return str(imp)

def comp(lista1, lista2):
    for val in lista1:
        if val not in lista2:
            return False
    return True
