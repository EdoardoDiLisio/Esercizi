#  EDOARDO DI LISIO
#  10.06.24

class Noleggio:
    def __init__(self, film_list):
        """
        Inizializza la classe Noleggio con una lista di film disponibili in negozio
        e un dizionario per tenere traccia dei film noleggiati da ogni cliente.

        Args:
        - film_list: una lista di oggetti Film disponibili in negozio.
        """
        self.film_list = film_list  # Lista di film disponibili
        self.rented_film = {}  # Dizionario per i film noleggiati dai clienti

    def isAvaible(self, film):
        """
        Verifica se un film è disponibile in negozio.

        Args:
        - film: l'oggetto Film da verificare.

        Returns:
        - True se il film è disponibile, False altrimenti.
        """
        return film in self.film_list

    def rentAMovie(self, film, clientID):
        """
        Noleggia un film per un cliente.

        Args:
        - film: l'oggetto Film da noleggiare.
        - clientID: l'ID del cliente che noleggia il film.
        """
        if self.isAvaible(film):  # Verifica disponibilità del film
            self.film_list.remove(film)  # Rimuove il film dalla lista dei disponibili
            if clientID in self.rented_film:  # Se il cliente ha già noleggiato film
                self.rented_film[clientID].append(film)  # Aggiunge il film alla lista
            else:
                self.rented_film[clientID] = [film]  # Crea una nuova lista per il cliente
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")

    def giveBack(self, film, clientID, days):
        """
        Restituisce un film precedentemente noleggiato.

        Args:
        - film: l'oggetto Film da restituire.
        - clientID: l'ID del cliente che restituisce il film.
        - days: il numero di giorni per cui il cliente ha tenuto il film.
        """
        self.film_list.append(film)  # Aggiunge il film alla lista dei disponibili
        self.rented_film[clientID].remove(film)  # Rimuove il film dalla lista noleggiati
        penale = film.calcolaPenaleRitardo(days)  # Calcola la penale per il ritardo
        print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale} euro!")

    def printMovies(self):
        """
        Stampa l'elenco dei film disponibili in negozio.

        Returns:
        - Una stringa formattata contenente i titoli e i generi dei film disponibili.
        """
        output = "Film disponibili in negozio:\n"
        for film in self.film_list:
            output += f"{film.getTitle()} - {film.getGenere()}\n"
        return output

    def printRentMovies(self, clientID):
        """
        Stampa l'elenco dei film noleggiati da un cliente specifico.

        Args:
        - clientID: l'ID del cliente di cui stampare l'elenco dei film noleggiati.

        Returns:
        - Una stringa formattata contenente i titoli e i generi dei film noleggiati dal cliente.
        """
        if clientID in self.rented_film:  # Verifica se il cliente ha noleggiato film
            output = f"Film noleggiati dal cliente {clientID}:\n"
            for film in self.rented_film[clientID]:
                output += f"{film.getTitle()} - {film.getGenere()}\n"
            return output
        else:
            return f"Nessun film noleggiato dal cliente {clientID}."  # Nessun film noleggiato
