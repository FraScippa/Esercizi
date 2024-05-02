#Francesca Scippa

#02-05-2024

#1. Create a Playlist:
#Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
#The function should return a dictionary with the playlist name and a set of songs. 
#Call the function with different numbers of songs to demonstrate flexibility.
#Example: create_playlist("Road Trip", {"Song 1", "Song 2"})
#Write a function called add_like() that accepts a dictionary, the name of a playlist, 
#and a boolean value indicating whether it is liked (True or False). This function should return an updated dictionary.
#Example: add_like(dictionary, “Road Trip”, liked=True)

def create_playlist(album: str, *songs: set) -> dict:
    """Creates a dictionary that accepts albums and songs as parameters"""
    playlist: dict = {album: set(songs)}
    
    return playlist

#print(create_playlist('Album1', 'Hakunamatata', "Nella vecchia fattoria", 'Allelujia' , 'Hakunamatata'))

def add_like(diz: dict, name: str, like: bool = True) -> dict:
    """if the playlist is in the dictionary then it will give true among the liked"""
    diz1: dict = {}
    
    for key, value in diz.items():
        diz1[key] = value
    
    diz1["liked"] = like
    
    if name in diz:
        diz1["liked"] = True
    else:
        diz1["liked"] = False
    
    
    return diz1

album: dict = create_playlist("Controcultura",'Turbe Giovanili','Donne')

#print(add_like(album, 'Album1', ))

#2. Book Collection:
#Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. This function should return a dictionary where the author's name is the key and the value is a list of their books. Demonstrate this function by adding books for different authors.
#Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
#Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. 
#This function should return an updated dictionary.
#Example: delete_book(dictionary, “Mark Twain”)

def add_book(autor: str, *title: str) -> dict:
    """Add books in a dictionary, the key is the autor."""
    books: dict = {autor: [title]}
    
    return books

#print(add_book("Gorge R.R. Martin", "Game Of Thrones","Fire And Blood"))

def delete_book(diz: dict, autor: str) -> dict:
    """Delete all the list connected to the autor"""
    if autor in diz:
        del diz[autor]
    
    return diz

book: dict =  add_book("Gorge R.R. Martin", "Game Of Thrones","Fire And Blood")

#print(delete_book(book, "Gorge R.R. Martin"))

#3. Personal Info:
#Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
#Make occupation, location, and age optional parameters. Use this function to create profiles for different people, 
#demonstrating how it handles these optional parameters.
#Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)

def build_profile(name: str, surname: str, *info) -> dict:
    """The paramenters are name, surname, occupation, location and age."""
    
    profile: dict = {"Name": name, "Surname": surname, "Occupation": info[0], "Location": info[1], "Age": info[2]}
    
    return profile

#print(build_profile('Sophia Jade','Phippen','Teacher','Milan', 26))

#4. Event Organizer:
#Write a function called plan_event() that accepts an event name, a list of participants, and an hour. 
#The function should return a dictionary that includes the event name and a list of the participants. 
#Call this function with varying numbers of participants to plan different events.
#Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)
#Write a function called modify_event() that accepts a dictionary, an event name, 
#and new details to modify an already planned event.
#Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)  

def plan_event(name: str, guest: list, hour: str) -> dict:
    """Accepts an event name, a list of participants, and an hour. """
    event: dict = {name: guest, "hour": hour}
    return event

#print(plan_event('PatryHard', ['Christian','Filippo'],'10pm'))

def modify_event(diz: dict, event: str, hour: str) -> dict:
    """Accepts a dictionary, an event name,
    and new details to modify an already planned event.
    """
    if event not in diz:
        diz['hour'] = hour
    
    return diz

event: dict = plan_event('PatryHard', ['Christian','Filippo'],'10pm')

#print(modify_event(event, 'PartyHard', '2am'))

#5. Shopping List:
#Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. 
#It should return a dictionary with the store name and a set of items to buy there. 
#Test the function with different stores and item lists.
#Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})
#Write a function called print_shopping_list() that accepts a dictionary and a store name, 
#then prints each item from that store's shopping list.
#Example: print_shopping_list(dictionary, "Grocery Store")

def create_shopping_list(store_name: str, *items: set) -> dict:
    """Accepts a store name and any number of items as arguments.""" 
    diz: dict = {store_name: set(items)}
    
    return diz

#print(create_shopping_list("Coop", "Bread","Milk", "Eggs", "Bread"))

def print_shopping_list(diz: dict, store_name: str) -> None:
    """Accepts a dictionary and a store name, 
    then prints each item from that store's shopping list.
    """
    for key, value in diz.items():
        print(key,":",value)
    
shopping_list: dict = create_shopping_list("Coop", "Bread","Milk", "Eggs", "IceCream")

print_shopping_list(shopping_list, "Coop")   
