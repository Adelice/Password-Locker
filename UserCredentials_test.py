from User import User
import unittest

class TestUsers(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Nancy","Umutoni","Adelice","1000Adel") # create contact object 

    def test_init(self):   
           '''
           test_init test case to test if the object is initialized properly
           '''
           self.assertEqual(self.new_user.first_name,"Nancy")
           self.assertEqual(self.new_user.last_name,"Umutoni")
           self.assertEqual(self.new_user.username,"Adelice")
           self.assertEqual(self.new_user.password,"1000Adel")
     
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
         '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)