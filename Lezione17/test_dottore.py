import unittest
from dottore import Dottore

class TestDottore(unittest.TestCase):

    def test_dottore_initialization(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        self.assertEqual(d.getName(), "Mario")
        self.assertEqual(d.getLastname(), "Rossi")
        self.assertEqual(d.getAge(), 0)
        self.assertEqual(d.getSpecialization(), "Pediatra")
        self.assertEqual(d.getParcel(), 50.0)

    def test_dottore_invalid_initialization(self):
        d = Dottore("Mario", "Rossi", 123, "Cinquanta")
        self.assertIsNone(d.getSpecialization())
        self.assertIsNone(d.getParcel())

    def test_set_specialization(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        d.setSpecialization("Cardiologo")
        self.assertEqual(d.getSpecialization(), "Cardiologo")
        d.setSpecialization(123)
        self.assertEqual(d.getSpecialization(), "Cardiologo")  # Specialization should not change

    def test_set_parcel(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        d.setParcel(100.0)
        self.assertEqual(d.getParcel(), 100.0)
        d.setParcel("Cento")
        self.assertEqual(d.getParcel(), 100.0)  # Parcel should not change

    def test_is_valid_doctor(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        d.setAge(45)
        self.assertTrue(d.isAValidDoctor())
        d.setAge(25)
        self.assertFalse(d.isAValidDoctor())

    def test_doctor_greet(self):
        d = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        d.setAge(45)
        self.assertEqual(d.doctorGreet(), "Ciao, sono Mario Rossi! Ho 45 anni! Sono un medico Pediatra")

if __name__ == '__main__':
    unittest.main()
