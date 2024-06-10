#  EDOARDO DI LISIO
#  10.06.24

import unittest

# Scopre ed esegue tutti i test nella directory corrente
def run_all_tests():
    # Crea un loader di test
    loader = unittest.TestLoader()
    # Cerca e carica tutti i test nella directory corrente
    suite = loader.discover(start_dir='.', pattern='test_*.py')

    # Crea un runner che eseguirà i test
    runner = unittest.TextTestRunner()
    # Esegue i test e restituisce i risultati
    runner.run(suite)

if __name__ == '__main__':
    run_all_tests()
