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
        
    #def __str__(self) -> str:
        #return f"The resturant's name is {self.resturant_name}, and the cusine type is {self.cusine_type} They served {self.number_served} customers"" 
    
    def descrive_resturant(self): 
        print(f"The resturant's name is {self.resturant_name}, and the cusine type is {self.cusine_type}. They served {self.number_served} customers")
         
    def open_resturant(self):
        print(f"The resturant {self.resturant_name} is Open!")
        
    def set_number_served(self, new_number_served: int):
        self.number_served: int = new_number_served
    
    def increment_number_served(self, increment_served: int):
        if self.number_served:
            self.number_served += increment_served
        else:
            self.new_number_served += increment_served
        
print("#"*100)
    
tana_della_volpe: Resturant = Resturant("tana_della_volpe","Italian", 150)

#print(tana_della_volpe)
tana_della_volpe.descrive_resturant()
tana_della_volpe.open_resturant()

#9-2. Three Restaurants: Start with your class from Exercise 9-1. 
#Create three different instances from the class, and call describe_restaurant() for each instance.

print("_"*100)

koy_sushi: Resturant = Resturant("Koy Sushi", "Japanese", 89)

#print(koy_sushi)
koy_sushi.descrive_resturant()
koy_sushi.open_resturant()

print("_"*100)

da_miranda: Resturant = Resturant("Da Miranda","Italian/Fish", 120)

#print(da_miranda)
da_miranda.descrive_resturant()
da_miranda.open_resturant()

print("_"*100)

himalaya_palace: Resturant = Resturant("Himalaya Palace", "Indian", 75)

himalaya_palace.descrive_resturant()
himalaya_palace.open_resturant()

print("#"*100)

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
    
    #def __str__(self) -> str:
        #return f"User(name: {self.first_name}\nlast name: {self.last_name}\nage:{self.age}\nheight: {self.height}"
    
    def describe_user(self):
        print(f"User\nname: {self.first_name}\nlast name: {self.last_name}\nage: {self.age}\nheight: {self.height}\nlogin attempts: {self.login_attempts}")
        
    def greet_user(self):
        print(f"Hello {self.first_name}! How are you?")
        
    def increment_login_attemps(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

francesca: User = User("Francesca", "Scippa", 25, 1.58)
francesca.describe_user()
francesca.greet_user()

print("_"*100)

nicolò: User = User("Nicolò", "Di Silvestro", 25, 1.75)
nicolò.describe_user()
nicolò.greet_user()

print("_"*100)

simone: User = User("Simone", "Marchica", 24, 1.85)
simone.describe_user()
simone.greet_user()

print("#"*100)

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

print("#"*100)

#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
#Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
#Make an instance of the User class and call increment_login_attempts() several times. 
#Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
#Print login_attempts again to make sure it was reset to 0.

for i in range(10):
    francesca.increment_login_attemps()

francesca.describe_user()

print("_"*100)

francesca.reset_login_attempts()
francesca.describe_user()

print("#"*100)

#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
#Either version of the class will work; just pick the one you like better. 
#Add an attribute called flavors that stores a list of ice cream flavors.
#Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

<<<<<<< HEAD
=======
class IceCreamStand: 
    
    def __init__(self, resturant: Resturant):
        
        self.resturant: Resturant = resturant
    
    def flavors(self, flavors: list[str] ) -> str:
        return f"The favors are: {self.flavors}"
    
gelato: IceCreamStand = IceCreamStand(tana_della_volpe)

print(gelato.flavors( ['Fragola','Cioccolato','Vaniglia']))
    
    




       
        







        



>>>>>>> 9e16394 (.)
