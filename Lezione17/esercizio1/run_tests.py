#  EDOARDO DI LISIO
#  10.06.24

import unittest
from test_persona import TestPersona
from test_dottore import TestDottore
from test_paziente import TestPaziente
from test_fattura import TestFattura

if __name__ == "__main__":
    # Definisci la suite di test
    suite = unittest.TestSuite()

    # Aggiungi i test per le classi Persona, Dottore, Paziente e Fattura
    suite.addTest(unittest.makeSuite(TestPersona))
    suite.addTest(unittest.makeSuite(TestDottore))
    suite.addTest(unittest.makeSuite(TestPaziente))
    suite.addTest(unittest.makeSuite(TestFattura))

    # Esegui la suite di test
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
