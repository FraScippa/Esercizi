#Francesca Scippa

#08-05-2024

class Food:

    def __init__(self, name: str, price: float, description: str):

        self.name: str = name
        self.price: float = price
        self.description: str = description
    
    def __str__(self) -> str:
        return f"Food: {self.name}\nPrice: {self.price}\nDescription: {self.description}"

class Menu:

    def __init__(self, foods: list[Food] = []):
        self.foods: list[Food] = foods
    
    def add_food(self, food: Food): #eulazione set con un contatore che rimane 1
        count: int = 0
        for food_menu in self.foods:
            if food.name != food_menu.name:
                count += 1 
                food_menu.price = food.price
        if count == 0:
            self.foods.append(food)
    
    def remove_food(self, food: Food):
        if food in self.foods:
            self.foods.remove(food)
 
    def get_avg_price(self) -> str:
        total_sum: float = 0
        for food in self.foods:
            total_sum += food.price
        avg_price: float = total_sum/len(self.foods)
        return avg_price

    def __str__(self)-> str: #questa funzione chiama altre funzioni ed è per stampare una stringa
        repr: str = "" #inizializzi una stringa vuota
        for food in self.foods:
            repr += food.__str__() + "\n"
        avg_price: float = self.get_avg_price()
        repr += "_"*30 + "\n"
        repr += f"Prezzo Medio = {avg_price}"
        return repr

pizza: Food = Food("Margherita", 7.50, "Pizza's with mozzarella and tomatos")
#print(pizza)
#print("_"*45)

pasta: Food = Food("Pasta al sugo", 6.00, "Pasta with tomato")
#print(pasta)
#print("_"*45)

steack: Food = Food("Steack", 12.50, "Beef of Cow")
#print(steack)
#print("_"*45)

menu: Menu = Menu()
menu.add_food(pizza)
menu.add_food(pasta)
menu.add_food(steack)

print(menu)

#menu.remove_food(pizza)
#print(menu)











