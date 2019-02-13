from user import User
import string
import random
class Credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_list =[]
	user_credentials_list = []
	@classmethod
	def check_user(cls,username,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.user_list:
			if (user.username == username and user.password == password):
				current_user = user.username
		return current_user

	def __init__(self,user_name,site_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		
		self.user_name = user_name
		self.site_name = site_name

		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		
		Credential.credentials_list.append(self)
	
	def generate_password(self,size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

	@classmethod
	def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list