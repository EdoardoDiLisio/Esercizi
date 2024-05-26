class Prodotto:
    def __init__(self, nome, quantita):
        self.nome = nome
        self.quantita = quantita

class Magazzino:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, nome):
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return prodotto
        return None

# Esempio di utilizzo del programma
magazzino = Magazzino()

# Aggiungiamo alcuni prodotti al magazzino
magazzino.aggiungi_prodotto(Prodotto("Penna", 100))
magazzino.aggiungi_prodotto(Prodotto("Quaderno", 50))
magazzino.aggiungi_prodotto(Prodotto("Matita", 75))

# Cerchiamo un prodotto per nome
nome_prodotto = "Penna"
prodotto_cercato = magazzino.cerca_prodotto(nome_prodotto)

if prodotto_cercato:
    print(f"Il prodotto '{nome_prodotto}' è presente nel magazzino con una quantità di {prodotto_cercato.quantita}.")
else:
    print(f"Il prodotto '{nome_prodotto}' non è presente nel magazzino.")

# Verifichiamo la disponibilità di un prodotto
nome_prodotto = "Quaderno"
prodotto_cercato = magazzino.cerca_prodotto(nome_prodotto)

if prodotto_cercato:
    if prodotto_cercato.quantita > 0:
        print(f"Il prodotto '{nome_prodotto}' è disponibile nel magazzino.")
    else:
        print(f"Il prodotto '{nome_prodotto}' non è disponibile nel magazzino.")
else:
    print(f"Il prodotto '{nome_prodotto}' non è presente nel magazzino.")