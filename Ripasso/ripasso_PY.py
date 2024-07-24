

#Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. 
#Ogni carta ha un valore compreso tra 2 e 11 compresi. Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, 
#a seconda di quale sia più favorevole al giocatore in quel momento. Dato un elenco di valori delle carte che rappresentano una mano di blackjack,
# scrivi una funzione per determinare il valore totale della mano.


def blackjack_hand_total(cards: list[int]) -> int:
    total = sum(cards)
    if total>21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
            return sum(cards)
    else:
        return total
    

#Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

#1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
#2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
#3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

#Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

#Esempio:

#construct_rectangle(4)

#L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
#Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. 
#Quindi la lunghezza L è 2 e la larghezza W è 2.
def construct_rectangle(area: float) -> list[float]:
    min_diff = area - 1
    result = [area, 1]
    
    for i in range(2, int(area**0.5) + 1):
        if area % i == 0:
            j = area // i
            if j >= i and j - i < min_diff:
                min_diff = j - i
                result = [j, i]
    return result


#Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. 
#Restituisce l'elenco riorganizzato.

def even_odd_pattern(nums: list[int]) -> list[int]:
    pari = [x for x in nums if x% 2 == 0]
    dispari = [x for x in nums if x% 2 != 0]
    ritorna = pari+dispari
    return ritorna
    

#Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative 
#comuni stop_words e restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente 
#(ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    word: str = ""
    Text: dict = {}
    for char in text:
        if char in [" ", ".", ",", ":", ";", "!", "?"]:
            if word is not stopwords and word !="":
                if word not in Text.keys():
                    Text[word] = 1
                else:
                    Text[word] +=1
            word = ""
        else:
            word += char.lower()
    return Text






