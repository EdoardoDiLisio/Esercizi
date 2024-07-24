#  EDOARDO DI LISIO
#  12.06.24

'''
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del 
pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe 
Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() 
che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, 
l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa 
classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca inoltre il metodo
inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete 
da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. Questa classe 
deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. Infine, si 
ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti 
e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:

1.
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

2.
Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

3.
Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

4.
Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321
'''

class Pagamento:
    def __init__(self):
        self.__importo = 0.0  # Inizializza l'attributo privato '__importo' a 0.0

    def set_importo(self, importo):
        self.__importo = importo  # Imposta l'importo del pagamento

    def get_importo(self):
        return self.__importo  # Restituisce l'importo del pagamento

    def dettagli_pagamento(self):
        return f"Importo del pagamento: €{self.get_importo():.2f}"  # Restituisce una stringa con l'importo del pagamento


class PagamentoContanti(Pagamento):  # La classe PagamentoContanti eredita dalla classe Pagamento
    def __init__(self):
        super().__init__()  # Chiama il costruttore della classe padre

    def dettagli_pagamento(self):  # Override del metodo dettagli_pagamento della classe Pagamento
        importo = self.get_importo()  # Ottiene l'importo del pagamento
        banconote = [500, 200, 100, 50, 20, 10, 5]  # Lista delle banconote disponibili
        monete = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]  # Lista delle monete disponibili
        banconote_usate = []  # Lista per tenere traccia delle banconote utilizzate
        monete_usate = []  # Lista per tenere traccia delle monete utilizzate

        # Calcola le banconote utilizzate per il pagamento
        for banconota in banconote:
            count = 0
            while importo >= banconota:
                importo -= banconota
                count += 1
            if count > 0:
                banconote_usate.append((banconota, count))

        # Converti l'importo rimanente in centesimi per gestire le monete
        importo = round(importo, 2)  # Arrotonda a 2 decimali
        importo_cents = int(importo * 100)  # Converti in centesimi

        # Calcola le monete utilizzate per il pagamento
        for moneta in monete:
            count = 0
            while importo_cents >= int(moneta * 100):
                importo_cents -= int(moneta * 100)
                count += 1
            if count > 0:
                monete_usate.append((moneta, count))

        # Costruisci una stringa con i dettagli del pagamento in contanti
        dettagli = f"Pagamento in contanti di: €{self.get_importo():.2f}\n"
        dettagli += f"{self.get_importo():.2f} euro da pagare in contanti con:\n"
        for banconota, count in banconote_usate:
            if count == 1:
                dettagli += f"{count} banconota da {banconota} euro\n"
            else:
                dettagli += f"{count} banconote da {banconota} euro\n"
        for moneta, count in monete_usate:
            if count == 1:
                dettagli += f"{count} moneta da {moneta} euro\n"
            else:
                dettagli += f"{count} monete da {moneta} euro\n"
        return dettagli  # Restituisce la stringa con i dettagli del pagamento


class PagamentoCartaDiCredito(Pagamento):  # La classe PagamentoCartaDiCredito eredita dalla classe Pagamento
    def __init__(self, nome_titolare, data_scadenza, numero_carta):
        super().__init__()  # Chiama il costruttore della classe padre
        print("***           ***")  # Stampa una riga vuota
        # Inizializza gli attributi specifici della carta di credito: nome_titolare, data_scadenza, numero_carta
        self.nome_titolare = nome_titolare
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta

    def dettagli_pagamento(self):  # Override del metodo dettagli_pagamento della classe Pagamento
        # Costruisci una stringa con i dettagli del pagamento con carta di credito
        return f"Pagamento di: €{self.get_importo():.2f} effettuato con la carta di credito\n" \
               f"Nome sulla carta: {self.nome_titolare}\n" \
               f"Data di scadenza: {self.data_scadenza}\n" \
               f"Numero della carta: {self.numero_carta}"


# Test delle classi
pagamento1 = PagamentoContanti()  # Crea un'istanza di PagamentoContanti
pagamento1.set_importo(150.0)  # Imposta l'importo del pagamento
print(pagamento1.dettagli_pagamento())  # Stampa i dettagli del pagamento

pagamento2 = PagamentoContanti()  # Crea un'altra istanza di PagamentoContanti
pagamento2.set_importo(95.25)  # Imposta l'importo del pagamento
print(pagamento2.dettagli_pagamento())  # Stampa i dettagli del pagamento

pagamento3 = PagamentoCartaDiCredito("Mario Rossi", "12/24", "12345678987654321")  # Crea un'istanza di PagamentoCartaDiCredito
pagamento3.set_importo(200.0)  # Imposta l'importo del pagamento
print(pagamento3.dettagli_pagamento())  # Stampa i dettagli del pagamento

pagamento4 = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", "98765432123456789")  # Crea un'altra istanza di PagamentoCartaDiCredito
pagamento4.set_importo(500.0)  # Imposta l'importo del pagamento
print(pagamento4.dettagli_pagamento())  # Stampa i dettagli del pagamento
