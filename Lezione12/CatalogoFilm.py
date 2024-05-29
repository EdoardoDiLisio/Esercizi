#  EDOARDO DI LISIO
#  29/05/24

'''
Catalogo Film :
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.
Classe:
- MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.
    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.
    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.
    - list_directors(): Elenca tutti i registi presenti nel catalogo.
    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.
    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
'''
class MovieCatalog:
    def __init__(self):
        # Inizializza il catalogo come un dizionario vuoto
        self.catalog = {}

    def add_movie(self, director_name, movies):
        # Aggiunge uno o più film a un regista specifico nel catalogo
        if director_name not in self.catalog:
            # Se il regista non esiste, crea un nuovo record nel catalogo
            self.catalog[director_name] = movies
        else:
            # Se il regista esiste, aggiorna la sua lista di film
            self.catalog[director_name].extend(movies)

    def remove_movie(self, director_name, movie_name):
        # Rimuove un film specifico dall'elenco dei film di un regista
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                # Se il film esiste nella lista del regista, rimuovilo
                self.catalog[director_name].remove(movie_name)
                # Se tutti i film sono stati rimossi, rimuovi anche il regista
                if not self.catalog[director_name]:
                    del self.catalog[director_name]
                return True  # Indica che il film è stato rimosso con successo
        return False  # Indica che il film non è stato trovato o il regista non esiste

    def list_directors(self):
        # Restituisce una lista dei registi presenti nel catalogo
        return list(self.catalog.keys())

    def get_movies_by_director(self, director_name):
        # Restituisce tutti i film di un regista specifico
        return self.catalog.get(director_name, [])  # Restituisce una lista vuota se il regista non esiste

    def search_movies_by_title(self, title):
        # Trova tutti i film che contengono una certa parola nel titolo
        found_movies = {}
        for director, movies in self.catalog.items():
            for movie in movies:
                if title.lower() in movie.lower():
                    # Se il titolo del film contiene la parola cercata, aggiungilo alla lista dei film trovati
                    if director not in found_movies:
                        found_movies[director] = [movie]
                    else:
                        found_movies[director].append(movie)
        if not found_movies:
            # Se nessun film è stato trovato con la parola cercata nel titolo, restituisci un messaggio di errore
            return "Nessun film trovato con il titolo contenente '{}'.".format(title)
        else:
            return found_movies


# Esempio di utilizzo del sistema
if __name__ == "__main__":
    catalogo = MovieCatalog()

    # Aggiungere film
    catalogo.add_movie("Christopher Nolan", ["Inception", "Interstellar", "The Dark Knight"])
    catalogo.add_movie("Quentin Tarantino", ["Pulp Fiction", "Django Unchained", "Kill Bill"])
    catalogo.add_movie("Martin Scorsese", ["The Irishman", "The Departed", "Goodfellas"])

    # Elencare i registi
    print("Registi nel catalogo:", catalogo.list_directors())

    # Ottenere i film di un regista
    print("Film di Christopher Nolan:", catalogo.get_movies_by_director("Christopher Nolan"))

    # Rimuovere un film
    catalogo.remove_movie("Martin Scorsese", "The Irishman")
    print("Film di Martin Scorsese dopo la rimozione:", catalogo.get_movies_by_director("Martin Scorsese"))

    # Cerca film per titolo
    print("Cerca film con 'Dark':", catalogo.search_movies_by_title("Dark"))
