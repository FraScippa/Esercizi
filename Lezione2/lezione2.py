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

'''print(invites)'''

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
    if idx < 3:
        print(guest)
    else:
        delate: str = invites.pop(idx)
        sorry.append(delate)        
print(sorry)














