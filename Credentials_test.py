from Credentials import Credential
from user import User
import unittest
class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User("","","","")
		self.new_user.save_user()
		user2 = User("","","","")
		user2.save_user()

		for user in User.user_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential("Nancy","Twitter","nancy")

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'Nancy')
		self.assertEqual(self.new_credential.site_name,'Twitter')
		
		self.assertEqual(self.new_credential.password,'nancy')

	def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		account = Credential("shema","Instagram","shema")
		account.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)
        
   

	
   
if __name__ == '__main__':
    unittest.main()