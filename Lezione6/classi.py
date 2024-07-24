class Person:
    def __init__(self, name:str, surname:str, ssn:str, birth_date:str, birth_place:str, gender:str) -> None:
        
        self._name: str = name
        self._surname: str = surname
        self._ssn: str = ssn
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender: str = gender
        self._ssn: str = None
        
        self.compute_ssn()
                    
    def get_ssn(self) -> str:
        """
        this function returns the ssn value
        input: none
        return: self._snn : str, the function returns the ssn value
        """
        return self._ssn
    
    def set_ssn(self, ssn: str) -> None:
        '''
        this function set the ssn
        input: ssn : str, the parameter conteins the user's snn
        return: None
        '''
        
        raise Exception('you cannot modify the ssn!')

                
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
        
        self._name = name
        self._ssn = self.compute_ssn()

    def compute_ssn(self)->bool:
        """
        check the ssn's correctness
        """
        
        first_three__name_char = self._name[:3]
        last_three__surname_char = self._surname[-3:]
        self._ssn = first_three__name_char .upper() + last_three__surname_char.upper()
        
person_1: Person = Person(name ='Edoardo',
                          surname ='Di_Lisio',
                          ssn ='dlsdrd00e30h501a' ,
                          birth_date = '30/05/2000',
                          birth_place = 'Roma',
                          gender = 'Male')

#person_2: Person = Person(name='Ilaria', surname='Sergi', ssn='ddfght')
        
print(person_1.get_ssn())


print(str(person_1))
#print(str(person_2))
queue: list = [person_1] #person_2]

for person in queue:
    print(person.get_ssn())

print(person_1.get_name())
print(str(person_1))