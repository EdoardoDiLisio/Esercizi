class Elettrodomestico:
    def __init__(self, marca, modello, potenza):
        # Metodo costruttore che inizializza gli attributi marca, modello e potenza.
        self.marca = marca
        self.modello = modello
        self.potenza = potenza
       
    def descrivi_elettrodomestico(self):
        # Metodo che stampa una descrizione del Elettrodomestico nel formato specificato.
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W")

class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, potenza, capacità: int):
        # Metodo costruttore che inizializza gli attributi della classe base e capacità: int.
        super().__init__(marca, modello, potenza)
        self.capacità = capacità

    def descrivi_elettrodomestico(self):
        # Sovrascrive il metodo della classe base per includere anche il numero di porte nella descrizione.
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Capacità: {self.capacità}L")



class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, potenza, carico_max: int):
        # Metodo costruttore che inizializza gli attributi della classe base e carico_max: int.
        super().__init__(marca, modello, potenza)
        self.carico_max = carico_max

    def descrivi_elettrodomestico(self):
        # Sovrascrive il metodo della classe base per includere anche il carico_max: int di  Lavatrice nella descrizione.
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Carico massimo: {self.carico_max}kg")


# Test case per verificare la funzionalità delle classi
# Creazione di oggetti Frigorifero e Lavatrice e descrizione degli elettrodomestici
frigo = Frigorifero("Samsung", "RT38K5538S8", 100, 380)
lavatrice = Lavatrice("LG", "F4J6VY1W", 200, 10)

# Descrizione degli elettrodomestici
frigo.descrivi_elettrodomestico()
lavatrice.descrivi_elettrodomestico()