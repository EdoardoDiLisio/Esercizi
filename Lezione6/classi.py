class Person:
    def __init__(self, name:str, surname:str, ssn:str) -> None:
        
        self._name: str = name
        self._surname: str = surname
        self._ssn: str = ssn
    
    def get_name(self):
        
        return  self._name
    
    def set_name(self, name: str) -> None:
        """
        this function set the attribute name
        input: name : str, the parameter contains the user's name
        input: name : str
        return: none
        """
        
        raise Exception('you cannot modify the name!')




Person_1: Person = Person(name='Edoardo', surname='Di_Lisio', ssn='DLSDRD00E30H501A')

print(Person_1.get_name())
Person_1.set_name(name='giusy')

print(Person_1.get_name())