# Hai il compito di indagare su un caso di numeri mancanti! Ti viene fornito un elenco di numeri univoci (nums) da 1 a n, 
# dove n è la lunghezza dell'elenco. Sembra però che ci sia un problema: mancano alcuni numeri!
# La tua missione è scrivere una funzione che prenda come input questo elenco di numeri (nums) potenzialmente incompleti. 
# Questo elenco rappresenta i numeri esistenti, ma alcuni numeri tra 1 e n potrebbero mancare.
# La funzione restituisce una nuova lista contenente tutti i numeri mancanti da 1 a n 
# che non sono presenti nella lista originale

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums) + 1
    nums_set = set(nums)
    numeri_mancanti = []
    
    for i in range(1, n):
        if i not in nums_set:
            numeri_mancanti.append(i)

    return numeri_mancanti