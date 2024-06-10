from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization, parcel):
        # Inizializza gli attributi ereditati dalla classe Persona
        super().__init__(first_name, last_name)
        # Verifica se la specializzazione è una stringa, altrimenti imposta a None e stampa un messaggio di errore
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")

        # Verifica se la parcella è un float, altrimenti imposta a None e stampa un messaggio di errore
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specialization):
        # Imposta la specializzazione se l'input è una stringa, altrimenti stampa un messaggio di errore
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel):
        # Imposta la parcella se l'input è un float, altrimenti stampa un messaggio di errore
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self):
        # Ritorna la specializzazione
        return self.__specialization

    def getParcel(self):
        # Ritorna la parcella
        return self.__parcel

    def isAValidDoctor(self):
        # Verifica se il dottore ha più di 30 anni, se sì stampa un messaggio di validità, altrimenti di invalidità
        if self.getAge() > 30:
            print(f"Doctor {self.getName()} {self.getLastname()} is valid!")
        else:
            print(f"Doctor {self.getName()} {self.getLastname()} is not valid!")

    def doctorGreet(self):
        # Chiama il metodo greet() della classe Persona e aggiunge un messaggio specifico per il dottore
        self.greet()
        print(f"Sono un medico {self.__specialization}")
