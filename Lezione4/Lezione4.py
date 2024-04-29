# Francesca Scippa
# 2024/04/29

#8-1. Message: Write a function called display_message() 
#that prints one sentence telling everyone what you are learning about in this chapter. 
#Call the function, and make sure the message displays correctly.

def display_message() -> None:
    """Prints one sentence telling everyone what you are learning about in this chapter"""
    
    message: str = 'In this chapter, I learning how to write a function.'
    
    print(message)
    
display_message()

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
#The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
#Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title: str) -> None:
    """Accepts one parameter, title."""
    
    message: str = 'One of my favorite books is ' + title.title()
    
    print(message)
    
favorite_book('alice in wonderland')    

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that 
#should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and 
#the message printed on it. Call the function once using positional arguments to make a shirt. 
#Call the function a second time using keyword arguments.

def make_shirt(size: str, text: str) -> str:
    """Accepts a size and the text of a message that 
    should be printed on the shirt. 
    """
    
    #check if the size is right.
    if (size.upper() != 'XS' and
        size.upper() != 'S' and
        size.upper() != 'M' and  
        size.upper() != 'L' and 
        size.upper() != 'XL' and  
        size.upper() != 'XXL') : 
        new_size: str = input('Please, insert a valid size like: XS/S/M/L/XL/XXL: ')
        t_shirt: str = f'The size of this t-shirt is: {new_size.upper()}\nand the text will be: {text}'
    else:
        t_shirt: str = f'The size of this t-shirt is: {size.upper()}\nand the text will be: {text}' 
    
    return t_shirt
    
print(make_shirt("n","See you later, aligator!"))

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size: str, text: str) -> str:
    """Accepts a size and the text of a message that 
    should be printed on the shirt. 
    """
    
    if (size.upper() != 'XS' and 
        size.upper() != 'S' and 
        size.upper() != 'M' and  
        size.upper() != 'L' and 
        size.upper() != 'XL' and  
        size.upper() != 'XXL' ): 
        new_size: str = input('Please, insert a valid size like: XS/S/M/L/XL/XXL: ')
        
        #if shirts are large or medium, the text will be change
        if (new_size.upper() == "L" or
            new_size.upper() == "M"):
            t_shirt: str = f'The size of this t-shirt is: {new_size.upper()}\nand the text will be: I love Python.'
        
        else:
            t_shirt: str = f'The size of this t-shirt is: {new_size.upper()}\nand the text will be: {text}'
            
    return t_shirt

print(make_shirt("n","See you later, aligator!"))

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. 
#Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the default country.

def describe_city (key: str, value: str ) -> str:
    """Accepts the name of a city and its country."""
    
    cities: dict = {'Rome': 'Italy', 'Moscow':"Russia",'Baku': "Azerbaigian",'New York': "America"}
    
    if (key.title() in cities and 
        value.title() == cities[key.title()]):
       final_message: str = key.title() + ' is in ' + value.title()
    
    #remember the .values() when you want to access to the value!!
    elif (key.title() not in cities 
        and value.title() not in cities.values()):
        print("Please, insert a valid key and a valid valute, thank you.")
        new_key1: str = input("Please, insert a city: ").title().strip()
        new_valute1: str = input("Please, insert the right country: ").title().strip()
        final_message: str = new_key1.title() + ' is in ' + new_valute1.title()
    
    elif key.title() not in cities:
        new_key: str = input("Please, insert the right city: ").title().strip()
        final_message: str = new_key.title().strip() + ' is in ' + value.title()
        
    elif value.title() not in cities.values():
        new_valute: str = input("Please, insert the right country: ").title().strip()
        final_message: str = key.title() + ' is in ' + new_valute.title().strip()
    
    return final_message        
        
print(describe_city ('New York', 'America'))

#8-7. Album: Write a function called  that builds a dictionary describing a music album. 
#The function should take in an artist name and an album title, 
#and it should return a dictionary containing these two pieces of information. 
#Use the function to make three dictionaries representing different albums. 
#Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
#If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
#Make at least one new function call that includes the number of songs on an album.

def make_album(artist: str, album: str, songs: int = None) -> dict:
    """Take an artist name and an album title, 
    and it return a dictionary containing these two pieces of information.
    """
    
    album: dict = {'artist': artist, 'title': album}
    
    if songs not in album:
        album["songs"] = songs
    
    return album
        
metal: dict = make_album("Iron Maiden", "Fear Of The Dark")
rock: dict = make_album("Dire Straits", "Money For Nothing")
rap: dict = make_album("Fabri Fibra", "Controcultura", 18)

print(metal)
print(rock)
print(rap)

# 8-8. User Albums: Start with your program from Exercise 8-7. 
#Write a while loop that allows users to enter an album’s artist and title. 
#Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
#Be sure to include a quit value in the while loop.

while True:
    
    artist: str = input("Insert an Artist: ").strip().title()
    title: str = input("Insert a Title: ").strip().title()
    songs: int = int(input("Insert number of songs: ")).strip()
    break
    
song: dict = make_album(artist, title, songs)
print(song)

#8-9. Messages: Make a list containing a series of short text messages. 
#Pass the list to a function called show_messages(), 
#which prints each text message.

