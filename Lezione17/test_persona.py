#  EDOARDO DI LISIO
#  10.06.24

import unittest
from persona import Persona

class TestPersona(unittest.TestCase):

    def test_persona_initialization(self):
        p = Persona("Mario", "Rossi")
        self.assertEqual(p.getName(), "Mario")
        self.assertEqual(p.getLastname(), "Rossi")
        self.assertEqual(p.getAge(), 0)

    def test_persona_invalid_initialization(self):
        p = Persona(123, [])
        self.assertIsNone(p.getName())
        self.assertIsNone(p.getLastname())
        self.assertIsNone(p.getAge())

    def test_set_name(self):
        p = Persona("Mario", "Rossi")
        p.setName("Luigi")
        self.assertEqual(p.getName(), "Luigi")
        p.setName(123)
        self.assertEqual(p.getName(), "Luigi")  # Name should not change

    def test_set_lastname(self):
        p = Persona("Mario", "Rossi")
        p.setLastName("Bianchi")
        self.assertEqual(p.getLastname(), "Bianchi")
        p.setLastName(123)
        self.assertEqual(p.getLastname(), "Bianchi")  # Lastname should not change

    def test_set_age(self):
        p = Persona("Mario", "Rossi")
        p.setAge(30)
        self.assertEqual(p.getAge(), 30)
        p.setAge("Trenta")
        self.assertEqual(p.getAge(), 30)  # Age should not change

    def test_greet(self):
        p = Persona("Mario", "Rossi")
        p.setAge(30)
        self.assertEqual(p.greet(), "Ciao, sono Mario Rossi! Ho 30 anni!")

if __name__ == '__main__':
    unittest.main()
