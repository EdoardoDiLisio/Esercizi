'''
1. Write a class called Student with the attributes name (str) and studyProgram (str);
2. create three instance. one for yourself, left and right neighbour;
3. Add a method printInfo that prints the name and studyProgram of a Student. Test your method on the object!
4. modify the code and add age and gender to the attributes. Modify your printing methods respectively too
'''

class Student:
    def __init__(self, name, study_program, age = None, gender = None):
        self.name = name
        self.study_program = study_program
        self.age = age
        self.gender = gender

    def print_info(self):
        print("Name:", self.name)
        print("Study Program:", self.study_program)
        if self.age is not None:
            print("Age:", self.age)
        if self.gender is not None:
            print("Gender:", self.gender)
        print()

yourself = Student("Edoardo_Di_Lisio", "Cyber_Security", 20, "Male")
left_neighbour = Student("Mario_Rossi", "Cyber_Security", 20, "Male")
right_neighbour = Student("Anna_Bianchi", "Cyber_Security", 22, "Female")

yourself.print_info()
left_neighbour.print_info()
right_neighbour.print_info()
