#EDOARDO DI LISIO
#26.06.2024

'''
Esercizio 1

Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')
'''
'''   
Esercizio 2

Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1
'''

from pathlib import Path
from time import *

print("\nFile Manager:\n")

class FileManager:

    def __init__(self, filename: str, mode: str) -> None:
        self.filename: str = str(Path(__file__).parent.resolve())+"\\"+filename
        self.mode: str = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            print("Caught an exception")
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Traceback: {traceback}")
        else:
            self.file.close()

def filemanager(func) -> None:
    def wrapper(*args):
        print("Opening file")
        func(*args)
        print("File closed\n")
    return wrapper

@filemanager
def fileopen(filename: str, mode: str) -> None:
    with FileManager(filename, mode) as f:
        f.write("HAWK TUAH!")
        f.close()

fileopen("example.txt","w")

print("Time manager:\n")

class Timer:

    def __init__(self) -> None:
        self.count: int = 0
    
    def __enter__(self) -> None:
        self.count = time()
    
    def __exit__(self, exc_type, exc_val, traceback) -> float:
        if exc_type is not None:
            print("Caught an exception")
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Traceback: {traceback}")
        else:
            print(f"time elapsed: {time() - self.count:.5f}") 

def timer(func):
    def wrapper(sec):
        print("Initiating function")
        func(sec)
        print("End of function\n")
    return wrapper

@timer
def checkTime(sec: int):
    with Timer():
        sleep(sec)

checkTime(2)