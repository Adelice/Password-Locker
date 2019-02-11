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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","Testuser","yvonne","yvonne") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

if __name__ == '__main__':
    unittest.main()