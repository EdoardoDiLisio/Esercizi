class Film:
    def __init__(self, id, title):
        # Metodo costruttore per inizializzare gli attributi
        self.__id = id  # Codice identificativo (privato)
        self.__title = title  # Titolo (privato)

    def setID(self, id):
        # Metodo per impostare il codice identificativo del film
        self.__id = id

    def setTitle(self, title):
        # Metodo per impostare il titolo del film
        self.__title = title

    def getID(self):
        # Metodo per ottenere il codice identificativo del film
        return self.__id

    def getTitle(self):
        # Metodo per ottenere il titolo del film
        return self.__title

    def isEqual(self, otherFilm):
        # Metodo per confrontare se due film hanno lo stesso codice identificativo
        return self.__id == otherFilm.getID()