def show_messages(lista: list) -> None:
    """Prints each text message containing in a list."""
    
    for i in lista:
        str2: str = i
        print(f"The messages are: {i}")
    
messages: list = ["I love you","Proud of you","I'm spain without S"] 

show_messages(messages)

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
#Write a function called send_messages() 
#that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
#After calling the function, print both of your lists to make sure the messages were moved correctly.
    
def send_messages(lista: list ) -> None:
    """Prints each text message and moves each message to a new list."""
    
    sent_message: list = []
    
    for i in lista:
        str1: str = i
        print(i)
        sent_message.append(i)
    
    print(sent_message)

send_messages(messages)

#8-11. Archived Messages: Start with your work from Exercise 8-10. 
#Call the function send_messages() with a copy of the list of messages. 
#After calling the function, print both of your lists to show that the original list has retained its messages.

def send_messages(lista: list ) -> None:
    """Prints each text message and moves each message to a new list."""
    
    copia: list = []
    
    for i in lista:
        copia.append(i)
    
    print(copia,lista)

send_messages(messages)

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, 
#and it should print a summary of the sandwich that’s being ordered. 
#Call the function three times, using a different number of arguments each time.

def sandwiches_ingredients(ing1: str, ing2: str, ing3: str, ingr4: str ) -> None:
    """Accept a list of items a person wants on a sandwich."""
    
    sandwiche: list = [ing1, ing2, ing3, ingr4]
    
    print(f"The ingredients are: {sandwiche}")
    
sandwiches_ingredients("tomato", "cheddar", "ham", "sauces")
sandwiches_ingredients("salad", "tomato", "vegan burger", "hummus")
sandwiches_ingredients("egg", "salad", "cheddar", "tomato" )

#8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
#using your first and last names and three other key-value pairs that describe you. 
#All the values must be passed to the function as parameters. 
#The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

def build_profile(name: str, age: int, hair: str) -> str:
    """Accept 3 items and return a string"""
    
    profile: dict = {'name': name, 'age': age, 'hair': hair}
    profile_complite: list = []
    
    for i in profile.values():
        profile_complite.append(i)
    end: str = f"{profile_complite[0]}, age {profile_complite[1]}, hair {profile_complite[2]}"
   
    return end

print(build_profile('Francesca Scippa', 25, 'blonde'))
 
#8-14. Cars: Write a function that stores information about a car in a dictionary. 
#The function should always receive a manufacturer and a model name. 
#It should then accept an arbitrary number of keyword arguments. 
#Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call 
#like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that’s returned to make sure all the information was stored correctly.   

def make_cars(brand: str, model:str, color: str, heating: bool) -> dict:
    """Store information about a car in a dictionary."""
    
    cars: dict = {'brand': brand, 'model': model, 'color': color, 'heating': heating}
   
    return cars
    
print(make_cars('Ford', 'Puma', 'White', True))

#8-15. Printing Models: Put the functions for the example printing_models.py 
#in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, 
#and modify the file to use the imported functions.

from printing_functions import construct_rectangle

print(construct_rectangle(4))

#8-16. Imports: Using a program you wrote that has one function in it, 
#store that function in a separate file. 
#Import the function into your main program file, and call the function using each of these approaches:

import printing_functions
from printing_functions import fibonacci #Calculate the value of fibonacci with the index
from printing_functions import is_subsequence as s #Check if a string is in another string and retun a Boolean
import printing_functions as pf
from printing_functions import moltiplication 

print(fibonacci(7))
print(s("abc", "ahbgdc"))
print(moltiplication(3,9))

#8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
#and make sure they follow the styling guidelines described in this section.

def make_shirt(size: str, text: str) -> str:
    """Accepts a size and the text of a message that 
    should be printed on the shirt. 
    """
    
    if (size.upper() != 'XS' and 
        size.upper() != 'S' and 
        size.upper() != 'M' and  
        size.upper() != 'L' and 
        size.upper() != 'XL' and  
        size.upper() != 'XXL' ): 
        new_size: str = input('Please, insert a valid size like: XS/S/M/L/XL/XXL: ')
        
        #if shirts are large or medium, the text will be change
        if (new_size.upper() == "L" or
            new_size.upper() == "M"):
            t_shirt: str = f'The size of this t-shirt is: {new_size.upper()}\nand the text will be: I love Python.'
        
        else:
            t_shirt: str = f'The size of this t-shirt is: {new_size.upper()}\nand the text will be: {text}'
            
    return t_shirt

########################################################################################################################################################

def make_album(artist: str, album: str, songs: int = None) -> dict:
    """Take an artist name and an album title, 
    and it return a dictionary containing these two pieces of information.
    """
    
    album: dict = {'artist': artist, 'title': album}
    if songs not in album:
        album["songs"] = songs
    
    return album
        
metal: dict = make_album("Iron Maiden", "Fear Of The Dark")
rock: dict = make_album("Dire Straits", "Money For Nothing")
rap: dict = make_album("Fabri Fibra", "Controcultura", 18)

########################################################################################################################################################

def sandwiches_ingredients(ing1: str, ing2: str, ing3: str, ingr4: str ) -> None:
    """Accept a list of items a person wants on a sandwich."""
    
    sandwiche: list = [ing1, ing2, ing3, ingr4]
    
    print(f"The ingredients are: {sandwiche}")
       