

def dic_buscar(valor):

    d = {"CORDOBA":5000,
        "MENDOZA":5500,
        "CHACO":3500,
        "FORMOSA":3600,
        "CORRIENTES":3400}

    #ret = None

    #{loc for loc in d.keys() if loc[:len(valor)]==valor}

    # {loc for loc in d.keys() if loc[:len(valor)]==valor}
    # ------
    # d2 = {valor:loc for loc in d.keys() if loc[:len(valor)]==valor}
    #ret = d2.get(valor,"")
    # ------
    ret = {valor:loc for loc in d.keys() if loc[:len(valor)]==valor}.get(valor)
    
    return ret


print("FOR", dic_buscar("FOR"))
print("COR", dic_buscar("COR"))
print("CORR", dic_buscar("CORR"))
print("ENT", dic_buscar("ENT"))

