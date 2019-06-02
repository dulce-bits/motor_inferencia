def EncadenamientoHA(parametros):
    BC, BH, meta = parametros
    while (not comp(meta, BH)):
        skip = False
        for regla in BC:
            if comp(meta, regla.getConcluciones()):
                if comp(regla.getPremisas(), BH):
                    BH.extend(regla.getConcluciones()) # agrega a la BH la conclusión de esa regla
                    print('|'+str(regla.getPremisas())+'| '+str(meta)+' | R'+str(regla.getIndex())+' |'+str(BH))
                    skip = True
                else:
                    for premisa in regla.getPremisas():
                        if premisa not in BH:
                            EncadenamientoHA([BC, BH, premisa])                           
            if skip:
                break
    return meta,BH


def EncadenamientoHAd(parametros):
    BC, BH, meta = parametros
    print('|NH   | Meta | R  |     BH     ')
    print('|     |  '+meta+'   |    |'+str(BH))
    while (not comp(meta, BH)):
        skip = False
        for regla in BC:
            if comp(regla.getPremisas(), BH) and not comp(regla.getConcluciones(), BH):
                BH = BH + regla.getConcluciones()
                print('|'+str(regla.getConcluciones())+'|  '+meta+'   | R'+str(regla.getIndex())+' |'+str(BH))
                skip = True
            if skip:
                break
    if comp(meta, BH):
        print('El sistema si tiene solución')
    else:
        print('El sistema no tiene solución')
    return


# Verificar si la lista1 esta dentro de la lista2
def comp(lista1, lista2):
    for val in lista1:
        if val not in lista2:
            return False
    return True