'''
-> -> Test e Unittest
+3 Quali sono i due principali framework per unit test in Python?
unittest e PyTest
-
+3Quale convenzione devono seguire gli header dei metodi di test in unittest?
I  nomi dei metodi devono iniziare con la parola test
-
Quale modulo deve contenere una directory per essere considerata importabile per i test?
__init__.py
-
+1 Quale metodo viene utilizzato per verificare se un valore è True in unittest?
assertTrue
-
Come si passa un messaggio personalizzato a un'asserzione in Python?
assert condizione, 'messaggio'
-
+1Qual è la classe base utilizzata per creare test case in unittest?
TestCase
-
Qual è il risultato dell'istruzione assert 1 < 0?
setUp
-
+1Cosa succede se si lancia un'asserzione con una condizione falsa senza fornire un messaggio?
un'AssertionError senza messaggio
-
Cos'è un'asserzione (assert) in Python?
Una parola chiave di python che verifica se una condizione/valore è vera o falsa
-
+1 Quale metodo viene utilizzato per verificare se una condizione è vera in unitest
asserTrue
-
+1Quale metodo viene utilizzato per verificare l'uguaglianza in unittest?
assertEqual
-
Quale comando esegue i test unittest modalità verbosa?
python -m unittest -v
-
Quale comando permette di visualizzare informazioni dettagliate su test eseguiti con unittest?
python -m unittest -v
-
+1qual è il risultato dell'istruzione assert 1<0?
AssertionError
-
+1Qual è lo scopo del metodo asserRaises in unittest?
verificare se viene sollevata un'eccezione specifica
-
quale comando esegue un singolo test case di unittest?
python -m unittest -v nome_file.TestNome
-
Qual è la classe base utilizzata per creare test case in unittest?
TestCase
-
Qual è il comando utilizzato per eseguire tutti i test in una directory in Python?
python -m unittest
-
Cosa verifica il metodo di assertIsNone in unittest?
verifica se la variabile è None
--------------------------------------------------------------------------
-> -> Conoscenza su File
+3Quale metodo di lettura legge una singola linea alla volta fino a incontrare il token EOF?
readline()
-
+1Quale metodo di lettura legge tutte le linee di un file e le mette in una lista?
readlines()
-
+3Quale carattere viene utilizzato per ottenere una nuova linea durante la scrittura su un file?
\n
-
+2Cosa rappresenta il metodo __enter__ di un context manager in Python?
Il metodo chiamato quando il flusso di esecuzione entra nel blocco with
-
+1Quale funzione viene chiamata per chiudere un file aperto in Python?
close()
-
Quale metodo viene utilizzato per assicurarsi che un file venga chiuso correttamente, anche in caso di errore?
with statement
-
Qual è il formato di default per aprire un file in Python?
'r'
-
+2Quale tipo di eccezione viene sollevata se si tenta di aprire un file che non esiste in modalità read?
FileNotFoundError
-
Qual è la funzione in Python utilizzata per aprire un file?
open()
-
+1Qual è la modalità di apertura di default per la funzione open() in Python?
read-only
-
Quale carattere speciale indica la fine di un file?
EOF
-
+1Quale metodo viene utilizzato per scrivere una stringa in un file?
write()
-
+1Quale modulo di Python fornisce funzioni per lavorare con il sistema operativo, incluso
os
-
+2Cosa rappresenta il metodo __exit__ di un context manager in Python?
il metodo chiamato quando il flusso di esecuzione esce dal blocco with, indipendentemente dal fatto che sia verificata un'accezione o meno
-
Quale carattere speciale indica la fine di un file?
EOF
-
Qual è il metodo per scrivere una lista di stringhe in un file?
writelines()
-cosa rappresenta un file in un sistema operativo moderno?
un insieme congruo di byte utilizzati per memorizzare dati
-Qual è il metodo consigliato per aprire e chiudere file in pyton per garantire un codice 
with statement

----------------------------------------------------------


Merge Sort/Algoritmi
+2Qual è il paradigma su cui si basa l'algoritmo Merge Sort?
Divide et impera
-
Qual è un vantaggio dell'algoritmo Merge Sort rispetto a Bubble Sort?
Ha una complessità temporale migliore
-
+1Qual è la complessità temporale di un algoritmo che esegue un'operazione indipendentemente dalla dimensione dell'input?
O(1)
-
+1Qual è la complessità temporale della soluzione iterativa per calcolare i numeri di Fibonacci?
O(n)
-
Qual è la complessità temporale di Bubble Sort?
O(n^2)
-
Qual è un esempio di algoritmo con complessità O(log n)?
Ricerca binaria
-
+1Qual è la complessità temporale di un algoritmo che ha una crescita quadratica con la dimensione dell'input?
O(n^2)
-
+2Qual è la complessità temporale di un algoritmo che ha una crescita fattoriale con la dimensione dell'input?
O(n!)
-
Qual è la complessità temporale dell'algoritmo ricorsivo per calcolare il numero di Fibonacci?
O(2^n)
-
+1Qual è la complessità temporale di un algoritmo che esplora una matrice quadrata?
O(n^2)
-
+1Qual è la caratteristica principale degli algoritmi con complessità o(1)?
il tempo di esecuzione è costante e non dipende dalla dimensione dell'Imput
-
+1Che cos'è la sequenza Fibonacci?
Una sequenza di numeri interi in cui ciascun numero è la somma dei due precedenti
-
+1QUal è la comoplessità temporale di Bubble Sort nel caso peggiore?
O(n^2)
-
Qual è il primo passo dell'algoritmo Merge Sort?
Dividere il problema in sottoproblemi più piccoli
-
QUal è un esempio di algoritmo con complessità O(n log n)?
Merge Sort
-
Qual è la complessità temporale di un Bubble Sort?
O(n^2)
-
"Qual è la complessità temporale della ricerca binaria?"
O(log n)
-
qual' è la complessità temporale di Merge Sort?
O(n log n)

------------------------------------------
Conoscenze su Decorators
+1Quale delle seguenti non è una caratteristica delle funzioni in Python? (Leggere attentamente la domanda)
Possono essere utilizzate solo come decoratori
-
+1Cosa succede se si passa una funzione con le parentesi come argomento a un'altra funzione?
La funzione viene eseguita immediatamente e viene passato il valore ritornato
-
+2Quale parola chiave viene utilizzata per definire una funzione in Python?
def
-
+1Cosa permette di fare la funzione wrapper() all'interno di un decoratore?
Avvolge la funzione originale e ne modifica il comportamento
-
+1Qual è il vantaggio principale dell'utilizzo dei decoratori?
Modificare facilmente il comportamento delle funzioni senza modificarne il codice
-
+2Qual è lo scopo di un decoratore in Python?
Modificare il comportamento di una funzione
-
+2Qual è la differenza tra una funzione con parentesi e una funzione senza parentesi passata come argomento?
La funzione con parentesi viene eseguita, mentre quella senza parentesi viene passata come referenza
-
+2Quale simbolo viene utilizzato per applicare un decoratore a una funzione?
@
-
+2 in Python, cosa significa che le funzioni sono oggetti di prima classe?
Possono essere passate e utilizzate come argomenti, proprio come qualsiasi altro oggetto
-
+1Qual è la funzione di un decoratore in Python?
È una funzione che avvolge un'altra funzione, modificandone il comportamento
-
Quale dei seguenti non è un esempio di utilizzo di decoratori?
Stampare informazioni / aumentare la velocità di esecuzione delle funzioni
-
+1Qual è il principale vantaggio di utilizzare le funzioni come oggetti di prima classe?
permette di passare, restituire e assegnare funzioni come variabili
-
Qual è il comportamento della funzione passata come argomento senza parentesi?
viene passata solo una referenza alla funzione senza eseguirla


--------------------------------------------------------------------------
 Conoscenze su Eccezioni
+1Qual è la classe base per la maggior parte delle eccezioni incorporate in Python?
Exception
-
+1Quale parola chiave viene utilizzata in Python per sollevare un'eccezione?
raise
-
Come si specifica un messaggio personalizzato in un'asserzione?
assert condizione, 'messaggio'
-
+1Come si può creare un'eccezione personalizzata in Python?
Ereditando da Exception
-
+2Come si può catturare qualsiasi eccezione generica?
except Exception as e
-
+2Quale blocco di codice viene utilizzato in Python per gestire le eccezioni?
try-except
-
Qual è lo scopo del blocco try in Python?
Tentare di eseguire il codice che potrebbe generare un'eccezione
-
Cosa succede se un'asserzione fallisce?
Viene sollevata un'AssertionError
-
+1Quale clausola viene utilizzata per eseguire azioni di pulizia dopo l'esecuzione del codice?
finally
-
+3Quale eccezione viene sollevata quando un'operazione di I/O fallisce?
IOError
-
+2Quale eccezione viene sollevata quando un operazione aritmetica non valida viene eseguita?
ArithmeticError
-
+1Qual è l'output di assert 1>0
Nessun output
-
1+Quale clausola si utilizza per eseguire il codice solo se non viene sollevata alcuna eccezione all'interno del blocco try?
Else
-
+3Qual è la differenza tra un'asserzione e un'accezione
Un asserzione verifica una condizione, un'eccezione gestisce errori
-
+1Come si specifica una clausola except che cattura solo un'eccezione
except TypeError as e
-
qual è la classe base per la maggior parte delle
BaseException
-
Qual è lo scopo del blocco try di Python?
Tentare di eseguire il codice che potrebbe generare un'eccezione
-
Qual è lo scopo della clausola finally in un blocco try-except?
Eseguire il codice di pulizia indipendentemente da
-
Quale eccezione viene sollevata quando si accede a una variabile non definita in Python?
NameError
-
Quale eccezione viene sollevata quando si tenta di dividere un numero per zero?
ZeroDivisionError
-
Cosa succede se un'asserzione fallisce?
viene sollevata un'AssertionError
-

___________________________________________________________

Threads
+1Qual è il metodo alternativo per ottenere l'esecuzione parallela in Python senza i limiti del GIL?
Utilizzare multiprocessing
-
+1Quale metodo viene utilizzato per proteggere le variabili condivise in un ambiente multi-thread?
Aggiungere lock
-
+1Qual è il vantaggio dell'utilizzo del GIL rispetto all'aggiunta di lock a tutte le strutture dati?
Previene i Dead Lock
-
+1Come si avvia un nuovo thread in Python?
Creando un'istanza di Thread e chiamando .start()
-
Cosa rappresenta un programma CPU-bound?
Un programma che spinge la CPU al limite
-
+1Qual è un potenziale problema dell'aggiunta di lock a tutte le strutture dati condivise?
Deadlock
-
+2Cosa rappresenta un thread in Python?
Un flusso separato di esecuzione
-
+1Cosa può causare un race condition nella gestione della memoria?
Due thread che modificano il conteggio dei riferimenti simultaneamente
-
+2Quale funzione deve essere passata a un'istanza di Thread?
Una funzione da eseguire nel nuovo thread
-
+1Perché è consigliato utilizzare ThreadPoolExecutor come context manager?
Per assicurarsi che i thread vengano uniti e chiusi correttamente
-
+1In quale scenario i thread sono particolarmente utili?
quando i compiti attendono eventi esterni
-
+1Qual è la soluzione per proteggere il conteggio dei riferimenti in un ambito multi-threading in Python?
aggiungere lock a tutte le strutture dati condivise
-
Cosa rappresenta un programma CPU-bound?
un programma che spinge la CPU al limite 
-
+1Quale funzione utilizza Python per il conteggio dei riferimenti?
sys.getrefcount()
-
+2Che significa che Python tratta le funzioni come first-class objects?
le funzioni possono essere passate come argomenti e restituire da altre funzioni
-
cosa succede alla fine del blocco with wuando si utilizza thread 
esegue un .join() su ciascuno dei thread del pool
-
+1Cosa rappresenta un programma I/O-bound?
un programma che attende input/output
-
quale metodo viene utilizzato per avviare un gruppo thread
.map()
-
Qual è lo scopo della funzione ThreadPoolExecutor in Python?
gestire un pool di thread
-
+1Qual è il problema principale di GIL?
può essere un collo di bottiglia per le prestazioni del programma
-
quale metodo python utilizza per la gestione della memoria?
reference counting
-
Perché il GIL è considerato un problema?
Perché limita le prestazioni dei programmi multi-Thread
-
Quale libreria standard Python fornisce supporto per i Thread?
threading
_______________________________________________________________
Docker
Qual è il comando per eseguire un contenitore Docker?
docker run
-
+1Cosa significa che i container sono isolati?
Ogni container esegue un'applicazione e le sue dipendenze senza interferire con altri container
-
+2Qual è il vantaggio dell'utilizzo di Docker in sviluppo?
Assicura che l'applicazione funzioni allo stesso modo in diversi ambienti
-
Cosa include un container?
Codice, runtime, strumenti di sistema e librerie
-
+1Cosa significa che un container è "standalone"?
Può essere eseguito indipendentemente su qualsiasi sistema che supporti il runtime dei container
-
+1Qual è uno dei benefici della rapida distribuzione dei container?
Scalabilità
-
Qual è uno dei vantaggi principali dei container?
Portabilità
-
Quale problema risolvono i container rispetto alle VM in termini di portabilità?
I container sono progettati per essere indipendenti dalla piattaforma
-
+1Cos'è un Dockerfile?
Un file con le istruzioni per costruire un'immagine Docker

21Qual è uno svantaggio delle macchine virtuali (VM)?
Consumo maggiore di risorse
-
Come si chiamano gli strumenti e servizi necessari per costruire, eseguire e distribuire applicazioni containerizzate?
Container engine
-
+1Cosa fa il comando docker run mytesting?
esegue il contenitore basato sull'immagine mytesting
-
+1Cos'è Docker?
Uno strumento per creare e gestire container
-
1+Cosa specifica l'istruzione "CMD" in un Docker?
il comando da eseguire quando un conteiner viene avviato.
-
Cosa virtualizzano le macchine virtuali(VM)?
L'hardware
-Qual è un altro vantaggio dei container rispetto alle VM?
L'efficienza
-
Quale tecnologia permettedi creare ambienti simulati su una singola macchina?
Virtualizzazione
-
cosa fa il comando "WORKDIR /app" in un dockerfile?
cambia la directory di lavoro nel container a /app

____________________________________________________________________________________________________
Multiprocessing
Qual è la differenza tra multiprocessing e threading in Python?
Multiprocessing crea processi separati con la propria memoria, mentre threading crea thread all'interno dello stesso processo con memoria condivisa
-
Come si può far sì che il processo principale attenda la fine dei processi figli?
Usando il metodo join
-
Quale metodo della classe Process consente di attendere la terminazione di un processo figlio?
join()
-
Cosa succede se non si utilizza il metodo join in un programma con multiprocessing?
Il programma principale può terminare prima che i processi figli abbiano finito
-
Qual è lo scopo del metodo start() nella libreria multiprocessing?
Avviare un nuovo processo
-
Che cosa si intende per overhead in un contesto di multiprocessing?
Il costo aggiuntivo in termini di risorse computazionali per gestire i processi
-
Quale comando della libreria multiprocessing permette di creare un nuovo processo?
Process()
-
Qual è la differenza principale tra un thread e un processo?
Un thread è un flusso di esecuzione separato all'interno di un processo; un processo è un'istanza di un programma in esecuzione
-
Quando è preferibile utilizzare il multiprocessing rispetto al threading?
Quando si eseguono operazioni CPU-bound
-
Che cosa significa GIL in Python?
Global Interpreter Lock
-
Che cos'è un deadlock in un contesto di multiprocessing?
due processi che si bloccano a vicenda
-
Qual è il vantaggio principale dell'uso del multiprocessing rispetto al threading per i compiti CPU-bound?
Il multiprocessing può sfruttare più core del processore
-
130

Quale metodo viene utilizzato per verificare se una condizione è vera in unittest?
assertTrue

Cosa succede se un'asserzione fallisce?
Viene sollevata un'AssertionError

Qual è il comportamento della funzione passata come argomento senza parentesi?
Viene passata solo una referenza alla funzione senza eseguirla

Come si chiamano gli strumenti e i servizi necessari per costruire,
eseguire e distribuire applicazioni containerizzate?
Container engine

Qual è il risultato dell'istruzione assert 1 < 0?
AssertionError

Cosa fa il comando "docker build -t mytesting ." ?
Costruisce un'immagine Docker con il tag mytesting

Qual è un altro vantaggio dei container rispetto alle VM?
Efficienza

Cosa rappresenta un programma CPU-bound?
Un programma che spinge la CPU al limite

Quando è preferibile utilizzare il multiprocessing rispetto al threading?
Quando si eseguono operazioni CPU-bound

Quale convenzione devono seguire gli header dei metodi di test in unittest?
I nomi dei metodi devono iniziare con la parola test

Quale metodo di lettura legge una singola linea alla volta fino a incontrare il token EOF?
readline()

Come si passa un messaggio personalizzato a un'asserzione in Python?
assert condizione as 'messaggio'

Quale metodo viene utilizzato per verificare se un valore è True in unittest?
assertTrue


Quale metodo viene utilizzato per proteggere le variabili condivise in un ambiente multi-thread?
Aggiungere Lock

Qual è il formato di default per aprire un file in Python?
'r'

Cosa virtualizzano le macchine virtuali (VM)?
L'Hardware

Cosa rappresenta un thread in Python?
Un flusso separato di esecuzione

Che cosa significa GIL in Python?
Global Interpreter Lock

Qual è il comando per eseguire un contenitore Docker?
Docker run

Qual è uno svantaggio delle macchine virtuali (VM)?
Consumo maggiore di risorse

Qual è uno dei vantaggi principali dei container?
Portabilità

Cosa verifica il metodo assertIsNone in unittest?
Verifica se una variabile è None

Qual è la funzione principale del GIL (Global Interpreter Lock) in Python?
Limitare l'esecuzione a un solo thread alla volta

Qual è il vantaggio dell'utilizzo di Docker in sviluppo?
Assicura che l'applicazione funzioni allo stesso modo in diversi ambienti

Cosa fa l'istruzione else in un blocco try-except?
Esegue un blocco di codice solo in assenza di eccezioni

Qual è lo scopo del metodo assertRaises in unittest?
Verificare se viene sollevata un'eccezione specifica

Che cos'è un deadlock in un contesto di multiprocessing?
Una situazione in cui due o più processi si bloccano a vicenda aspettando risorse

Qual è il metodo utilizzato per scrivere una lista di stringhe in un file?
writelines()

Quale funzione deve essere passata a un'istanza di Thread?
Una funzione da eseguire nel nuovo thread

Cosa succede se non si utilizza il metodo join in un programma con multiprocessing?
Il programma principale può terminare prima che i processi figli abbiano finito

Quale comando esegue i test unittest in modalità verbosa?
python -m unittest -v

Quale eccezione viene sollevata quando si tenta di dividere un numero per zero?
ZeroDivisionError

Quale metodo viene eseguito prima di ogni test in una classe di test unittest?
setUp()

Come si può creare un'eccezione personalizzata in Python?
Ereditando da Exception

Cosa specifica l'istruzione "CMD" in un Dockerfile?
Il comando da eseguire quando il container viene avviato

Come si definisce una funzione all'interno di un'altra funzione in Python?
Inner function

Quale problema risolvono i container rispetto alle VM in termini di portabilità?
I container sono progettati per essere indipendenti dalla piattaforma

Qual è il vantaggio principale dell'utilizzo dei decoratori?
Modificare facilmente il comportamento delle funzioni senza modificarne il codice

Quale problema comune si verifica quando si dimentica di chiudere un file in Python?
Memory Leak

Qual è la soluzione per proteggere il conteggio dei riferimenti in un ambiente multi-thread?
Aggiungere lock a tutte le strutture dati condivise

Cosa include un container?
Codice, runtime, strumenti di sistema e librerie

Come si avvia un nuovo thread in Python?
Creando un'istanza di Thread e chiamando .start()

Qual è la differenza tra multiprocessing e threading in Python?
Multiprocessing crea processi separati con la propria memoria, mentre threading crea thread all'interno dello stesso processo con memoria condivisa

Cosa rappresenta un file in un sistema operativo moderno?
Un insieme contiguo di byte utilizzati per memorizzare dati

Cosa fa il comando "docker run mytesting" ?
Esegue il contenitore basato sull'immagine mytesting

Cosa fa il comando "WORKDIR /app" in un Dockerfile?
Cambia la directory di lavoro nel container a /app

Cosa significa che i container sono isolati?
Ogni container esegue un'applicazione e le sue dipendenze senza interferire con altri container

Cos'è Docker?
Uno strumento per creare e gestire container

Qual è la differenza tra una funzione con parentesi e una funzione senza parentesi passata come argomento?
La funzione con parentesi viene eseguita, mentre quella senza parentesi viene passata come referenza

Qual è l'effetto del GIL su un programma CPU-bound?
Limita le prestazioni a un singolo core della CPU

Come si chiama il processo di avvolgere una funzione con un decoratore?
Decorazione

Quale eccezione viene sollevata quando un'operazione di I/O fallisce?
IOError

Quale comando della libreria multiprocessing permette di creare un nuovo processo?
Process()

Quale metodo viene utilizzato per avviare un gruppo di thread con ThreadPoolExecutor?
.map()

Quali sono i due principali framework per unit test in Python?
unittest e PyTest

Cosa succede se si passa una funzione con le parentesi come argomento a un'altra funzione?
La funzione viene eseguita immediatamente e viene passato il valore ritornato

Quale libreria Python è utilizzata per il multiprocessing?
multiprocessing

Cosa rappresenta il metodo __exit__ di un context manager in Python?
Il metodo chiamato quando il flusso di esecuzione esce dal blocco with, indipendentemente dal fatto che si sia verificata un'eccezione o meno

Quali sono le tre parti principali che compongono un file su sistemi moderni?
Header,Data,EOF(End Of File)

Qual è il principale vantaggio di utilizzare le funzioni come oggetti di prima classe?
Permette di passare, restituire e assegnare funzioni come variabili

Cos'è una macchina virtuale (VM)?
Un ambiente simulato creato tramite virtualizzazione

Qual è la differenza principale tra un thread e un processo?
Un thread è un flusso di esecuzione separato all'interno di un processo; un processo è un'istanza di un programma in esecuzione

In quale scenario i thread sono particolarmente utili?
Quando i compiti attendono eventi esterni

Come si può far sì che il processo principale attenda la fine dei processi figli?
Usando il metodo join

Quale modulo deve contenere una directory per essere considerata importabile per i test?
__init__.py

Come si solleva un'eccezione con un messaggio personalizzato?
raise Exception('messaggio')

Quale dei seguenti non è un esempio di utilizzo dei decoratori?
Aumentare la velocità di esecuzione delle funzioni

Quale comando esegue una singola funzione di test all'interno di un file di test con unittest?
python -m unittest -v nome_file.nome_funzione

Quale parola chiave viene utilizzata in Python per sollevare un'eccezione?
raise

Quale metodo della classe Process consente di attendere la terminazione di un processo figlio?
join()

In Python, cosa significa che le funzioni sono oggetti di prima classe?
Possono essere passate e utilizzate come argomenti, proprio come qualsiasi altro oggetto

Qual è lo scopo di un decoratore in Python?
Modificare il comportamento di una funzione

Quale metodo di lettura legge tutte le linee di un file e le mette in una lista?
readlines()

Cosa rappresenta un programma I/O-bound?
Un programma che attende input/output

Quale simbolo viene utilizzato per applicare un decoratore a una funzione?
@

Come si specifica un messaggio personalizzato in un'asserzione?
assert condizione, 'messaggio'

Quale delle seguenti non è una caratteristica delle funzioni in Python?
Possono essere utilizzate solo come decoratori

Qual è la classe base utilizzata per creare test case in unittest?
TestCase

Perché il GIL è considerato un problema?
Perché limita le prestazioni dei programmi multi-thread

Che cosa si intende per overhead in un contesto di multiprocessing?
Il costo aggiuntivo in termini di risorse computazionali per gestire i processi

Cosa succede se si lancia un'asserzione con una condizione falsa senza fornire un messaggio?
Viene sollevata un'AssertionError senza messaggio

Qual è il metodo alternativo per ottenere l'esecuzione parallela in Python senza i limiti del GIL?
Utilizzare multiprocessing

Qual è il problema principale del GIL?
Può essere un collo di bottiglia per le prestazioni in programmi multi-thread

Quale modulo in Python fornisce funzioni per lavorare con il sistema operativo, inclusa la gestione dei file?
os

Quale tecnologia permette di creare ambienti simulati su una singola macchina fisica?
Virtualizzazione

Quale modulo include ThreadPoolExecutor?
concurrent.futures

Qual è il vantaggio principale dell'uso del multiprocessing rispetto al threading per compiti CPU-bound?
Il multiprocessing può sfruttare più core del processore

Qual è lo scopo del metodo start() nella libreria multiprocessing?
Avviare un nuovo processo

Quale metodo Python utilizza per la gestione della memoria?
Reference counting

Quale funzione utilizza Python per il conteggio dei riferimenti?
sys.getrefcount()

Quale tipo di eccezione viene sollevata se si tenta di aprire un file che non esiste in modalità read?
FileNotFoundError

Cos'è un'asserzione (assert) in Python?
Una parola chiave di python che verifica se una condizione/valore è vera o falsa

Quale clausola si utilizza per eseguire il codice solo se non ci sono eccezioni?
else

Cosa fa l'istruzione "COPY . /app" in un Dockerfile?
Copia i contenuti della directory corrente nella directory /app all'interno del container

Quale comando permette di visualizzare informazioni dettagliate sui test eseguiti con unittest?
python -m unittest -v

Quale clausola viene utilizzata per eseguire azioni di pulizia dopo l'esecuzione del codice?
finally

Qual è lo scopo del blocco try in Python?
Tentare di eseguire il codice che potrebbe generare un'eccezione

Quale carattere speciale indica la fine di un file?
EOF

Cosa permette di fare la funzione wrapper() all'interno di un decoratore?
Avvolge la funzione originale e ne modifica il comportamento

Come si specifica una clausola except che cattura solo l'eccezione TypeError?
except e: TypeError

Quale metodo viene utilizzato per assicurarsi che un file venga chiuso correttamente, anche in caso di errore?
with statement

Quale eccezione viene sollevata quando un'operazione aritmetica non valida viene eseguita?
MathError

Quale metodo viene utilizzato per verificare l'uguaglianza in unittest?
assertEqual

Qual è uno dei benefici della rapida distribuzione dei container?
Scalabilità

Qual è lo scopo della clausola finally in un blocco try-except?
Eseguire il codice di pulizia indipendentemente dal risultato del blocco try

Quale comando esegue un singolo test case in unittest?
python -m unittest nome_file.TestNome

Cosa significa che Python tratta le funzioni come first-class objects?
Le funzioni possono essere passate come argomenti e restituite da altre funzioni

Qual è la funzione in Python utilizzata per aprire un file?
open()

Cosa succede alla fine del blocco with quando si utilizza ThreadPoolExecutor?
Esegue un .join() su ciascuno dei thread nel pool

Quale libreria standard Python fornisce il supporto per i thread?
threading

Qual è un esempio di programma che potrebbe beneficiare dell'uso dei thread?
Un programma che non richiede attesa

Perché è consigliato utilizzare ThreadPoolExecutor come context manager?
Per assicurarsi che i thread vengano uniti e chiusi correttamente

Quale funzione viene chiamata per chiudere un file aperto in Python?
close()

Quale blocco di codice viene utilizzato in Python per gestire le eccezioni?
try-except

Quale parola chiave viene utilizzata per definire una funzione in Python?
def

Qual è il metodo consigliato per aprire e chiudere file in Python per garantire un codice più pulito?
with statement

Cos'è un Dockerfile?
Un file con le istruzioni per costruire un'immagine Docker

Qual è un potenziale problema dell'aggiunta di lock a tutte le strutture dati condivise?
Deadlock

Quale carattere viene utilizzato per ottenere una nuova linea durante la scrittura su un file?
\n

Qual è il metodo utilizzato per scrivere una stringa in un file?
write()

Qual è il comando utilizzato per eseguire tutti i test in una directory in Python?
python -m unittest

Qual è il vantaggio dell'utilizzo del GIL rispetto all'aggiunta di lock a tutte le strutture dati?
Previene i deadlock

Qual è la funzione di ThreadPoolExecutor?
Gestire un pool di thread

Qual è l'output di assert 1 > 0 se la condizione è vera?
Nessun output

Come si può catturare qualsiasi eccezione generica?
except Exception as e

Qual è la differenza tra un'asserzione e un'eccezione?
Un'asserzione verifica una condizione, un'eccezione gestisce errori

Qual è l'effetto del GIL sui programmi multithreaded in Python?
Limita l'utilizzo effettivo dei threads ai programmi I/O Bounded

Cosa rappresenta il metodo __enter__ di un context manager in Python?
Il metodo chiamato quando il flusso di esecuzione entra nel blocco with

Quale eccezione viene sollevata quando si accede a una variabile non definita?
NameError

Qual è il metodo utilizzato per confrontare se due valori non sono uguali in unittest?
AssertNotEqual

Cosa significa che un container è "standalone"?
Può essere eseguito indipendentemente su qualsiasi sistema che supporti il runtime dei container

Qual è il comando per costruire un'immagine Docker da un Dockerfile?
docker Build

Quale argomento posizionale aggiuntivo viene comunemente utilizzato con la funzione open() per specificare come si desidera aprire il file?
mode

Cosa può causare un race condition nella gestione della memoria?
Due thread che modificano il conteggio dei riferimenti simultaneamente

Qual è la classe base per la maggior parte delle eccezioni incorporate in Python?
Exception

Come si esegue un singolo file di test con unittest?
python -m unittest -v nome_file

Qual è la modalità di apertura di default per la funzione open() in Python?
read-only

Qual è la funzione di un decoratore in Python?
È una funzione che avvolge un'altra funzione, modificandone il comportamento
'''
