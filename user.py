class User:
     '''
    A user class initialization
    '''

     user_list = []
     
     def __init__(self, user_name, password):
          """
        Args:
        Username(string)
        password(string)
        """
        
          self.user_name = user_name
          self.password = password
          
          
     def save_user(self):
          '''        
        saving Users
        '''     
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
    