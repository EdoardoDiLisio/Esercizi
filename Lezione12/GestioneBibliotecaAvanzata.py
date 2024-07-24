#  EDOARDO DI LISIO
#  29/05/24
'''
Sistema Avanzato di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali 
libri sono disponibili in un dato momento.
Classi:
- Libro: Rappresenta un libro con titolo, autore, stao del prestito. Il libro deve essere inizialmente disponibile (non prestato).
- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.
    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. 
    Restituisce un messaggio di stato.
    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. 
    Restituisce un messaggio di stato.
    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, 
    restituisce un messaggio di errore.
Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
'''

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.prestato = False

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f"Il libro '{libro.titolo}' di {libro.autore} è stato aggiunto al catalogo."

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.prestato:
                    return f"Il libro '{titolo}' è già stato prestato."
                else:
                    libro.prestato = True
                    return f"Il libro '{titolo}' è stato prestato con successo."
        return f"Il libro '{titolo}' non è disponibile nella biblioteca."

    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.prestato:
                    libro.prestato = False
                    return f"Il libro '{titolo}' è stato restituito con successo."
                else:
                    return f"Il libro '{titolo}' non è stato prestato."
        return f"Il libro '{titolo}' non è disponibile nella biblioteca."

    def mostra_libri_disponibili(self):
        libri_disponibili = [libro.titolo for libro in self.catalogo if not libro.prestato]
        if libri_disponibili:
            return "Libri disponibili: " + ", ".join(libri_disponibili)
        else:
            return "Nessun libro disponibile al momento."


# Test del sistema
biblioteca = Biblioteca()

# Aggiunta dei libri
libro1 = Libro("Il signore degli anelli", "J.R.R. Tolkien")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("Harry Potter e la pietra filosofale", "J.K. Rowling")

print(biblioteca.aggiungi_libro(libro1))
print(biblioteca.aggiungi_libro(libro2))
print(biblioteca.aggiungi_libro(libro3))

# Prestito di un libro
print(biblioteca.presta_libro("1984"))
print(biblioteca.presta_libro("1984"))  # Tentativo di prendere in prestito lo stesso libro di nuovo

# Restituzione di un libro
print(biblioteca.restituisci_libro("1984"))

# Mostra libri disponibili
print(biblioteca.mostra_libri_disponibili())
