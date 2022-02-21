import random
from user import User
from credentials import Credentials


def create_our_user(username,password):
     '''
    method to create a new users account
    '''
     new_user= User(username, password)
     return new_user

def save_our_user(user):
    '''
    method to save the user created
    '''    
    user.save_user()

def show_user(user):
    '''
    method to show or display a user that have initially created
    '''
    user.show_user_created()    

def login(username,password):
    '''
    method that allow an already existing user to login to the account
    '''    
    verified_user_details=Credentials.verifyDetails(username, password)
    return verified_user_details

def create_credentials(account, username, password):
    '''
    function that create a new credential
    '''
    new_credential= Credentials(account, password, username)
    return new_credential

def save_credentials(credentials):
    '''
    method to save a new created  credentials of the account 
    '''
    Credentials.save_credentials(credentials)

def delete_credentials(credentials):
    '''
    method to delete a credentials
    '''
    Credentials.delete_credentials(credentials)

def search_credentials(account):
    '''
    method that allow search an existing credential
    '''
    return Credentials.search_credentials(account)

def show_all_credentials():
    '''
    method to display all the credentials of a user
    '''
    return Credentials.display_credentials()

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
               print('Do you want to auto-generate a password ?')
               password_answer = input(" yes: 'y' or no: 'n ")
               if password_answer == 'y':
                    created_user_password = User.generate_password()
                    # print(f'your generated {new_account} password is {generated_account_password}')
                    if password_answer == 'n':
                         print('enter your password the good old way')
                         created_user_password = input('password: ')
                         
               
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
                              entered_password_management = input('you have no passwords to view yet select "a" to add: ')
                              if entered_password_management == 'a':
                                   new_account= input('account: ')
                                   new_account_username= input('User name: ')
                                   print('Do you want to auto-generate a password ?')
                                   password_answer = input(" yes => 'y' or no=> 'n':  ")
                                   if password_answer == 'y':
                                        generated_account_password = Credentials.generate_password()
                                        print(f'your generated {new_account} password is {generated_account_password}')
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
                    print('Do you want to auto-generate a password ?')
                    password_answer = input(" yes: 'y' or no: 'n ")
                    if password_answer == 'y':
                         User.generate_password()
                    if password_answer == 'n':
                         print('enter your password the good old way')
                         default_user_password = input('password: ')
                    
                    print('\n')
               else:
                    print('login success')
                    print(f"Welcome !! to your account, \n Do you want to view (v) or add (a) your passwords")
                    entered_password_management = input("'v' or 'a':  _")
                    if entered_password_management == 'v':
                         for user in User.user_list: print(user)
                    elif entered_password_management == 'a':
                         new_account= input('account: ')
                         new_account_username= input('User name: ')
                         print('Do you want to auto-generate a password ?')
                         password_answer = input(" yes: 'y' or no: 'n ")
                         if password_answer == 'y':
                              Credentials.generate_password()
                         if password_answer == 'n':
                              print('enter your password the good old way')
                              account_password = input('password: ')
                         # save_credentials(create_credentials(new_account, new_account_username, account_password))
                    print('\n')
          elif short_code == "exit":
               break
          else:
               print('enter valid code to proceed accordingly')
      
if __name__ == "__main__":
     main()