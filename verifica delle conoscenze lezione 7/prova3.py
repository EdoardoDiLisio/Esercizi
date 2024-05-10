'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo 
i prodotti che hanno un prezzo superiore a 20, scontati del 10%.Scrivi una funzione che accetti un dizionario di prodotti 
con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:

    return {product: price * 0.9 for product, price in prodotti.items() if price > 20}

##################################################################################################

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    discounted_prodotti = {}
    for product, price in prodotti.items():
        if price > 20:
            discounted_price = price * 0.9
            discounted_prodotti[product] = discounted_price
    return discounted_prodotti
