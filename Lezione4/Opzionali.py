# Francesca Scippa
# 2024/04/30

#1.School Grading System:
#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average, 
#and a message indicating whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.

def school_grading_system(name: str, scores: list) -> None:
    """ Accepts two paraments, name and scores.
    The output will be a list with all the grades entered, 
    calculating the average of them.
    """
    for score in scores:
        if score >= 60:
            print(f"You pass the exame with {score}!")
        elif score < 60:
            print(f"You don't pass the exam! {score} is not enough!")
        
        som: float = sum(scores)
        result: float = som / len(scores)
        
        
    
    print(f"{name}'s scores are {scores}")
    print(f"Your average is {result}")
    
scores: list = [60, 75.5, 82, 55.5]    

#school_grading_system("Francesca", scores)

#2.Guess the Number Game:
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too high, 
#too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.   

def guess_the_number(start: int, stop: int) -> None:
    """Accepts two paraments, min and max number.
    You have to guess the random number between these extremes. 
    """
    import random
    
    n_random: int = random.randint(start,stop)
    
    t = 0
    while t <= 10:
        
        n_user: int = int(input("Insert your attempt: "))
        
        if n_random == n_user:
            print("You Win!")
            break
        
        if n_random > n_user:
            diff: int = n_random - n_user
        
        else:
            diff: int = n_user - n_random
            
        if diff < 2:
            t += 1
            print("Big Fire!")
        
        elif diff >= 2 and diff < 4:
            t += 1
            print("Fire")
        
        elif diff >= 4 and diff < 7:
            t += 1
            print("Water")
        
        elif diff  >= 7 and diff < 10:
            t += 1
            print("Downpour")
        
        elif diff > 20:
            t += 1
            print("Completely changes number")
            
#print(guess_the_number(1, 10))

#3.E-commerce Shopping Cart:
#Create a function that defines a product with a name, price, and quantity.
#Create a function that manages the shopping cart, allowing the user to add, remove, 
#and view products in the cart.
#The function should calculate the cart total and apply any discounts or taxes.
#Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

def products() -> None:
    """Print all of products"""
    
    print("### Welcome, to our online store! ####\nThese are our products.")
    
    product: dict= {'T-shirt':{"product":'T-shirt',"price": "19.99€", "quantity": 1},
    'Skirt':{"product":'Skirt',"price":"35.50€", "quantity": 1},
    'Shoes':{"product":'Shoes',"price":"80.00€", "quantity": 1},
    'Trouses':{"product":'Trouses',"price":"45.20€", "quantity": 1},
    'Socks':{"product":'Socks',"price":"9.99€", "quantity": 1},
    'Accessories':{"product":'Accessories',"price":"4.50€", "quantity": 1},
    'Belt':{"product":'Belt',"price":"25.00€", "quantity": 1}}
    
    for item in product.values():
        print(item)
    
    print("### Happy Shopping! ###")

def add_cart(cart: list, product: str) -> None:
    """Add the product in the cart."""
    cart.append(product) 
    
def remove_cart(cart:list , product_name: str) -> None:
    """Revome the product to the cart."""
    for item in cart:
        if item['product'] == product_name:
            cart.remove(item)
            break  

def view_cart(cart: list) -> None:
    """Shows you what is in the cart."""
    if cart:
        print("You shopping cart: ")
        for item in cart:
            print(f"product {item['product']}, price: {item['price']}€, quantity: {item['quantity']}") 
    else:
        print("Your cart is empty.")
        
def calculate_tot(cart: list) -> None:
    """Calculate the total of the cart."""
    total: float = sum(item['price'] * item['quantity'] for item in cart)
    return total

product: dict= {'T-shirt':{"product":'T-shirt',"price": 19.99, "quantity": 1},
    'Skirt':{"product":'Skirt',"price": 35.50, "quantity": 1},
    'Shoes':{"product":'Shoes',"price": 80.00, "quantity": 1},
    'Trouses':{"product":'Trouses',"price": 45.20, "quantity": 1},
    'Socks':{"product":'Socks',"price": 9.99, "quantity": 1},
    'Accessories':{"product":'Accessories',"price": 4.50, "quantity": 1},
    'Belt':{"product":'Belt',"price": 25.00, "quantity": 1}}

cart: list = []

while True:
    
    products()
    
    name: str = input("Enter the product you want to buy: ")
    quantity: int = int(input("How many do you want?(Type a number 1 from 10): "))
    
    if name in product.keys():
        price = product[name]["price"]
        object = {"product": name, "price": price, "quantity": quantity}
        add_cart(cart, object)
    else:
        print("Product not found!")
        
    message: str = input("Do you wanto to continue your shopping? (y/n): ").lower()
    if message != "y":
        break
    
    view_cart(cart)
    tot: float = calculate_tot(cart)
    print(f"Total: {tot}€")
    
    message_remove: str = input("Do you want to remove any product from your cart? (y/n): ").lower()
    if message_remove == 'y':
        product_name: str = input("Enter the product you want to remove: ")
        remove_cart(cart, product_name)
        view_cart(cart)
        tot: float = calculate_tot(cart)
        print(f"Total: {tot}€")
    
#5. Inventory Management System:
#Create a function that defines an item with a code, name, quantity, and price.
#Create a database or dictionary to store the items in inventory.
#Implement functions to add, remove, search, and update items in the inventory.
#Use for loops and conditional statements to manage the various inventory operations.

def item(code: int, name: str, quantity: int, price: float) -> dict:
    """Defines an item, with the paraments request."""
    items: dict = {'code': code, 'name': name, 'quantity': quantity, 'price': price}
    return items
    
def add_items(inventory: dict, item: dict) -> None:
    """Add a new item in the dictionary."""
    code = item['code']
    if code not in inventory:
        inventory[code] = item
    
def remove_item(inventory: dict, item_code: str) -> None:
    """Remove an item in the dictionary."""
    if item_code in inventory:
        inventory.pop(item_code)
    else:
        print("The item with this code dosen't exist in the inventory.")

def update_item(inventory: dict, item_code) -> None:
    """If the item already exists increase its quantity by 1."""
    if item_code in inventory:
        inventory[item_code]['quantitaty'] += 1
    else:
        print("The item with this code dosen't exist in the inventory.")

inventory: dict = {} 

while True:
    