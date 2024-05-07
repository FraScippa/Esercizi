#Francesca Scippa

#07-05-2024

class Person:

    def __init__(self, name: str, age: int, height: float):

        self.name: str = name
        self.age: int = age
        self.height: float = height
        #self.hobby: set[str] = set{}
    
    def bulk_set_hobby(self, hobbies: list[str]):
        self.hobby = self.hobby.union(set(hobbies)) #union ritorna un nuovo set
        #self.hobby += hobbies
        """for hobby in hobbies:
            #self.hobby.append(hobby)
            self.set_hobby(hobby)"""

    def set_hobby(self, new_hobby: str):
        self.hobby.add(set([new_hobby]))
        #self.hobby.append(new_hobby)

    def remove_hobby(self, old_hobby: str):
        if old_hobby in self.hobby:
            self.hobby.revome(old_hobby)

    def __str__(self) -> str: #deve essere indentata nella Classe
        return f"persona(name: {self.name}, age: {self.age}, height: {self.height})"

lista : list = []

alice: Person = Person("Alice W.", 45, 170)
lista.append(alice)

bob: Person = Person("Bob M.", 36, 169)
lista.append(bob)

"""if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.age)"""

paolo: Person = Person("Paolo C.", 20, 186)
lista.append(paolo)

nicolò: Person = Person("Nicolò D.S", 25, 175)
lista.append(nicolò)

marco: Person = Person("Marco D.C", 50, 190)
lista.append(marco)

### Prende la persona più giovane ###

index_min_age: int = 0
youngest: int = float('inf')

for i in range(len(lista)):
    if lista[i].age < youngest:
        youngest = lista[i].age
        index_min_age = i

persona = lista[index_min_age]

#print(f"il nome della persona più giovane è {persona}") 
"""con età {persona.age}"\
+ f altezza = {persona.height})"""

class Student:

    def __init__(self, name: str, studyProgram: str):

        self.name: str = name
        self.studyProgram: str =  studyProgram
        self.age = 0
        self.gender = None

    def set_age(self, new_age: int):
        self.age = new_age

    def set_gender(self, new_gender: str):
        self.gender = new_gender

    def __str__(self) -> str:
        return f"Il nome dello studente è {self.name} e partecipa al corso di {self.studyProgram},"\
            +f" ha {self.age} anni, ed è {self.gender}"

francesca: Student = Student("Francesca", "Cloud")
francesca.set_gender("F")
francesca.set_age(25)

print(francesca)

marco: Student = Student("Marco", "Cloud")
marco.set_gender("M")
marco.set_age(23)
print(marco)

walter: Student = Student("Walter", "Cloud")
walter.set_gender("M")
walter.set_age(33)
print(walter)


class Students:
    
    my_grades: list = []
    student_grades: list = []

    def __init__(self, name: str):
        self.name: str = name
        #self.grade: float = grade
        #self.student_grades.append(grade)

    def print_grade(self):
        print(f"Il mio voto è {self.grade}")
    
    def add_grades(self, grade: float):
        self.my_grades.append(grade)
    
    def grades_averange(self):
        return sum(self.my_grades)/ len(self.my_grades)

    @classmethod
    def get_avg_grades(cls):

        avg= sum(cls.student_grades) / len(cls.student_grades)
        return avg

francesca = Students(name = "Francesca")

francesca.add_grades(9)
francesca.add_grades(7)
francesca.add_grades(10)

print(Students.my_grades)
#print(Students.student_grades)
#francesca.print_grades()


class Animal:

    def __init__ (self, name: str, legs: int):
        
        self.name: str = name
        self.legs: int = legs
    
    def setLegs(self, new_legs: int):
        self.legs: int = new_legs

    def get_legs(self) -> int:
        return self.legs

    def __str__(self):
        return f"The animal's name is {self.name}, he has {self.legs} legs."
        
dog: Animal = Animal("Noè", 4)
dog.setLegs(3)
print(dog)

class Food:

    def __inti__(self, name: str, price: float, description: str):

        self.name: str = name
        self.price: float = price
        self.description: str = description

class Menu:

    foods: list = []

    def __init__(self, food: list[str]):
        self.foods.append(food)
    
    def add_food(self, new_food: str):
        self.foods.append(new_food)
    
    def remove_food(self, food_remove: str):
        self.foods.remove(food_remove)

    def __str__(self):
        return f"Food:{self.name}/nPrice:{self.price}/nDescription:{self.description}"

pizza: Food = Food("Margherita", 7.50, "Pizza's with mozzarella and tomatos")
print(pizza)


