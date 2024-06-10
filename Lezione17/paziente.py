from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, id_code):
        # Inizializza gli attributi ereditati dalla classe Persona
        super().__init__(first_name, last_name)
        # Verifica se il codice identificativo è una stringa, altrimenti imposta a None e stampa un messaggio di errore
        if isinstance(id_code, str):
            self.__id_code = id_code
        else:
            self.__id_code = None
            print("Il codice identificativo inserito non è una stringa!")

    def setIdCode(self, id_code):
        # Imposta il codice identificativo se l'input è una stringa, altrimenti stampa un messaggio di errore
        if isinstance(id_code, str):
            self.__id_code = id_code
        else:
            print("Il codice identificativo inserito non è una stringa!")

    def getIdCode(self):
        # Ritorna il codice identificativo
        return self.__id_code

    def patientInfo(self):
        # Stampa le informazioni del paziente, inclusi nome, cognome e codice identificativo
        print(f"Paziente: {self.getName()} {self.getLastname()}")
        print(f"ID: {self.__id_code}")
