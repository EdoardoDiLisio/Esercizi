#Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. 
#Restituisce l'elenco riorganizzato.

def even_odd_pattern(nums: list[int]) -> list[int]:
    
    pari = [num for num in nums if num % 2 == 0]
    dispari = [num for num in nums if num % 2 != 0]
    return pari + dispari