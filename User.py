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
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)
   