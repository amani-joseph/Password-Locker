from user import User
import random
import string
from userDetails import read_from_file, write_to_file

data_file = "credentials.csv"
class Credentials:
    '''
    This class handles credentials of our user
    '''
    credentials=[]

    def __init__(self,account,username,password):
        '''
        method that initialise our object user
        '''
        self.account=account
        self.username=username
        self.password=password

    def __str__(self):
        '''
        methods that output the user details inform of a string
        '''
        return "Your Username: " + self.username +" \n Your password is:"+ {self.password}

    def __repr__(self):
        '''
        method that return all credentials
        '''
        return (f'Credentials {self.account} {self.username} {self.password}')

    @classmethod
    def verifyDetails(cls, username,password):
        '''
        method to verify if a user exist
        '''            

        our_user_details=  ''
        for user in User.users:
            if user.username==username and user.password==password:
                our_user_details=user.username
                return our_user_details

    def save_credentials(self):
        write_to_file(data_file,self)
        Credentials.credentials.append(self)

    print(credentials)     

    @classmethod
    def search_credentials(cls,account):
        '''
        method that search an existing account
        '''     
        for credentials in cls.credentials:
            if credentials.account==account:
                return credentials.__repr__()
    @classmethod
    def display_credentials(cls):
        '''
        method that displays the account details
        '''
        read_from_file("users.csv")
        read_from_file("credentials.csv")
        return cls.credentials            
    @classmethod
    def delete_credentials(cls,account):
        '''
        method that checks if a user exist and delete it 
        '''
        for  credentials in cls.credentials:
            if credentials.account == account:
                cls,credentials.remove(credentials)
                return cls.credentials

    @classmethod
    def check_if_credentials_exist(cls,account):
        '''
        method that checks existence of a credentials
        '''
        for credentials in cls.credentials:
            if credentials.account==account:
                return True
        return False

    
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

         gen_password = ""
         for char in password_list:
               gen_password += char
     #     return gen_password     
         print(f"Your password is: {gen_password}")
    