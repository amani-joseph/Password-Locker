import random
import string
data_file = "users.csv"
class User:
     user_list = ['testuser','12345']
     
     def __init__(self, user_name, password):
          self.user_name = user_name
          self.password = password
          
     def save_user(self):
          User.user_list.append(self)
     def __repr__(self) -> str:
             return f"{self.username}"  


     @classmethod
     def show_user(cls):
        return cls.users      

     def find_by_username(cls,username):
        '''
        method to find the user using username
        '''    
        for user in cls.users:
            if user.username==username:
                return user
     def find_user(cls):
        '''
        method to find user in the list
        '''            
        return cls.users

     def delete_user(cls,username):
        '''
        method to delete an existing user
        '''
        for user in cls.users:
            if username==username:
                cls.users.remove(user)
                return True
            return False    

     def del_user(self):
        '''
        method to delete a single user
        '''
        User.users.remove(self)
        return True 
     
     def generate_password():
          letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
          numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
          symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
          print("Welcome to the Password Generator!")
          nr_letters = int(input("How many letters would you like in your password?\n")) 
          nr_symbols = int(input(f"How many symbols would you like?\n"))
          nr_numbers = int(input(f"How many numbers would you like?\n"))
          password_list = []

          for char in range(1, nr_letters + 1):
                    password_list.append(random.choice(letters))

          for char in range(1, nr_symbols + 1):
                    password_list += random.choice(symbols)

          for char in range(1, nr_numbers + 1):
                    password_list += random.choice(numbers)

          print(password_list)
          random.shuffle(password_list)
          print(password_list)

          master_password = ""
          for char in password_list:
                    master_password += char
               
          print(f"Your password is: {master_password}")