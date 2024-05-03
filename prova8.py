'''
def prime_factors(n: int) -> list[int]:
    
    fattori_primi = []

    while n % 2 == 0:
        fattori_primi.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            fattori_primi.append(i)
            n //= i

    if n > 2:
        fattori_primi.append(n)

    return fattori_primi
    
    '''
# Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). 
# Questi gioielli hanno vari valori, alcuni più preziosi di altri. Il tuo compito è trovare il terzo gioiello distinto più 
# prezioso nello scrigno.
# Qual è la svolta?
# Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). 
# A noi però interessano solo valori distinti, ovvero gioielli con valori unici.
# Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). 
# Se nello scrigno sono presenti almeno tre valori distinti, la funzione dovrebbe restituire il valore del terzo 
# gioiello distinto di maggior valore.
# Ma c'è un problema!
# Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), 
# la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.

def third_max(nums: list[int]) -> int:
    unique_nums = sorted(set(nums), reverse=True)
    if len(unique_nums) >= 3:
            return unique_nums[2]
    else:
        return max(unique_nums)