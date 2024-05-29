#Francesca Scippa

#07-05-2024

#9-1. Restaurant: Make a class called Restaurant. 
#The __init__() method for Restaurant should store two attributes: 
#a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
#and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Resturant:
    
    def __init__(self, resturant_name: str, cusine_type: str, number_served: int):
        
        self.resturant_name: str = resturant_name
        self.cusine_type: str = cusine_type
        self.number_served: int = number_served
        
    def __str__(self) -> str:
        return f"The resturant's name is {self.resturant_name}, and the cusine type is {self.cusine_type} They served {self.number_served} customers" 
    
    def descrive_resturant(self): 
        return self.__str__()
         
    def open_resturant(self):
        print(f"\nThe resturant {self.resturant_name} is Open!")
        
    def set_number_served(self, new_number_served: int):
        self.number_served: int = new_number_served
    
    def increment_number_served(self, increment_served: int):
        if self.number_served:
            self.number_served += increment_served
        else:
            self.new_number_served += increment_served
        
tana_della_volpe: Resturant = Resturant("tana_della_volpe","Italian", 150)

#print(tana_della_volpe)
tana_della_volpe.descrive_resturant()
tana_della_volpe.open_resturant()

#9-2. Three Restaurants: Start with your class from Exercise 9-1. 
#Create three different instances from the class, and call describe_restaurant() for each instance.

print("_"*30)

koy_sushi: Resturant = Resturant("Koy Sushi", "Japanese", 89)

#print(koy_sushi)
koy_sushi.descrive_resturant()
koy_sushi.open_resturant()

print("_"*30)

da_miranda: Resturant = Resturant("Da Miranda","Italian/Fish", 120)

#print(da_miranda)
da_miranda.descrive_resturant()
da_miranda.open_resturant()

print("_"*30)

himalaya_palace: Resturant = Resturant("Himalaya Palace", "Indian", 75)

himalaya_palace.descrive_resturant()
himalaya_palace.open_resturant()

print("#"*30)

#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
#and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.

