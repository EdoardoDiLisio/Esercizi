'''
Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi. 
Queste note possono avere altezze (valori) diversi. Una sequenza armoniosa è come una melodia piacevole in cui la differenza 
di altezza tra la nota massimale e quella minimale è uguale a 1. Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, perché 
la differenza fra 3 e 2 è 1.

Trovare l'armonia perfetta:

Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri). 
La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note. Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.

Colpire le note giuste:

Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. 
La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza).
'''

def find_lhs(nums: list[int]) -> int:
    freq_map = {}
    max_length = 0
    
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    for num in freq_map:
        if num + 1 in freq_map:
            max_length = max(max_length, freq_map[num] + freq_map[num + 1])
    
    return max_length
