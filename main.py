class Person:
    def __init__(self):
        self.species = "Homo Sapiens"

    def display_species(self):
        print(f"Вид: {self.species}")

class Learner:
    def __init__(self):
        self.learner = True

    def is_learner(self):
        return self.learner

class Student(Person, Learner):
    def __init__(self):
        Person.__init__(self)
        Learner.__init__(self)
        self.name = "N/A"
        self.age = 19
        self.height = 205
        self.school = 98

    def display(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Рост: {self.height}")
        print(f"Школа: {self.school}")
        self.display_species()
        print(f"Учащийся: {self.is_learner()}")

student = Student()

student.display()
