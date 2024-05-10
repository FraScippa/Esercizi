
class Resturant:
    
    def __init__(self, resturant_name: str, cusine_type: str, number_served: int):
        
        self.resturant_name: str = resturant_name
        self.cusine_type: str = cusine_type
        self.number_served: int = number_served
        
    def __str__(self) -> str:
        return f"\nThe resturant's name is {self.resturant_name}, and the cusine type is {self.cusine_type} They served {self.number_served} customers" 
    
    def descrive_resturant(self): 
        return self.__str__()
         
    def open_resturant(self):
        print(f"The resturant {self.resturant_name} is Open!")
        
    def set_number_served(self, new_number_served: int):
        self.number_served: int = new_number_served
    
    def increment_number_served(self, increment_served: int):
        if self.number_served:
            self.number_served += increment_served
        else:
            self.new_number_served += increment_served
            
##########################################################################################

from importUser import User

class Privileges:
    
    def __init__(self, privileges: list[str]):
        
        self.privileges: list[str] = privileges
        
    def __str__(self):
        s: str = ""
        for privilege in self.privileges:
            s += privilege + ", "
        return f"\nThe Admin privileges are: {s} "
    
    def show_privileges(self):
        return self.__str__()

class Admin:
    
    def __init__(self, user: User, privileges: Privileges):
        
        self.privileges: Privileges = privileges
        self.user: User = user

    def show_privileges(self):
        return str(self.privileges)