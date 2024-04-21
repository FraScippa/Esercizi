# Francesca Scippa
# 2024/04/17

#print("Hello World")

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

invites: list = ['Marco', 'Davide', 'Filippo', 'Christian']

'''for person in invites:
    print(f"Ehy {person}, vuoi venire a cena?")'''

'''messageM: str = f"Hey,{invites[0]}! Vorresti venire a cena?"
messageD: str = f"Hey,{invites[1]}! Vorresti venire a cena?"
messageF: str = f"Hey,{invites[2]}! Vorresti venire a cena?"
messageC: str = f"Hey,{invites[3]}! Vorresti venire a cena?"'''

#print(f"{messageM} \n {messageD} \n {messageF} \n {messageC} ")

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

#change item 3, on the list
invites[3]: str = 'Lorenzo'

#loop list item
'''for person in invites:
    print(f"Ehy {person}, vuoi venire a cena?")'''

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
#Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5.
#Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

#change invites
invites.insert(0, 'Giovanni')
invites.insert(2, 'Angelo')
invites.append('ALberto')

#loop list item
for person in invites:
    message: str = f"Ehy {person}, vuoi venire a cena?"
    print(message)

print(invites)

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, 
#and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program.

sorry: list = []

for idx, guest in enumerate(invites):
    if idx < 5:
        print('Ehy!',guest,'the dinner is cancelade, I\'m so sorry :(.')
    else:
        delate: str = invites.pop(idx)
        sorry.append(delate)   
        
#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#•->Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#•->Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#•->Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#•->Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.

visit: list = [ 'Tokyo', 'Rio', 'Paris', 'NewYork']
sort: list = visit.sort()
reverse: list = visit.reverse()
sorted: list = sorted(visit)
print(f"normal list {visit} \n reverse {reverse} \n sorted {sorted} \n sort {sort} ")

#3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
#use len() to print a message indicating the number of people you’re inviting to dinner.

number_invites: int = len(invites)
print(f"The guests are {number_invites}")

#3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains,
#rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

items: list = []

#start a loop
while True:
    
    #ask an item 
    item: str = input('please, write an item (write stop for ending): ').strip()
    
    #check, transforming item in lowercase and stop the loop 
    if item.lower() == 'stop':
        print('Ending the program...')
        print('Final items:', items)
        break
    #add new item in items list
    elif item not in items:
        items.append(item)
        print(items)

#6-1. Person: Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. 
#Print each piece of information stored in your dictionary.

#Welcome message
print("### Please, write your personal information ###")

person: dict = {}

#add information request
first_name: str = input('First Name: ').title()
last_name: str = input('Last Name: ').title()
age: int = int(input('Age(please, with numbers): '))
city: str = input('City: ').title()


person.update({'First Name': first_name, 'Last Name': last_name, 'Age': age, 'City': city})

print(person)
print('Thankyou')
    

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
#Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary. 
#Print each person’s name and their favorite number. For even more fun, 
#poll a few friends and get some actual data for your program.

favorite_numbers: dict = {}

while True:

    name: str = input('Enter your name: ')
    number: int = int(input('Favorite number: '))

    if name.lower() == 'stop': 
        print(favorite_numbers)
        break
    elif name not in favorite_numbers:
        favorite_numbers.update({'Name': name, 'Favorite number': number})
    

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, 
#or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary: dict = {'Variable': 'named storage location in a program that holds a value.', 
                  'Function': 'named block of code that performs a specific task or operation.',
                  'Loop': 'programming construct that repeats a block of code multiple times based on a condition.',
                  'Comment': 'piece of text in a program that is ignored by the compiler or interpreter and is used for adding notes or explanations within the code.',
                  'String': 'used to represent text data in computer programs.'}

#print one word for line and the meaning indented on a second line
for key, valute in glossary.items():
    print('-',key,'-','\n',valute)

#print the word followed by a colon and then its meaning
for key, valute in glossary.items():
    print("-",key,":",valute) 

#6-7. People: Start with the program you wrote for Exercise 6-1. 
#Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
#Loop through your list of people. As you loop through the list, print everything you know about each person.

#create 3 dictionaries
person: dict = {'Name':'Anna','Surname':'Carletti','Age':25,'City':'Milan'}
man: dict = {'Name':'Nicolò',"Surname":'Di Silvestro','Age':25,"City":'Rome'}
woman: dict = {'Name':'Sophia Jade',"Surname":'Phippen','Age':26,'City':'Milan'}

people: list = []

people.append(person)
people.append(man)
people.append(woman)

for p in people:
    print(p)

#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as you do, 
#print everything you know about each pet. 

#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
#Then print each person’s name along with their favorite numbers.

#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#Create a dictionary of information about each city and include the country that the city is in, 
#its approximate population, and one fact about that city. 
#The keys for each city’s dictionary should be something like country, population, and fact. 
#Print the name of each city and all of the information you have stored about it.

#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
#Use one of the example programs from this chapter, and extend it by adding new keys and values, 
#changing the context of the program, or improving the formatting of the output.










