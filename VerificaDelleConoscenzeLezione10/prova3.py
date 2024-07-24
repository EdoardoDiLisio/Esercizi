'''
Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.
'''

def calcola_stipendio(ore_lavorate: int) -> float:
    paga_oraria = 10
    ore_normali = 40

    if ore_lavorate <= ore_normali:
        stipendio_lordo = ore_lavorate * paga_oraria
    else:
        ore_extra = ore_lavorate - ore_normali
        stipendio_lordo = (ore_normali * paga_oraria) + (ore_extra * paga_oraria * 1.5)
    
    return stipendio_lordo

print(calcola_stipendio(40))

print(calcola_stipendio(30))

print(calcola_stipendio(45))

print(calcola_stipendio(60))

print(calcola_stipendio(0))