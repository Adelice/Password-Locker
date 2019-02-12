class User:
    """
    class that generates new instances of contacts
    """
    def __init__(self,first_name,last_name,username,password):

        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.password=password
    user_list = [] #Empty user list
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False
    