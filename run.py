import random
from user import User

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
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
          password += char
     
     return gen_password
     # print(f"Your password is: {password}")

def main ():
     while True:
          print('Welcome to password locker')
          print('\n')
          print('select a code to navigate: to create an account use "new_user": To login to your account "login" : To exit "exit"')
          short_code = input().lower()
          print('\n')
          
          if short_code == 'new_user':
               print("create user name")
               created_user_name = input()
               
               print("create password")
               created_user_password = input()
               
               print("confirm password")
               confirm_password = input()
               
               while confirm_password != created_user_password:
                    print('Your passwords did not match')
                    print('Re-enter your password')
                    print('\n')
                    created_user_password = input()
               
                    print("confirm password")
                    confirm_password = input()
               else:
                    print(f"congratulations {created_user_name} ! your acccount has been successfull")
                    print('\n')
                    print('proceed to login')
                    print('User name:')
                    entered_user_name = input()
                    print('Enter your password')
                    entered_password = input()
                    
               while entered_user_name != created_user_name or entered_password != created_user_password:
                    print('invalid user name or password')
                    print('User name:')
                    entered_user_name = input()
                    print('Enter your password')
                    entered_password = input()
               else:
                    print(f"Welcome {entered_user_name} !! to your account, \n Do you want to add (a) your passwords")
                    entered_password_management = input('you have no passwords to view yet select "a" to add: _')
                    if entered_password_management == 'a':
                         new_account= input('account: ')
                         new_account_username= input('User name: ')
                         print('Do you want to auto-generate a password ?')
                         password_answer = input(" yes: 'y' or no: 'n ")
                         if password_answer == 'y':
                              generate_password()
                         if password_answer == 'n':
                              print('enter your password the good old way')
                              account_password = input('password: ')
                              
                    print('\n')
                    
          elif short_code == "login":
               print('Welcome back')
               print('Enter your user name')
               default_user_name = input()
               print('Please enter your password')
               default_user_password = input()
               print('\n')
               
               while default_user_name != 'testuser' or default_user_password != "12345":
                    print('Wrong username and password')
                    print('Enter username')
                    default_user_name = input()
                    print('Please enter your password')
                    default_user_password = input()
                    print('\n')
               else:
                    print('login success')
                    print(f"Welcome !! to your account, \n Do you want to view (v) or add (a) your passwords")
                    entered_password_management = input("'v' or 'a':  _")
                    if entered_password_management == 'v':
                         for user in User.user_list: print(user)
                    elif entered_password_management == 'a':
                         new_account= input('account: ')
                         print('Do you want to auto-generate a password ?')
                         password_answer = input(" yes: 'y' or no: 'n ")
                         if password_answer == 'y':
                              generate_password()
                         if password_answer == 'n':
                              print('enter your password the good old way')
                              account_password = input('password: ')
                      
                    print('\n')
          elif short_code == "exit":
               break
          else:
               print('enter valid code to proceed accordingly')
      
if __name__ == "__main__":
     main()