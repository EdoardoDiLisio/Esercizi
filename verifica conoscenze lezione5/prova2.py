'''
Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere,
mantenendo l'ordine originale degli elementi.
'''

def remove_duplicates(lst: list) -> list:
    seen = set()  
    result = []   
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result