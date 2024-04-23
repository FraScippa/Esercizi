
#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
#For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizzas: list = ['capricciosa','diavola','margherita']

for pizza in pizzas:
    #print(pizza) for print only pizzas.
    print(f'I like so much the {pizza}. I really love pizza!')

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, 
#such as Any of these animals would make a great pet!

animals: list = ['dog','cat','horse']

for animal in animals:
    print(f"{animal} is a great pet")
print('Any of these animals would make a great pet!')

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

numbers_20: list = [i for i in range(1,21)]

print(numbers_20)

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

'''numbers: list = [n for n in range(1000000)]

 print(numbers)'''

#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() 
#and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

numbers_milion: list = [n for n in range(1000000)]

print(f'the max number is {max(numbers_milion)} - the min number is {min(numbers_milion)}')

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
#Use a for loop to print each number.

odd_numbers: list = [odd for odd in range(1,21,2)]

print(odd_numbers)

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

mult_3: list = [n for n in range(3,31,3)]

print(mult_3)

#4-8. Cubes: A number raised to the third power is called a cube. 
#For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes: list = [n**3 for n in range(1,11) ]

print(cubes)

#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.


lista: list = [n for n in range (31)]
middle: int = len(lista)//2

print(f"The first three items in the list are: {lista[0]}, {lista[1]}, {lista[2]}")
print(f'The Three items from the middle of the list are: {lista[middle-1]}, {middle}, {lista[middle + 1]}')
print(f'The last three items in the list are: {lista[-1]}, {lista[-2]}, {lista[-3]}')

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, 
#and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, 
#and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

friend_pizzas: list = pizzas.copy() #copy the list pizzas

pizzas.append('crostino') #add a new pizza to the first list
friend_pizzas.append('napoli') #add new pizza to the list friend_pizzas

print(f'My favorite pizzas are: {pizzas}')
print(f'My friend’s favorite pizzas are: {friend_pizzas}')

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.

first_course: list = ['carbonara','amatriciana', 'boscaiola']
second_course: list = ['bistecca','aragosta', 'spigola']

first_list: list = [food for food in first_course]
second_list: list = [food for food in second_course]

print(f'{first_course}--{second_course}')

#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.

dog: str = 'Border Collie'
dog1: str = "German shepherd"

if dog == dog and dog != dog1:
    print(f"Is {dog} == Border Collie? I predict True")
    print(dog == 'Border Collie')
    print(f"Is {dog} == German shepherd? I predict False")
    print(dog == 'German shepherd')

car: str = 'Subaru'
motor: str = 'Kawasaki'

if car == car and car != motor:
    print(f"Is {car} == Subaru? I predict True")
    print(car == 'Subaru')
    print(f"Is {car} == Kawasaki? I predict False")
    print(car == 'Kawasaki')

food: str = 'Carbonara'
food1: str = 'Amatriciana'

if food == food and food != food1:
    print(f"Is {food} == Carbonara? I predict True")   
    print(food == 'Carbonara')
    print(f"Is {food} == Amatriciana? I predict False")
    print(food== 'Amatriciana')

game: str = 'CallOfDuty'
game1: str = 'LeagueOfLegends'

if game == game and game != game1:
    print(f"Is {game} == CallOfDuty? I predict True")   
    print(game == 'CallOfDuty')
    print(f"Is {game} == LeagueOfLegends? I predict False")
    print(game== 'LeagueOfLegends')

shoes: str = 'Adidas'
shoes1: str = 'Nike'

if shoes == shoes and shoes != shoes1:
    print(f"Is {shoes} == Adidas? I predict True")   
    print(shoes == 'Adidas')
    print(f"Is {shoes} == Nike? I predict False")
    print(shoes== 'Nike')