class User:
    
    def __init__(self, first_name: str, last_name: str, age: int, height: float):
        
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.height: int = height
        self.login_attempts: int = 0
    
    def __str__(self) -> str:
        return f"User(name: {self.first_name}\nlast name: {self.last_name}\nage:{self.age}\nheight: {self.height}\nlogin attempts: {self.login_attempts}"
    
    def describe_user(self):
        return self.__str__()
        
    def greet_user(self):
        print(f"\nHello {self.first_name}! How are you?")
        
    def increment_login_attemps(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

francesca: User = User("Francesca", "Scippa", 25, 1.58)
francesca.describe_user()
francesca.greet_user()

print("_"*30)

nicolò: User = User("Nicolò", "Di Silvestro", 25, 1.75)
nicolò.describe_user()
nicolò.greet_user()

print("_"*30)

simone: User = User("Simone", "Marchica", 24, 1.85)
simone.describe_user()
simone.greet_user()

print("#"*30)

#9-4. Number Served: Start with your program from Exercise 9-1. 
#Add an attribute called number_served with a default value of 0. 
#Create an instance called restaurant from this class. 
#Print the number of customers the restaurant has served, and then change this value and print it again. 
#Add a method called set_number_served() that lets you set the number of customers that have been served. 
#Call this method with a new number and print the value again. 
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

tana_della_volpe: Resturant = Resturant("tana_della_volpe","Italian", 150)

tana_della_volpe.set_number_served(100)
tana_della_volpe.descrive_resturant()

tana_della_volpe.increment_number_served(20)
tana_della_volpe.descrive_resturant()

#print("#"*30)

#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
#Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
#Make an instance of the User class and call increment_login_attempts() several times. 
#Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
#Print login_attempts again to make sure it was reset to 0.

for i in range(10):
    francesca.increment_login_attemps()

francesca.describe_user()

#print("_"*30)

francesca.reset_login_attempts()
francesca.describe_user()

#print("#"*30)

#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
#Either version of the class will work; just pick the one you like better. 
#Add an attribute called flavors that stores a list of ice cream flavors.
#Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

class IceCreamStand: 
    
    def __init__(self, resturant: Resturant, flavors: list[str]):
        
        self.flavors: list[str] = flavors
        self.resturant: Resturant = resturant
        
    def __str__(self) -> str:
        s: str = ""
        for flavor in self.flavors:
            s += flavor + ", "
        return f"\nThe flavors are: {s}"
    
gelato: IceCreamStand = IceCreamStand(tana_della_volpe,['Fragola','Cioccolato','Vaniglia'])

print(gelato)
print("#"*30)
#9-7. Admin: An administrator is a special kind of user. 
#Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
#Add an attribute, privileges, that stores a list of strings like "can add post", 
#"can delete post", "can ban user", and so on. Write a method called show_privileges() 
#that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

#9-8. Privileges: Write a separate Privileges class. 
#The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
#Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
#Create a new instance of Admin and use your method to show its privileges.

class Privileges:
    
    def __init__(self, privileges: list[str]):
        
        self.privileges: list[str] = privileges
        
    def __str__(self):
        s: str = ""
        for privilege in self.privileges:
            s += privilege + ", "
        return f"The Admin privileges are: {s} "
    
    def show_privileges(self):
        return self.__str__()

class Admin:
    
    def __init__(self, user: User, privileges: Privileges):
        
        self.privileges: Privileges = privileges
        self.user: User = user

    def show_privileges(self):
        return str(self.privileges)
    
privileges: Privileges = Privileges(["can add post", "can delete post", "can ban user"])
admin1: Admin = Admin(francesca, privileges)

#print(admin1.show_privileges())

#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. 
#Add a method to the Battery class called upgrade_battery(). 
#This method should check the battery size and set the capacity to 65 if it isn’t already. 
#Make an electric car with a default battery size, call get_range() once, 
#and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

class Battery:
    
    def __init__(self, charge_percentage: float, size: str = None):
        
        self.charge_percentage: float = charge_percentage
        self.size: str = None
        
    def upgrade_battery(self):
        
        if self.size == 'Medium':
            self.charge_percentage = 65
        
        if self.charge_percentage < 100:
            self.charge_percentage += 1
        
        if self.charge_percentage == 100:
            pass
    
    def __str__(self) -> str:
        return f"The cahrge percentage is {self.charge_percentage}"
    
battery: Battery = Battery(12.5, 'Medium')

for x in range(20):
    battery.upgrade_battery()

#print(battery)

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 
#Make a separate file that imports Restaurant. 
#Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

from imported import Resturant

sora_lella: Resturant = Resturant("SoraLella", "Roman", 178)

print(sora_lella.descrive_resturant())
print('#'*30)

#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, 
#Privileges, and Admin in one module. Create a separate file, make an Admin instance, 
#and call show_privileges() to show that everything is working correctly.

from imported import Privileges, Admin

privileges1: Privileges = Privileges(['add user', 'ban user'])
sophia: User = User("Sophia", "Phippen", 26, 175)
admin2: Admin = Admin(sophia, privileges)

print(admin2.show_privileges())    
print("_"*30)

#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
#In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from importUser import User

print(admin2.show_privileges())
print('_'*30)

#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
#Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
#Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times

import random

class Die:
    
    def __init__(self, sides: int = 6):
        
        self.sides: int = sides
    
    def roll_die(self):
        return random.randint(1, self.sides)
    
die6: Die = Die()

for roll in range(10):
    print(die6.roll_die())
print('_'*30)   

die10: Die = Die(10)

for roll in range(10):
    print(die10.roll_die())
print('_'*30)     

die20: Die = Die(20)

for roll in range(10):
    print(die10.roll_die())        
print('_'*30)          

#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
#Randomly select 4 numbers or letters from the list and print a message saying 
#that any ticket matching these 4 numbers or letters wins a prize.

class Lottery:

    def __init__(self, ticket: tuple[int,str]):

        self.ticket: tuple[int,str] = ticket

    def random_ticket(self) -> str:
        ticket0: list[int] =random.sample(self.ticket,4)
        return "Any ticket matching these 4 numbers or letters wins a prize."
        
letters: tuple[str] = ('A','B','C','D','F')
ticket: tuple[int,str] = ()

for n in range(11):
    number: tuple[int] = (n, )
    ticket += number

ticket += letters

ticket1: Lottery = Lottery(ticket)

print(ticket1.random_ticket())



       
        







        



