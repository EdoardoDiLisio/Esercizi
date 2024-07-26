






#Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.


usernames = ["admin" ,"tizio", "caio", "sempronio" ,"pippo" ]
for username in usernames:
	if username == "admin":
		print : "Ciao admin! Vuoi vedere un report completo?"
	else:
		print (f"Ciao {username} benvenuto a bordo!")
		
		
#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.

usernames = [ ]
if usernames:
    for username in usernames:
        print(" Ciao {username}, grazie per esserti loggato oggi!")
else:
    print("Accidenti, ci servono più utenti!")
    

#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ["John", "Flea", "Chad", "Anhony", "Josh"]
new_users = ["Arik", "Dave", "George","John","Flea"]
current_users_lower = [user.lower() for user in current_users]


'''
Cosa fa il comando "ls" in un sistema Linux?
Mostra il contenuto di una directory
-
Quale dei seguenti comandi viene utilizzato per creare una nuova directory (cartella) in un sistema Linux?
mkdir
-
Quale comando viene utilizzato per visualizzare il percorso della directory corrente in Linux?
pwd
-
Quale dei seguenti comandi Linux viene utilizzato per spostare o rinominare file e directory?
mv
-
Quale comando in Linux viene utilizzato per eliminare un file o una directory?
rm
-
Quale comando viene utilizzato per cambiare la directory corrente in una directory specifica in un sistema Linux?
cd
-
Cosa rappresenta l'acronimo "CPU" nel contesto dell'hardware di un computer?
Central Processing Unit
-
Qual è il comando Linux per creare un file vuoto?
touch
-
Cosa rappresenta l'acronimo "RAM" nel contesto dell'hardware di un computer?
Random Access Memory
-
Quale componente dell'architettura di un computer è responsabile dell'esecuzione effettiva delle istruzioni?
CPU
-
Cosa fa il metodo strip() quando viene chiamato su una stringa in Python?
Rimuove gli spazi vuoti all"inizio e alla fine della stringa
-
Qual è il risultato dell'espressione 3 * "2" in Python?
222
-
Quale tipo di struttura dati viene utilizzato per memorizzare una collezione di elementi univoci in Python?
Insieme
-
Qual è il metodo utilizzato per unire più stringhe in Python?
.join()
-
Quale delle seguenti è una caratteristica di un set in Python?
Non può essere indicizzato
-
In Python, lo "scope" di una variabile all'interno di una funzione si riferisce a:
d. La visibilità della variabile all'interno della funzione
-
Quale operatore viene utilizzato per la concatenazione di due liste in Python?
+
Cosa restituirà l'espressione "Hello World"[::-1] in Python?
"dlroW olleH"
-
Cosa restituisce la funzione range(3, 10, 2) in Python?
Una lista di numeri da 3 a 10 (non compreso), con passo di 2
-
Qual è il tipo di dato del risultato di len('Python') in Python?
-
Qual è il tipo di dato del risultato di len('Python') in Python?
-
Question 1Answer
int
-
Quale operazione non è permessa con i tipi di dato int in Python?
Confronto con stringhe
-
Quale tipo di dato è il risultato di 5 / 2 in Python?
Float
-
Quale metodo stringa in Python restituisce una versione maiuscola della stringa?
upper()
-
Quale funzione può convertire un int in un float in Python?
Float()
-
In una rete point-to-point, come vengono trasferiti i dati?
I dati vengono inviati direttamente da un dispositivo a un altro attraverso un collegamento diretto.
-
Come sono configurati i dispositivi nella topologia a MESH di una rete?
Ogni dispositivo è collegato direttamente a ogni altro dispositivo
-
Quale affermazione descrive meglio una rete peer-to-peer (P2P)?
Ogni nodo può fungere da client o da server
-
Che cosa è 'anycast' nella comunicazione di rete?
Comunicazione uno-a-molti più vicini
-
Come vengono selezionati i percorsi in una rete point-to-point quando sono disponibili più percorsi?
Il percorso può essere selezionato sulla base della lunghezza o del traffico.
-
Qual è una caratteristica della topologia a BUS?
Utilizza un unico canale di comunicazione condiviso
-
Nella comunicazione di rete, cosa significa 'broadcast'?

Invio di messaggi a tutti i dispositivi nella rete
-
Quale delle seguenti affermazioni descrive meglio il modello client-server?
Un nodo centrale fornisce risorse e servizi agli altri nodi
-
Qual è una funzione primaria delle reti di computer?
Condividere risorse e informazioni tra dispositivi
-
Nel contesto delle reti di computer, cosa significa 'unicast'?
Il messaggio è inviato a un singolo dispositivo designato
-
Qual è il risultato dell'addizione dei numeri binari 1100 e 111?
10011
-
Considera l'espressione booleana: (A OR B) AND NOT (C AND D). 
Quale è il risultato di questa espressione quando A=0, B=1, C=1, D=0?
1
-
Converti il numero decimale 26 in un numero binario. Qual è il risultato corretto?
11010
-
Qual è il risultato della sottrazione dei numeri binari 10100 e 110 ?
01110
-
Come viene chiamato un gruppo di 8 bit?
Byte
-
Quante combinazioni distinte si possono creare con 4 bit?
sedici
-
Qual è l'intervallo di valori rappresentabili con 5 bit?
0 a 31
-
Quanti bit utilizza l'Extended ASCII per rappresentare ciascun carattere?
8
-
Qual è l'unità di base dell'informazione nel codice binario?
Bit
-
Converti il numero binario 10100 in un numero decimale. Qual è il risultato corretto?
20
-
A cosa serve il registro TEMP nella CPU?
Tiene i dati intermedi durante l'esecuzione delle istruzioni
-
Che cos'è la CPU in un computer?
L'unità di elaborazione centrale che esegue istruzioni dei programmi e gestisce le operazioni di calcolo.
-
Che cosa è il MDR?
Memory Data Register, contiene dati trasferiti da o verso la memoria
-
Cosa collega il system bus in un computer?
La CPU, la RAM e i dispositivi periferici
-
Cosa fa il MAR?
Tiene l'indirizzo di memoria da accedere
-
Cosa fa l'ALU?
Esegue operazioni aritmetiche e logiche
-
Cosa memorizza la RAM principalmente in un'architettura Von Neumann?
Sia dati che istruzioni
-
Qual è la funzione principale dei dispositivi di output?
Convertire i segnali digitali in forma leggibile/percettibile per gli umani
-
Quale dispositivo può funzionare sia come input che come output?
Monitor touchscreen
-
Quali sono i due tipi principali di operazioni che si possono effettuare sulla memoria?
Leggere e scrivere
-
Che cos'è un protocollo di un certo layer n?
Le regole per la comunicazione tra lo stesso layer su macchine diverse
-
Che cos'è un servizio non orientato alla connessione?
Un servizio che tratta ogni pacchetto di dati indipendentemente
-
Che cosa governano i protocolli di rete?
Le interazioni tra dispositivi connessi
-
In quali applicazioni si preferiscono generalmente i servizi non orientati alla connessione?
Streaming e giochi online
-
Che tipo di servizio è un servizio orientato alla connessione?
Un servizio che stabilisce una connessione dedicata prima della trasmissione dei dati
-
Come sono strutturate le reti per semplificare il design?
In più layers costruiti uno sull'altro
-
Cosa accade quando i pacchetti dati vengono persi in un servizio orientato alla connessione?
Vengono ritrasmessi
-
Cosa è un'internetwork?
Una collezione di diverse reti collegate tramite un gateway
-
Qual è il ruolo della "ACK" nei servizi orientati alla connessione?
Confermare la corretta ricezione di un pacchetto dati
-
Quali sono le caratteristiche chiave dei servizi orientati alla connessione?
Affidabilità, controllo del flusso e ordine dei dati
-
Che cosa è un driver?
Un software che traduce i comandi del sistema operativo in comandi comprensibili per l'hardware
-
Che cosa si intende per BIOS?
Un insieme di routine software memorizzate su un chip della scheda madre che inizializza l'hardware durante l'avvio del computer
-
Che cosa si intende per kernel?
Il componente centrale del sistema operativo che gestisce le operazioni fondamentali come la gestione della memoria, dei processi e dell'hardware
-
Che cosa si intende per sistema operativo?
Un software che gestisce le risorse hardware e software di un computer, esegue applicazioni e servizi, e interagisce con l'utente
-
Qual è il ruolo principale della scheda madre in un computer?
Collegare e permettere la comunicazione tra i componenti elettronici cruciali
-
Qual è la funzione principale del firmware in un dispositivo elettronico?
Inizializzare il componente e facilitare l'interazione con altri componenti
-
Qual è uno dei principali vantaggi di un Hybrid Kernel?
Combina le prestazioni di un kernel monolitico con la modularità di un micro-kernel
-
Quale delle seguenti è un vantaggio dell'UEFI rispetto al BIOS?
Offre meccanismi di sicurezza
-
Quale delle seguenti memorie non è volatile?
Rom
-
Quale tipo di sistema operativo permette l'esecuzione di programmi per più utenti simultaneamente?
Multi-user Operating Systems
-
Che cosa fa un dispositivo dopo aver ricevuto i dati in CSMA/CA?
Invia un segnale di conferma
-
Che cosa rappresentano le collisioni nel contesto delle reti?
Scontro tra pacchetti di dati trasmessi contemporaneamente
-
Cosa fa il preambolo in un frame dati?
Aiuta il dispositivo ricevente a prepararsi per comprendere i dati in arrivo
.
Qual è la differenza principale tra CSMA/CD e CSMA/CA?
CSMA/CD rileva le collisioni, mentre CSMA/CA evita le collisioni
-
Quali sono le funzioni del sottolivello Logical Link Control (LLC)?
Controllo del flusso di rete e rilevazione degli errori
-
Qual è la funzione principale del sottolivello Media Access Control (MAC)?
Gestire il controllo degli accessi al mezzo di trasmissione
-
Qual è lo scopo del checksum in un frame dati?
Rilevare errori nella trasmissione
-
Qual è lo scopo del modello ISO/OSI?
Fornire un modello standard contro cui possono essere confrontate varie architetture di rete
-
Quale livello del modello OSI è responsabile della connessione fisica tra i dispositivi?
Livello Physical
-
Quale livello del modello OSI gestisce il trasferimento dati nodo-a-nodo e la rilevazione e correzione degli errori?
Livello Data Link
---

Quale livello è responsabile della creazione, mantenimento e terminazione delle connessioni?
Transport Layer
--
Qual è lo scopo principale della Network Address Translation (NAT)?
Tradurre gli indirizzi IP privati in indirizzi IP pubblici
-
Quale dei seguenti è l'indirizzo logico utilizzato per identificare i dispositivi su una rete?
Indirizzo IP
-
Quale algoritmo di instradamento calcola il percorso verso una destinazione tramite metriche di costo cumulative?
Shortest Path First (SPF)
-
Qual è il ruolo principale del Application Layer?
Fornire servizi di rete alle applicazioni utente
-
Qual è la funzione principale del Network Layer nel modello OSI?
Instradamento e inoltro dei pacchetti di dati
-
Qual è lo scopo principale della Subnet Mask?
Determinare le porzioni di rete e host di un indirizzo IP
-
Cosa rappresenta un socket in una rete?
Un'interfaccia attraverso cui le applicazioni comunicano all'interno di una rete
-
Quale livello del modello OSI è responsabile della gestione del dialogo tra due computer?

Session Layer
-
Quale livello è responsabile della traduzione dei dati tra il livello di applicazione e la rete?
Presentation Layer
-
Quale dei seguenti è un esempio di interfaccia alfanumerica?
Interfaccia a riga di comando
-
Cosa fa il sistema operativo quando si verifica un "page fault"?
Sposta la pagina dal disco alla RAM
-
Quale delle seguenti affermazioni descrive correttamente una directory in un file system?
Una directory è un file che contiene puntatori ad altri file.
-
Quale comando di sistema viene utilizzato per creare un nuovo processo in un sistema operativo Unix-like?
Fork
-
Quale componente del sistema operativo traduce gli indirizzi di memoria virtuali in indirizzi fisici?
Memory Management Unit (MMU
-
Quale procedura verifica l'identità dell'utente?
Autenticazione
-
Qual è lo stato di un processo che ha terminato la sua esecuzione ma non è ancora stato rilasciato dal processo genitore?
Zombie
-
Qual è il ruolo principale della memoria buffer nella gestione dei dispositivi periferici?
Immagazzinare temporaneamente i dati per sincronizzare il trasferimento tra processi e dispositivi
-
Quale dei seguenti è un dispositivo di memoria secondaria?
Hardisk
-
Qual è il principale vantaggio dell'utilizzo della memoria virtuale in un sistema operativo?
Permette ai processi di avere più spazio di indirizzamento rispetto alla memoria fisica disponibile
-
Quale protocollo è utilizzato per il trasporto dei messaggi di posta elettronica?
SMTP
-
Quale protocollo del Transport Layer fornisce una comunicazione affidabile e orientata alla connessione?
TCP
-
Quale protocollo fornisce una connessione non affidabile e senza connessione, spesso utilizzato per lo streaming audio/video?
UDP
-
Quale protocollo di posta elettronica scarica i messaggi dal server e li elimina tipicamente dopo il download?
POP3
-
Quale protocollo viene utilizzato per risolvere i nomi di dominio in indirizzi IP?
DSN
-
Quale protocollo utilizza i messaggi di tipo "Echo Request" ed "Echo Reply" per testare la connettività di rete?
IMPC
-
Quale protocollo di posta elettronica consente agli utenti di visualizzare e manipolare i messaggi come se fossero memorizzati localmente, mantenendo la sincronizzazione su più dispositivi?
IMAP
-
Quale protocollo viene utilizzato per il trasferimento di pagine web?
http
-
Quale protocollo è utilizzato per la configurazione automatica degli indirizzi IP sui dispositivi di rete?
DHCP
-
Qual è il compito principale del protocollo ARP?

Mappare gli indirizzi IP agli indirizzi MAC

90

Qual è il compito principale del protocollo ARP?
Mappare gli indirizzi IP agli indirizzi MAC
-
Che tipo di servizio è un servizio orientato alla connessione?
Un servizio che stabilisce una connessione dedicata prima della trasmissione dei dati
-
Qual è una caratteristica della topologia a BUS?
utilizza un unico canale di comunicazione condiviso
-
Quale protocollo è utilizzato per il trasporto dei messaggi di posta elettronica?
SMTP
-
Che cos'è un protocollo di un certo layer n?
Le regole per la comunicazione tra lo stesso layer su macchine diverse
-
Quale delle seguenti affermazioni descrive meglio il modello client-server?
Un nodo centrale fornisce risorse e servizi agli altri nodi
-
Quali sono i due tipi principali di operazioni che si possono effettuare sulla memoria?
Leggere e scrivere
-
Qual è il ruolo principale del Application Layer?
Fornire servizi di rete alle applicazioni utente
-
Quale delle seguenti è un vantaggio dell'UEFI rispetto al BIOS?
Offre meccanismi di sicurezza
-
Qual è lo scopo del modello ISO/OSI?
Fornire un modello standard contro cui possono essere confrontate varie architetture di rete
-
Che cos'è un servizio non orientato alla connessione?
Un servizio che tratta ogni pacchetto di dati indipendentemente
-
Che cosa governano i protocolli di rete?
Le interazioni tra dispositivi connessi
-
Quali sono le caratteristiche chiave dei servizi orientati alla connessione?
Affidabilità, controllo del flusso e ordine dei dati
-
Che cosa si intende per kernel?
Il componente centrale del sistema operativo che gestisce le operazioni fondamentali come la gestione della memoria, dei processi e dell'hardware
-
Converti il numero binario 10100 in un numero decimale. Qual è il risultato corretto?
20
-
Quale protocollo utilizza i messaggi di tipo "Echo Request" ed "Echo Reply" per testare la connettività di rete?
ICMP
-
Quale affermazione descrive meglio una rete peer-to-peer (P2P)?
Ogni nodo può fungere da client o da server
-
Qual è lo scopo principale della Subnet Mask?
Determinare le porzioni di rete e host di un indirizzo IP
-
Cosa memorizza la RAM principalmente in un'architettura Von Neumann?
Sia dati che istruzioni
-
Come viene chiamato un gruppo di 8 bit?
Byte
-
Cosa fa il sistema operativo quando si verifica un "page fault"?
Sposta la pagina dal disco alla RAM
-
Quale comando di sistema viene utilizzato per creare un nuovo processo in un sistema operativo Unix-like?
fork
-
Quale livello del modello OSI è responsabile della connessione fisica tra i dispositivi?
Livello Physical
-
Che cosa si intende per sistema operativo?
Un software che gestisce le risorse hardware e software di un computer, esegue applicazioni e servizi, e interagisce con l'utente
-
Come vengono selezionati i percorsi in una rete point-to-point quando sono disponibili più percorsi?
Il percorso può essere selezionato sulla base della lunghezza o del traffico.
-
Qual è la funzione principale del sottolivello Media Access Control (MAC)?
Gestire il controllo degli accessi al mezzo di trasmissione
-
Che cosa si intende per BIOS?
Un insieme di routine software memorizzate su un chip della scheda madre che inizializza l'hardware durante l'avvio del computer
-
Quale livello è responsabile della creazione, mantenimento e terminazione delle connessioni?
Transport Layer
-
Qual è l'intervallo di valori rappresentabili con 5 bit?
da 0 a 31
-
Cosa fa il MAR?
Tiene l'indirizzo di memoria da accedere
-
Che cosa rappresentano le collisioni nel contesto delle reti?
Scontro tra pacchetti di dati trasmessi contemporaneamente
-
Che cosa è 'anycast' nella comunicazione di rete?
Comunicazione uno-a-molti più vicini
-
Quale dei seguenti è l'indirizzo logico utilizzato per identificare i dispositivi su una rete?
Indirizzo IP
-
Nel contesto delle reti di computer, cosa significa 'unicast'?
Il messaggio è inviato a un singolo dispositivo designato
-
Che cosa fa un dispositivo dopo aver ricevuto i dati in CSMA/CA?
Invia un segnale di conferma
-
Cosa rappresenta un socket in una rete?
Un'interfaccia attraverso cui le applicazioni comunicano all'interno di una rete
-
Quale livello del modello OSI è responsabile della gestione del dialogo tra due computer?
Session Layer
-
Qual è uno dei principali vantaggi di un Hybrid Kernel?
Combina le prestazioni di un kernel monolitico con la modularità di un micro-kernel
-
Cosa collega il system bus in un computer?
La CPU, la RAM e i dispositivi periferici
-
Qual è lo scopo del checksum in un frame dati?
Rilevare errori nella trasmissione
-
Qual è il ruolo principale della scheda madre in un computer?
Collegare e permettere la comunicazione tra i componenti elettronici cruciali
-
Considera l'espressione booleana: (A OR B) AND NOT (C AND D). 
Quale è il risultato di questa espressione quando A=0, B=1, C=1, D=0?
1
-
Quale protocollo di posta elettronica consente agli utenti di visualizzare e manipolare i messaggi come se fossero memorizzati localmente, mantenendo la sincronizzazione su più dispositivi?
IMAP
-
Come sono configurati i dispositivi nella topologia a MESH di una rete?
Ogni dispositivo è collegato direttamente a ogni altro dispositivo
-
Qual è la funzione principale del Network Layer nel modello OSI?
Instradamento e inoltro dei pacchetti di dati
-
Nella comunicazione di rete, cosa significa 'broadcast'?
Invio di messaggi a tutti i dispositivi nella rete
-
Qual è il risultato dell'addizione dei numeri binari 1100 e 111?
10011
-
Qual è l'unità di base dell'informazione nel codice binario
Bit
-
Quale protocollo è utilizzato per la configurazione automatica degli indirizzi IP sui dispositivi di rete?
DHCP
-
Quale protocollo di posta elettronica scarica i messaggi dal server e li elimina tipicamente dopo il download?
POP3
-
Qual è la funzione principale del firmware in un dispositivo elettronico?
Inizializzare il componente e facilitare l'interazione con altri componenti
-
Quale livello è responsabile della traduzione dei dati tra il livello di applicazione e la rete?
Presentation Layer
-
Quale tipo di sistema operativo permette l'esecuzione di programmi per più utenti simultaneamente?
Multi-user Operating Systems
-
Quale procedura verifica l'identità dell'utente?
Autenticazione
-
Converti il numero decimale 26 in un numero binario. Qual è il risultato corretto?
11010
-
Che cosa è il MDR?
Memory Data Register, contiene dati trasferiti da o verso la memoria
-
Qual è il principale vantaggio dell'utilizzo della memoria virtuale in un sistema operativo?
Permette ai processi di avere più spazio di indirizzamento rispetto alla memoria fisica disponibile
-
Quale algoritmo di instradamento calcola il percorso verso una destinazione tramite metriche di costo cumulative?
Shortest Path First (SPF)
-
Quale dispositivo può funzionare sia come input che come output?
Monitor touchscreen
-
Quale componente del sistema operativo traduce gli indirizzi di memoria virtuali in indirizzi fisici?
Memory Management Unit (MMU)
-
Quante combinazioni distinte si possono creare con 4 bit?
Sedici
-
Cosa accade quando i pacchetti dati vengono persi in un servizio orientato alla connessione?
vengono ritrasmessi
-
Qual è il ruolo principale della memoria buffer nella gestione dei dispositivi periferici?
Immagazzinare temporaneamente i dati per sincronizzare il trasferimento tra processi e dispositivi
-
In una rete point-to-point, come vengono trasferiti i dati?
I dati vengono inviati direttamente da un dispositivo a un altro attraverso un collegamento diretto.
-
Qual è il risultato della sottrazione dei numeri binari 10100 e 110 ?
01110
-
Quale protocollo fornisce una connessione non affidabile e senza connessione, spesso utilizzato per lo streaming audio/video?
UDP
-
In quali applicazioni si preferiscono generalmente i servizi non orientati alla connessione?
Streaming e giochi online
-
Quale protocollo del Transport Layer fornisce una comunicazione affidabile e orientata alla connessione?
TCP
-
Quale delle seguenti affermazioni descrive correttamente una directory in un file system?
Una directory è un file che contiene puntatori ad altri file.
-
Qual è lo stato di un processo che ha terminato la sua esecuzione ma non è ancora stato rilasciato dal processo genitore?
Zombie
-
A cosa serve il registro TEMP nella CPU?
Tiene i dati intermedi durante l'esecuzione delle istruzioni
-
Che cosa è un driver?
Un software che traduce i comandi del sistema operativo in comandi comprensibili per l'hardware
-
Cosa fa l'ALU?
Esegue operazioni aritmetiche e logiche
-
Quale dei seguenti è un dispositivo di memoria secondaria?
Hardisk
-
Quale protocollo viene utilizzato per risolvere i nomi di dominio in indirizzi IP?
DNS
-
Qual è il ruolo della "ACK" nei servizi orientati alla connessione?
Confermare la corretta ricezione di un pacchetto dati
-
Quale protocollo viene utilizzato per il trasferimento di pagine web?
HTTP
-
Qual è una funzione primaria delle reti di computer?
Condividere risorse e informazioni tra dispositivi
-
Quale delle seguenti memorie non è volatile?
ROM
-
Quale livello del modello OSI gestisce il trasferimento dati nodo-a-nodo e la rilevazione e correzione degli errori?
Livello Data Link
-
Cosa fa il preambolo in un frame dati?
Aiuta il dispositivo ricevente a prepararsi per comprendere i dati in arrivo
-
Che cos'è la CPU in un computer?
L'unità di elaborazione centrale che esegue istruzioni dei programmi e gestisce le operazioni di calcolo.
-
Qual è la funzione principale dei dispositivi di output?
Convertire i segnali digitali in forma leggibile/percettibile per gli umani
-
Quale dei seguenti è un esempio di interfaccia alfanumerica?
Interfaccia a riga di comando
-
Cosa è un'internetwork?
Una collezione di diverse reti collegate tramite un gateway
-
Quali sono le funzioni del sottolivello Logical Link Control (LLC)?
Controllo del flusso di rete e rilevazione degli errori
-
Qual è la differenza principale tra CSMA/CD e CSMA/CA?
CSMA/CD rileva le collisioni, mentre CSMA/CA evita le collisioni
-
Qual è lo scopo principale della Network Address Translation (NAT)?
Tradurre gli indirizzi IP privati in indirizzi IP pubblici
-
Come sono strutturate le reti per semplificare il design?
In più layers costruiti uno sull'altro
-
Quanti bit utilizza l'Extended ASCII per rappresentare ciascun carattere?
8 bit

90

Qual è il compito principale del protocollo ARP?
Mappare gli indirizzi IP agli indirizzi MAC
-
Che tipo di servizio è un servizio orientato alla connessione?
Un servizio che stabilisce una connessione dedicata prima della trasmissione dei dati
-
Qual è una caratteristica della topologia a BUS?
utilizza un unico canale di comunicazione condiviso
-
Quale protocollo è utilizzato per il trasporto dei messaggi di posta elettronica?
SMTP
-
Che cos'è un protocollo di un certo layer n?
Le regole per la comunicazione tra lo stesso layer su macchine diverse
-
Quale delle seguenti affermazioni descrive meglio il modello client-server?
Un nodo centrale fornisce risorse e servizi agli altri nodi
-
Quali sono i due tipi principali di operazioni che si possono effettuare sulla memoria?
Leggere e scrivere
-
Qual è il ruolo principale del Application Layer?
Fornire servizi di rete alle applicazioni utente
-
Quale delle seguenti è un vantaggio dell'UEFI rispetto al BIOS?
Offre meccanismi di sicurezza
-
Qual è lo scopo del modello ISO/OSI?
Fornire un modello standard contro cui possono essere confrontate varie architetture di rete
-
Che cos'è un servizio non orientato alla connessione?
Un servizio che tratta ogni pacchetto di dati indipendentemente
-
Che cosa governano i protocolli di rete?
Le interazioni tra dispositivi connessi
-
Quali sono le caratteristiche chiave dei servizi orientati alla connessione?
Affidabilità, controllo del flusso e ordine dei dati
-
Che cosa si intende per kernel?
Il componente centrale del sistema operativo che gestisce le operazioni fondamentali come la gestione della memoria, dei processi e dell'hardware
-
Converti il numero binario 10100 in un numero decimale. Qual è il risultato corretto?
20
-
Quale protocollo utilizza i messaggi di tipo "Echo Request" ed "Echo Reply" per testare la connettività di rete?
ICMP
-
Quale affermazione descrive meglio una rete peer-to-peer (P2P)?
Ogni nodo può fungere da client o da server
-
Qual è lo scopo principale della Subnet Mask?
Determinare le porzioni di rete e host di un indirizzo IP
-
Cosa memorizza la RAM principalmente in un'architettura Von Neumann?
Sia dati che istruzioni
-
Come viene chiamato un gruppo di 8 bit?
Byte
-
Cosa fa il sistema operativo quando si verifica un "page fault"?
Sposta la pagina dal disco alla RAM
-
Quale comando di sistema viene utilizzato per creare un nuovo processo in un sistema operativo Unix-like?
fork
-
Quale livello del modello OSI è responsabile della connessione fisica tra i dispositivi?
Livello Physical
-
Che cosa si intende per sistema operativo?
Un software che gestisce le risorse hardware e software di un computer, esegue applicazioni e servizi, e interagisce con l'utente
-
Come vengono selezionati i percorsi in una rete point-to-point quando sono disponibili più percorsi?
Il percorso può essere selezionato sulla base della lunghezza o del traffico.
-
Qual è la funzione principale del sottolivello Media Access Control (MAC)?
Gestire il controllo degli accessi al mezzo di trasmissione
-
Che cosa si intende per BIOS?
Un insieme di routine software memorizzate su un chip della scheda madre che inizializza l'hardware durante l'avvio del computer
-
Quale livello è responsabile della creazione, mantenimento e terminazione delle connessioni?
Transport Layer
-
Qual è l'intervallo di valori rappresentabili con 5 bit?
da 0 a 31
-
Cosa fa il MAR?
Tiene l'indirizzo di memoria da accedere
-
Che cosa rappresentano le collisioni nel contesto delle reti?
Scontro tra pacchetti di dati trasmessi contemporaneamente
-
Che cosa è 'anycast' nella comunicazione di rete?
Comunicazione uno-a-molti più vicini
-
Quale dei seguenti è l'indirizzo logico utilizzato per identificare i dispositivi su una rete?
Indirizzo IP
-
Nel contesto delle reti di computer, cosa significa 'unicast'?
Il messaggio è inviato a un singolo dispositivo designato
-
Che cosa fa un dispositivo dopo aver ricevuto i dati in CSMA/CA?
Invia un segnale di conferma
-
Cosa rappresenta un socket in una rete?
Un'interfaccia attraverso cui le applicazioni comunicano all'interno di una rete
-
Quale livello del modello OSI è responsabile della gestione del dialogo tra due computer?
Session Layer
-
Qual è uno dei principali vantaggi di un Hybrid Kernel?
Combina le prestazioni di un kernel monolitico con la modularità di un micro-kernel
-
Cosa collega il system bus in un computer?
La CPU, la RAM e i dispositivi periferici
-
Qual è lo scopo del checksum in un frame dati?
Rilevare errori nella trasmissione
-
Qual è il ruolo principale della scheda madre in un computer?
Collegare e permettere la comunicazione tra i componenti elettronici cruciali
-
Considera l'espressione booleana: (A OR B) AND NOT (C AND D). 
Quale è il risultato di questa espressione quando A=0, B=1, C=1, D=0?
1
-
Quale protocollo di posta elettronica consente agli utenti di visualizzare e manipolare i messaggi come se fossero memorizzati localmente, mantenendo la sincronizzazione su più dispositivi?
IMAP
-
Come sono configurati i dispositivi nella topologia a MESH di una rete?
Ogni dispositivo è collegato direttamente a ogni altro dispositivo
-
Qual è la funzione principale del Network Layer nel modello OSI?
Instradamento e inoltro dei pacchetti di dati
-
Nella comunicazione di rete, cosa significa 'broadcast'?
Invio di messaggi a tutti i dispositivi nella rete
-
Qual è il risultato dell'addizione dei numeri binari 1100 e 111?
10011
-
Qual è l'unità di base dell'informazione nel codice binario
Bit
-
Quale protocollo è utilizzato per la configurazione automatica degli indirizzi IP sui dispositivi di rete?
DHCP
-
Quale protocollo di posta elettronica scarica i messaggi dal server e li elimina tipicamente dopo il download?
POP3
-
Qual è la funzione principale del firmware in un dispositivo elettronico?
Inizializzare il componente e facilitare l'interazione con altri componenti
-
Quale livello è responsabile della traduzione dei dati tra il livello di applicazione e la rete?
Presentation Layer
-
Quale tipo di sistema operativo permette l'esecuzione di programmi per più utenti simultaneamente?
Multi-user Operating Systems
-
Quale procedura verifica l'identità dell'utente?
Autenticazione
-
Converti il numero decimale 26 in un numero binario. Qual è il risultato corretto?
11010
-
Che cosa è il MDR?
Memory Data Register, contiene dati trasferiti da o verso la memoria
-
Qual è il principale vantaggio dell'utilizzo della memoria virtuale in un sistema operativo?
Permette ai processi di avere più spazio di indirizzamento rispetto alla memoria fisica disponibile
-
Quale algoritmo di instradamento calcola il percorso verso una destinazione tramite metriche di costo cumulative?
Shortest Path First (SPF)
-
Quale dispositivo può funzionare sia come input che come output?
Monitor touchscreen
-
Quale componente del sistema operativo traduce gli indirizzi di memoria virtuali in indirizzi fisici?
Memory Management Unit (MMU)
-
Quante combinazioni distinte si possono creare con 4 bit?
Sedici
-
Cosa accade quando i pacchetti dati vengono persi in un servizio orientato alla connessione?
vengono ritrasmessi
-
Qual è il ruolo principale della memoria buffer nella gestione dei dispositivi periferici?
Immagazzinare temporaneamente i dati per sincronizzare il trasferimento tra processi e dispositivi
-
In una rete point-to-point, come vengono trasferiti i dati?
I dati vengono inviati direttamente da un dispositivo a un altro attraverso un collegamento diretto.
-
Qual è il risultato della sottrazione dei numeri binari 10100 e 110 ?
01110
-
Quale protocollo fornisce una connessione non affidabile e senza connessione, spesso utilizzato per lo streaming audio/video?
UDP
-
In quali applicazioni si preferiscono generalmente i servizi non orientati alla connessione?
Streaming e giochi online
-
Quale protocollo del Transport Layer fornisce una comunicazione affidabile e orientata alla connessione?
TCP
-
Quale delle seguenti affermazioni descrive correttamente una directory in un file system?
Una directory è un file che contiene puntatori ad altri file.
-
Qual è lo stato di un processo che ha terminato la sua esecuzione ma non è ancora stato rilasciato dal processo genitore?
Zombie
-
A cosa serve il registro TEMP nella CPU?
Tiene i dati intermedi durante l'esecuzione delle istruzioni
-
Che cosa è un driver?
Un software che traduce i comandi del sistema operativo in comandi comprensibili per l'hardware
-
Cosa fa l'ALU?
Esegue operazioni aritmetiche e logiche
-
Quale dei seguenti è un dispositivo di memoria secondaria?
Hardisk
-
Quale protocollo viene utilizzato per risolvere i nomi di dominio in indirizzi IP?
DNS
-
Qual è il ruolo della "ACK" nei servizi orientati alla connessione?
Confermare la corretta ricezione di un pacchetto dati
-
Quale protocollo viene utilizzato per il trasferimento di pagine web?
HTTP
-
Qual è una funzione primaria delle reti di computer?
Condividere risorse e informazioni tra dispositivi
-
Quale delle seguenti memorie non è volatile?
ROM
-
Quale livello del modello OSI gestisce il trasferimento dati nodo-a-nodo e la rilevazione e correzione degli errori?
Livello Data Link
-
Cosa fa il preambolo in un frame dati?
Aiuta il dispositivo ricevente a prepararsi per comprendere i dati in arrivo
-
Che cos'è la CPU in un computer?
L'unità di elaborazione centrale che esegue istruzioni dei programmi e gestisce le operazioni di calcolo.
-
Qual è la funzione principale dei dispositivi di output?
Convertire i segnali digitali in forma leggibile/percettibile per gli umani
-
Quale dei seguenti è un esempio di interfaccia alfanumerica?
Interfaccia a riga di comando
-
Cosa è un'internetwork?
Una collezione di diverse reti collegate tramite un gateway
-
Quali sono le funzioni del sottolivello Logical Link Control (LLC)?
Controllo del flusso di rete e rilevazione degli errori
-
Qual è la differenza principale tra CSMA/CD e CSMA/CA?
CSMA/CD rileva le collisioni, mentre CSMA/CA evita le collisioni
-
Qual è lo scopo principale della Network Address Translation (NAT)?
Tradurre gli indirizzi IP privati in indirizzi IP pubblici
-
Come sono strutturate le reti per semplificare il design?
In più layers costruiti uno sull'altro
-
Quanti bit utilizza l'Extended ASCII per rappresentare ciascun carattere?
8 bit
-
Qual è il compito principale del protocollo ARP?
Mappare gli indirizzi IP agli indirizzi MAC
-
Che tipo di servizio è un servizio orientato alla connessione?
Un servizio che stabilisce una connessione dedicata prima della trasmissione dei dati
-
Qual è una caratteristica della topologia a BUS?
utilizza un unico canale di comunicazione condiviso
-
Quale protocollo è utilizzato per il trasporto dei messaggi di posta elettronica?
SMTP
-
Che cos'è un protocollo di un certo layer n?
Le regole per la comunicazione tra lo stesso layer su macchine diverse
-
Quale delle seguenti affermazioni descrive meglio il modello client-server?
Un nodo centrale fornisce risorse e servizi agli altri nodi
-
Quali sono i due tipi principali di operazioni che si possono effettuare sulla memoria?
Leggere e scrivere
-
Qual è il ruolo principale del Application Layer?
Fornire servizi di rete alle applicazioni utente
-
Quale delle seguenti è un vantaggio dell'UEFI rispetto al BIOS?
Offre meccanismi di sicurezza
-
Qual è lo scopo del modello ISO/OSI?
Fornire un modello standard contro cui possono essere confrontate varie architetture di rete
-
Che cos'è un servizio non orientato alla connessione?
Un servizio che tratta ogni pacchetto di dati indipendentemente
-
Che cosa governano i protocolli di rete?
Le interazioni tra dispositivi connessi
-
Quali sono le caratteristiche chiave dei servizi orientati alla connessione?
Affidabilità, controllo del flusso e ordine dei dati
-
Che cosa si intende per kernel?
Il componente centrale del sistema operativo che gestisce le operazioni fondamentali come la gestione della memoria, dei processi e dell'hardware
-
Converti il numero binario 10100 in un numero decimale. Qual è il risultato corretto?
20
-
Quale protocollo utilizza i messaggi di tipo "Echo Request" ed "Echo Reply" per testare la connettività di rete?
ICMP
-
Quale affermazione descrive meglio una rete peer-to-peer (P2P)?
Ogni nodo può fungere da client o da server
-
-
Qual è lo scopo principale della Subnet Mask?
Determinare le porzioni di rete e host di un indirizzo IP
-
Cosa memorizza la RAM principalmente in un'architettura Von Neumann?
Sia dati che istruzioni
-
Come viene chiamato un gruppo di 8 bit?
Byte
-
Cosa fa il sistema operativo quando si verifica un "page fault"?
Sposta la pagina dal disco alla RAM
-
Quale comando di sistema viene utilizzato per creare un nuovo processo in un sistema operativo Unix-like?
fork
-
Quale livello del modello OSI è responsabile della connessione fisica tra i dispositivi?
Livello Physical
-
Che cosa si intende per sistema operativo?
Un software che gestisce le risorse hardware e software di un computer, esegue applicazioni e servizi, e interagisce con l'utente
-
Come vengono selezionati i percorsi in una rete point-to-point quando sono disponibili più percorsi?
Il percorso può essere selezionato sulla base della lunghezza o del traffico.
-
Qual è la funzione principale del sottolivello Media Access Control (MAC)?
Gestire il controllo degli accessi al mezzo di trasmissione
-
Che cosa si intende per BIOS?
Un insieme di routine software memorizzate su un chip della scheda madre che inizializza l'hardware durante l'avvio del computer
-
Quale livello è responsabile della creazione, mantenimento e terminazione delle connessioni?
Transport Layer
-
Qual è l'intervallo di valori rappresentabili con 5 bit?
da 0 a 31
-
Cosa fa il MAR?
Tiene l'indirizzo di memoria da accedere
-
Che cosa rappresentano le collisioni nel contesto delle reti?
Scontro tra pacchetti di dati trasmessi contemporaneamente
-
Che cosa è 'anycast' nella comunicazione di rete?
Comunicazione uno-a-molti più vicini
-
Quale dei seguenti è l'indirizzo logico utilizzato per identificare i dispositivi su una rete?
Indirizzo IP
-
Nel contesto delle reti di computer, cosa significa 'unicast'?
Il messaggio è inviato a un singolo dispositivo designato
-
Che cosa fa un dispositivo dopo aver ricevuto i dati in CSMA/CA?
Invia un segnale di conferma
-
Cosa rappresenta un socket in una rete?
Un'interfaccia attraverso cui le applicazioni comunicano all'interno di una rete
-
Quale livello del modello OSI è responsabile della gestione del dialogo tra due computer?
Session Layer
-
Qual è uno dei principali vantaggi di un Hybrid Kernel?
Combina le prestazioni di un kernel monolitico con la modularità di un micro-kernel
-
Cosa collega il system bus in un computer?
La CPU, la RAM e i dispositivi periferici
-
Qual è lo scopo del checksum in un frame dati?
Rilevare errori nella trasmissione
-
Qual è il ruolo principale della scheda madre in un computer?
Collegare e permettere la comunicazione tra i componenti elettronici cruciali
-
Considera l'espressione booleana: (A OR B) AND NOT (C AND D). 
Quale è il risultato di questa espressione quando A=0, B=1, C=1, D=0?
1
-
Quale protocollo di posta elettronica consente agli utenti di visualizzare e manipolare i messaggi come se fossero memorizzati localmente, mantenendo la sincronizzazione su più dispositivi?
IMAP
-
Come sono configurati i dispositivi nella topologia a MESH di una rete?
Ogni dispositivo è collegato direttamente a ogni altro dispositivo
-
Qual è la funzione principale del Network Layer nel modello OSI?
Instradamento e inoltro dei pacchetti di dati
-
Nella comunicazione di rete, cosa significa 'broadcast'?
Invio di messaggi a tutti i dispositivi nella rete
-
Qual è il risultato dell'addizione dei numeri binari 1100 e 111?
10011
-
Qual è l'unità di base dell'informazione nel codice binario
Bit
-
Quale protocollo è utilizzato per la configurazione automatica degli indirizzi IP sui dispositivi di rete?
DHCP
-
Quale protocollo di posta elettronica scarica i messaggi dal server e li elimina tipicamente dopo il download?
POP3
-
Qual è la funzione principale del firmware in un dispositivo elettronico?
Inizializzare il componente e facilitare l'interazione con altri componenti
-
Quale livello è responsabile della traduzione dei dati tra il livello di applicazione e la rete?
Presentation Layer
-
Quale tipo di sistema operativo permette l'esecuzione di programmi per più utenti simultaneamente?
Multi-user Operating Systems
-
Quale procedura verifica l'identità dell'utente?
Autenticazione
-
Converti il numero decimale 26 in un numero binario. Qual è il risultato corretto?
11010
-
Che cosa è il MDR?
Memory Data Register, contiene dati trasferiti da o verso la memoria
-
Qual è il principale vantaggio dell'utilizzo della memoria virtuale in un sistema operativo?
Permette ai processi di avere più spazio di indirizzamento rispetto alla memoria fisica disponibile
-
Quale algoritmo di instradamento calcola il percorso verso una destinazione tramite metriche di costo cumulative?
Shortest Path First (SPF)
-
Quale dispositivo può funzionare sia come input che come output?
Monitor touchscreen
-
Quale componente del sistema operativo traduce gli indirizzi di memoria virtuali in indirizzi fisici?
Memory Management Unit (MMU)
-
Quante combinazioni distinte si possono creare con 4 bit?
Sedici
-
Cosa accade quando i pacchetti dati vengono persi in un servizio orientato alla connessione?
vengono ritrasmessi
-
Qual è il ruolo principale della memoria buffer nella gestione dei dispositivi periferici?
Immagazzinare temporaneamente i dati per sincronizzare il trasferimento tra processi e dispositivi
-
In una rete point-to-point, come vengono trasferiti i dati?
I dati vengono inviati direttamente da un dispositivo a un altro attraverso un collegamento diretto.
-
Qual è il risultato della sottrazione dei numeri binari 10100 e 110 ?
01110
-
Quale protocollo fornisce una connessione non affidabile e senza connessione, spesso utilizzato per lo streaming audio/video?
UDP
-
In quali applicazioni si preferiscono generalmente i servizi non orientati alla connessione?
Streaming e giochi online
-
Quale protocollo del Transport Layer fornisce una comunicazione affidabile e orientata alla connessione?
TCP
-
Quale delle seguenti affermazioni descrive correttamente una directory in un file system?
Una directory è un file che contiene puntatori ad altri file.
-
Qual è lo stato di un processo che ha terminato la sua esecuzione ma non è ancora stato rilasciato dal processo genitore?
Zombie
-
A cosa serve il registro TEMP nella CPU?
Tiene i dati intermedi durante l'esecuzione delle istruzioni
-
Che cosa è un driver?
Un software che traduce i comandi del sistema operativo in comandi comprensibili per l'hardware
-
Cosa fa l'ALU?
Esegue operazioni aritmetiche e logiche
-
Quale dei seguenti è un dispositivo di memoria secondaria?
Hardisk
-
Quale protocollo viene utilizzato per risolvere i nomi di dominio in indirizzi IP?
DNS
-
Qual è il ruolo della "ACK" nei servizi orientati alla connessione?
Confermare la corretta ricezione di un pacchetto dati
-
Quale protocollo viene utilizzato per il trasferimento di pagine web?
HTTP
-
Qual è una funzione primaria delle reti di computer?
Condividere risorse e informazioni tra dispositivi
-
Quale delle seguenti memorie non è volatile?
ROM
-
Quale livello del modello OSI gestisce il trasferimento dati nodo-a-nodo e la rilevazione e correzione degli errori?
Livello Data Link
-
Cosa fa il preambolo in un frame dati?
Aiuta il dispositivo ricevente a prepararsi per comprendere i dati in arrivo
-
Che cos'è la CPU in un computer?
L'unità di elaborazione centrale che esegue istruzioni dei programmi e gestisce le operazioni di calcolo.
-
Qual è la funzione principale dei dispositivi di output?
Convertire i segnali digitali in forma leggibile/percettibile per gli umani
-
Quale dei seguenti è un esempio di interfaccia alfanumerica?
Interfaccia a riga di comando
-
Cosa è un'internetwork?
Una collezione di diverse reti collegate tramite un gateway
-
Quali sono le funzioni del sottolivello Logical Link Control (LLC)?
Controllo del flusso di rete e rilevazione degli errori
-
Qual è la differenza principale tra CSMA/CD e CSMA/CA?
CSMA/CD rileva le collisioni, mentre CSMA/CA evita le collisioni
-
Qual è lo scopo principale della Network Address Translation (NAT)?
Tradurre gli indirizzi IP privati in indirizzi IP pubblici
-
Come sono strutturate le reti per semplificare il design?
In più layers costruiti uno sull'altro
-
Quanti bit utilizza l'Extended ASCII per rappresentare ciascun carattere?
8 bit
-
'''