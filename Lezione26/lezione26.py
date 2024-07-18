'''
Esercizio: Codificatori di un messaggio
Completion requirements
# Codificatori Messaggio
Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro 
sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), dove testoCodificato 
sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. 
Il costruttore dovrebbe ricevere un numero intero chiamato chiave. Si definisca il metodo codifica(testoInChiaro) così che ogni 
lettera del testo sia spostata dal valore contenuto in chiave.
Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', la lettera 'c' sarà 
sostituita da 'f' e così via.

     Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c 
     da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).


Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. 
Il costruttore dovrebbe ricevere un numero intero chiamato n. Si definisca il metodo codifica(testoInChiaro) così che il messaggio 
sia combinato n volte. Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna 
delle metà in modo alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza 
del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). Il messaggio combinato è 'afbgchdie'.

    Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni il testo 
    cifrato da usare nel metodo codifica(testoInChiaro).


Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

    Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie un'azione inversa al 
    metodo sposta_carattere().

    Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa 
    al metodo combinazione().


Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file 
per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

### Test tramite codice driver:
Test del Cifratore a Scorrimento:
- Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.

Test del Cifratore a Combinazione:
- Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.
'''

# Gioele Amendola
# 18/07/2024

from abc import ABC, abstractmethod
# # Codificatori Messaggio
# Si crei una classe astratta chiamata CodificatoreMessaggio 
# che ha un solo metodo astratto codifica(testoInChiaro),
# dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.
class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str):
        pass
# Si crei una classe astratta chiamata DecodificatoreMessaggio
# che abbia un solo metodo decodifica(testoCodificato),
# dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.
class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str):
        pass

# Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio.
#  Il costruttore dovrebbe ricevere un numero intero chiamato chiave.
#  Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.
# Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd',
#  la lettera 'b' sarà sostituita da 'e', la lettera 'c' sarà sostituita da 'f' e così via.
#  Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c
#  da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).
class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave: int):
        self.chiave: int = chiave
    
    def __sposta_carattere(self, char: str) -> str:
        if char.isalpha():
            if char.isupper():
                return chr((ord(char) - ord('A') + self.chiave) % 26 + ord('A'))
            else:
                return chr((ord(char) - ord('a') + self.chiave) % 26 + ord('a'))
        return char

    def __decodifica_carattere(self, char: str) -> str:
        if char.isalpha():
            if char.isupper():
                return chr((ord(char) - ord('A') - self.chiave) % 26 + ord('A'))
            else:
                return chr((ord(char) - ord('a') - self.chiave) % 26 + ord('a'))
        return char

    def codifica(self, testoInChiaro: str):
        testoCodificato: str = ""
        for c in testoInChiaro:
            testoCodificato += self.__sposta_carattere(c)
        return testoCodificato

    def decodifica(self, testoCodificato: str):
        testoDecodificato: str = ""
        for c in testoCodificato:
            testoDecodificato += self.__decodifica_carattere(c)
        return testoDecodificato

    def leggi_file(self, path: str):
        with open(path, 'r') as file:
            return file.read()
    
    def scrivi_file(self, path: str, testo: str):
        with open(path, 'w') as file:
            file.write(testo)

# Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio.
#  Il costruttore dovrebbe ricevere un numero intero chiamato n.
#  Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte.
#  Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo
#  alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi'
#  (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà).
#  Il messaggio combinato è 'afbgchdie'.
# Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni
#  il testo cifrato da usare nel metodo codifica(testoInChiaro).
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int):
        self.n: int = n
    
    def __combinazione(self, testo: str) -> str:
        if len(testo)%2 == 0:
            length: int = len(testo)//2
        else:
            length: int = len(testo)//2 + 1
        half1: str = testo[:length]
        half2: str = testo[length:]
        result: str = ""
        for i in range(len(half2)):
            result += half1[i] + half2[i]
        if len(testo)%2 != 0:
            result += half1[-1]
        return result
    
    def __decodifica_combinazione(self, testo: str) -> str:
        length: int = len(testo)
        half1: str = ""
        half2: str = ""
        for i in range(length):
            if i % 2 == 0:
                half1 += testo[i]
            else:
                half2 += testo[i]
        return half1 + half2
    
    def codifica(self, testoInChiaro: str):
        testoCodificato: str = self.__combinazione(testoInChiaro)
        return testoCodificato
    
    def decodifica(self, testoCodificato: str):
        testoDecodificato: str = self.__decodifica_combinazione(testoCodificato)
        return testoDecodificato
    
    def leggi_file(self, path: str):
        with open(path, 'r') as file:
            return file.read()
    
    def scrivi_file(self, path: str, testo: str):
        with open(path, 'w') as file:
            file.write(testo)
    
# Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

# Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento
#  che compie un'azione inversa al metodo sposta_carattere().
# Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa al metodo combinazione().

# Infine, si implementi anche un metodo per leggere il testo da cifrare da un file
# e un metodo per scrivere il testo cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

# ### Test tramite codice driver:
# Test del Cifratore a Scorrimento:
# - Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
cifratoreScorrimento: CifratoreAScorrimento = CifratoreAScorrimento(3)
# - Lettura del testo: Il testo in chiaro viene letto da un file.
testoInChiaro: str = cifratoreScorrimento.leggi_file("Lezione26/codificare.txt")
# - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
testoCodificato: str = cifratoreScorrimento.codifica(testoInChiaro)
# - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
cifratoreScorrimento.scrivi_file("Lezione26/codificatoScorrimento.txt", testoCodificato)
# - Stampa del testo codificato: Il testo codificato viene stampato.
print(testoCodificato)
# - Decodifica: Il testo codificato viene decodificato.
testoDecodificato: str = cifratoreScorrimento.decodifica(testoCodificato)
# - Stampa del testo decodificato: Il testo decodificato viene stampato.
print(testoDecodificato)

# Test del Cifratore a Combinazione:
# - Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
cifratoreCombinazione: CifratoreACombinazione = CifratoreACombinazione(3)
# - Lettura del testo: Il testo in chiaro viene letto da un file.
testoInChiaro = cifratoreCombinazione.leggi_file("Lezione26/codificare.txt")
# - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
testoCodificato = cifratoreCombinazione.codifica(testoInChiaro)
# - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
cifratoreCombinazione.scrivi_file("Lezione26/codificatoCombinazione.txt", testoCodificato)
# - Stampa del testo codificato: Il testo codificato viene stampato.
print(testoCodificato)
# - Decodifica: Il testo codificato viene decodificato.
testoDecodificato = cifratoreCombinazione.decodifica(testoCodificato)
# - Stampa del testo decodificato: Il testo decodificato viene stampato.
print(testoDecodificato)