#  EDOARDO DI LISIO
#  10.06.24

import unittest
from paziente import Paziente

class TestPaziente(unittest.TestCase):

    def test_paziente_initialization(self):
        p = Paziente("Mario", "Rossi", "P001")
        self.assertEqual(p.getName(), "Mario")
        self.assertEqual(p.getLastname(), "Rossi")
        self.assertEqual(p.getAge(), 0)
        self.assertEqual(p.getIdCode(), "P001")

    def test_set_id_code(self):
        p = Paziente("Mario", "Rossi", "P001")
        p.setIdCode("P002")
        self.assertEqual(p.getIdCode(), "P002")
        p.setIdCode(123)
        self.assertEqual(p.getIdCode(), "P002")  # ID Code should not change

    def test_patient_info(self):
        p = Paziente("Mario", "Rossi", "P001")
        self.assertEqual(p.patientInfo(), "Paziente: Mario Rossi\nID: P001")

if __name__ == '__main__':
    unittest.main()
