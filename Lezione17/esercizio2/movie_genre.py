#  EDOARDO DI LISIO
#  10.06.24

from film import Film

class Genre(Film):
    def __init__(self, id, title, genre, penale):
        # Metodo costruttore per inizializzare attributi della classe Genre e della classe padre Film
        super().__init__(id, title)
        self.__genre = genre  # Genere del film (privato)
        self.__penale = penale  # Penale associata al genere del film (privato)

    def getGenere(self):
        # Metodo per ottenere il genere del film
        return self.__genre

    def getPenale(self):
        # Metodo per ottenere il valore della penale associata al genere del film
        return self.__penale

    def calcolaPenaleRitardo(self, days):
        # Metodo per calcolare la penale da pagare per il ritardo nella restituzione del film
        return self.__penale * days

class Azione(Genre):
    def __init__(self, id, title):
        # Metodo costruttore per inizializzare attributi specifici per il genere Azione
        super().__init__(id, title, "Azione", 3.0)

class Commedia(Genre):
    def __init__(self, id, title):
        # Metodo costruttore per inizializzare attributi specifici per il genere Commedia
        super().__init__(id, title, "Commedia", 2.5)

class Drama(Genre):
    def __init__(self, id, title):
        # Metodo costruttore per inizializzare attributi specifici per il genere Drama
        super().__init__(id, title, "Dramma", 2.0)
