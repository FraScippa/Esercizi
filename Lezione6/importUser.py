
class User:
    
    def __init__(self, first_name: str, last_name: str, age: int, height: float):
        
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.height: int = height
        self.login_attempts: int = 0
    
    def __str__(self) -> str:
        return f"User(name: {self.first_name}\nlast name: {self.last_name}\nage:{self.age}\nheight: {self.height}\nlogin attempts: {self.login_attempts}"
    
    def describe_user(self):
        return self.__str__()
        
    def greet_user(self):
        print(f"Hello {self.first_name}! How are you?")
        
    def increment_login_attemps(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0