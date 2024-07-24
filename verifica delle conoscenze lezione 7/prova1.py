'''
Scrivi una funzione che elimini dalla lista dati certi 
elementi specificati in un dizionario. Il dizionario 
contiene elementi da rimuovere come chiavi e il numero 
di volte che devono essere rimossi come valori.
'''
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for elem, count in da_rimuovere.items():
        while count > 0 and elem in lista:
            lista.remove(elem)
            count -= 1
    return lista