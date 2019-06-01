def EncadenamientoHA(parametros):
    BC, BH, meta = parametros
    while (not comp(meta, BH)):
        skip = False
        for regla in BC:
            if comp(meta, regla.getConcluciones()):
                if comp(regla.getPremisas(), BH):
                    print (str(regla.getPremisas().index(regla.getPremisas()))+"Se aplico ReglaJAJAJAJASS:", (regla.getPremisas(), regla.getConcluciones()))
                    BH.extend(regla.getConcluciones()) # agrega a la BH la conclusión de esa regla
                    skip = True
                else:
                    for premisa in regla.getPremisas():
                        if premisa not in BH:
                            EncadenamientoHA([BC, BH, [premisa]])
            if skip:
                break
    print (BH)
    return


def EncadenamientoHAd(parametros):
    BC, BH, meta = parametros
    print('|NH   | Meta | R |     BH     ')
    while (not comp(meta, BH)):
        skip = False
        for regla in BC:
            if comp(regla.getPremisas(), BH) and not comp(regla.getConcluciones(), BH):
                #print ("Se aplico Regla:", (regla.getPremisas(), regla.getConcluciones()))
                BH = BH + regla.getConcluciones()
                print('|'+str(regla.getConcluciones())+'|  '+meta+'   | '+str(regla.getIndex())+' |'+str(BH))
                skip = True
            if skip:
                break
    return


# Verificar si la lista1 esta dentro de la lista2
def comp(lista1, lista2):
    for val in lista1:
        if val not in lista2:
            return False
    return True
