'''
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
'''

def list_statistics(numbers: list[int]) -> ... :
    if not numbers:
        return None, None, None
    
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    
    return maximum, minimum, average