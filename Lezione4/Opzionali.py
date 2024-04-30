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

                 
            
    
    




    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
    
    
       
    
    

