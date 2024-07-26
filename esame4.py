def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dizionario = {}
    for chiave , valore in tuples:
        if chiave in dizionario:
            dizionario[chiave] += valore
        else:
            dizionario[chiave] = valore
    return dizionario