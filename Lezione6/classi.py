class Person:
    def __init__(self, name:str, surname:str, ssn:str) -> None:
        
        self._name: str = name
        self._surname: str = surname
        self._ssn: str = ssn
        
        self._funzione_1()
    
    def get_ssn(self) -> str:
        """
        this function returns the ssn value
        input: none
        return: self._snn : str, the function returns the ssn value
        """
        return self._ssn
    def _funzione_1(self):
        
        self._name.lower()
        
    def get_name(self) -> str:
        """
        this function returns a person's name
        input: none
        return: self._name : str, the function returs the person's name
        """
        return  self._name
    
    def set_name(self, name: str) -> None:
        """
        this function set the attribute name
        input: name : str, the parameter contains the user's name
        input: name : str
        return: none
        """
        
        raise Exception('you cannot modify the name!')

    def __str__(self) -> str:
        
        return f"name: {self._name} surname: {self._surname} ssn: {self._ssn}"


person_1: Person = Person(name='Edoardo', surname='Di_Lisio', ssn='dlsdrd00e30h501a')
person_2: Person = Person(name='Ilaria', surname='Sergi', ssn='ddfght')

queue: list = [person_1, person_2]

for person in queue:
    print(person.get_ssn())

print(person_1.get_ssn())
print(person_1.get_name())
print(str(person_1))