#  EDOARDO DI LISIO
#  04.06.24
'''
Si richiede di sviluppare dei casi di test per funzioni date prendendo gli input da file.

     Prendere le soluzioni ottenute del test Moodle della lezione 9 (esercizi vari)
    Creare dei nuovi casi di test utilizzando unittest
    Gli input per ogni caso di test deve essere preso da un file dedicato con un formato bene definito scelto a piacere.
    Scrivere l'output della funzione un file di output dedicato.

Ed esempio: 

Creare 5 nuovi casi di test di test per la funzione anagram(s, t) dove s e t sono anagrammi da comparare. Gli input di ogni caso di test, quindi s e t, devono estrapolati da un file di input dedicato.

Ogni caso di test deve avere un file di input separato che rispetti il formato scelto.
'''

import unittest

def anagram(s: str, t: str) -> bool:
    # Converte entrambe le stringhe in minuscolo e poi le ordina
    # Confronta le versioni ordinate delle due stringhe
    # Ritorna True se sono uguali, False altrimenti
    return sorted(s.lower()) == sorted(t.lower())

class TestAnagram(unittest.TestCase):

    def read_input(self, filename):
        with open(filename, 'r') as file:
            s = file.readline().strip()
            t = file.readline().strip()
        
        print(s, t)
        return s, t

    def write_output(self, filename, result):
        with open(filename, 'w') as file:
            file.write(str(result))

    def test_anagram_case1(self):
        s, t = self.read_input('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_input1.txt')
        result = anagram(s, t)
        self.write_output('test_output1.txt', result)
        self.assertTrue(result)

    def test_anagram_case2(self):
        s, t = self.read_input('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_input2.txt')
        result = anagram(s, t)
        self.write_output('test_output2.txt', result)
        self.assertFalse(result)

    def test_anagram_case3(self):
        s, t = self.read_input('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_input3.txt')
        result = anagram(s, t)
        self.write_output('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_output3.txt', result)
        self.assertTrue(result)

    def test_anagram_case4(self):
        s, t = self.read_input('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_input4.txt')
        result = anagram(s, t)
        self.write_output('test_output4.txt', result)
        self.assertFalse(result)

    def test_anagram_case5(self):
        s, t = self.read_input('test_input5.txt')
        result = anagram(s, t)
        self.write_output('test_output5.txt', result)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
