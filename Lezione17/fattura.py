class Fattura:
    def __init__(self, patients, doctor):
        # Inizializza la lista dei pazienti e il dottore
        self.__patients = patients
        self.__doctor = doctor

        # Verifica se il dottore è valido, se sì imposta il numero di fatture e il salario, altrimenti imposta tutto a None
        if doctor.isAValidDoctor():
            self.__fatture = len(patients)
            self.__salary = 0
        else:
            self.__fatture = None
            self.__salary = None
            self.__patients = None
            self.__doctor = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        # Calcola e ritorna il salario del dottore moltiplicando la parcella per il numero di pazienti
        if self.__doctor and self.__patients:
            self.__salary = self.__doctor.getParcel() * len(self.__patients)
            return self.__salary
        return 0

    def getFatture(self):
        # Ritorna il numero di fatture, che è il numero di pazienti
        if self.__doctor and self.__patients:
            self.__fatture = len(self.__patients)
            return self.__fatture
        return 0

    def addPatient(self, new_patient):
        # Aggiunge un nuovo paziente alla lista, aggiorna il numero di fatture e il salario, e stampa un messaggio
        if self.__patients is not None:
            self.__patients.append(new_patient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.__doctor.getLastname()} è stato aggiunto il paziente {new_patient.getIdCode()}")

    def removePatient(self, id_code):
        # Rimuove un paziente dalla lista basandosi sul codice identificativo, aggiorna il numero di fatture e il salario, e stampa un messaggio
        if self.__patients is not None:
            patient_to_remove = None
            for patient in self.__patients:
                if patient.getIdCode() == id_code:
                    patient_to_remove = patient
                    break
            if patient_to_remove:
                self.__patients.remove(patient_to_remove)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor {self.__doctor.getLastname()} è stato rimosso il paziente {id_code}")
