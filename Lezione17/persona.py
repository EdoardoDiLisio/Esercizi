class Persona:
    def __init__(self, first_name, last_name):
        # Verifica se il nome è una stringa, altrimenti imposta a None e stampa un messaggio di errore
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è una stringa!")

        # Verifica se il cognome è una stringa, altrimenti imposta a None e stampa un messaggio di errore
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print("Il cognome inserito non è una stringa!")

        # Se sia il nome che il cognome sono stringhe, imposta l'età a 0, altrimenti a None
        if isinstance(first_name, str) and isinstance(last_name, str):
            self.__age = 0
        else:
            self.__age = None

    def setName(self, first_name):
        # Imposta il nome se l'input è una stringa, altrimenti stampa un messaggio di errore
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")

    def setLastName(self, last_name):
        # Imposta il cognome se l'input è una stringa, altrimenti stampa un messaggio di errore
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self, age):
        # Imposta l'età se l'input è un intero, altrimenti stampa un messaggio di errore
        if isinstance(age, int):
            self.__age = age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self):
        # Ritorna il nome
        return self.__first_name

    def getLastname(self):
        # Ritorna il cognome
        return self.__last_name

    def getAge(self):
        # Ritorna l'età
        return self.__age

    def greet(self):
        # Stampa un messaggio di saluto con nome, cognome ed età
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")
