'''
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e 
l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui 
il numero specificato di posizioni sia maggiore della lunghezza della lista.
'''

def rotate_left(elements: list, k: int) -> list:
    if not elements:
        return elements
    k = k % len(elements)
    rotated_elements = elements[k:] + elements[:k]
    return rotated_elements