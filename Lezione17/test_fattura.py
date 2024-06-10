#  EDOARDO DI LISIO
#  10.06.24

import unittest
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

class TestFattura(unittest.TestCase):

    def test_fattura_initialization_valid_doctor(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        d.setAge(45)
        p1 = Paziente("Giulia", "Verdi", "P001")
        p2 = Paziente("Marco", "Neri", "P002")
        lista_pazienti = [p1, p2]
        f = Fattura(lista_pazienti, d)
        self.assertEqual(f.getFatture(), 2)
        self.assertEqual(f.getSalary(), 100.0)

    def test_fattura_initialization_invalid_doctor(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        d.setAge(25)
        p1 = Paziente("Giulia", "Verdi", "P001")
        lista_pazienti = [p1]
        f = Fattura(lista_pazienti, d)
        self.assertIsNone(f.fatture)
        self.assertIsNone(f.salary)

    def test_add_patient(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        d.setAge(45)
        p1 = Paziente("Giulia", "Verdi", "P001")
        lista_pazienti = [p1]
        f = Fattura(lista_pazienti, d)
        p2 = Paziente("Marco", "Neri", "P002")
        f.addPatient(p2)
        self.assertEqual(f.getFatture(), 2)
        self.assertEqual(f.getSalary(), 100.0)

    def test_remove_patient(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        d.setAge(45)
        p1 = Paziente("Giulia", "Verdi", "P001")
        p2 = Paziente("Marco", "Neri", "P002")
        lista_pazienti = [p1, p2]
        f = Fattura(lista_pazienti, d)
        f.removePatient("P001")
        self.assertEqual(f.getFatture(), 1)
        self.assertEqual(f.getSalary(), 50.0)

if __name__ == '__main__':
    unittest.main()
