#!/usr/bin/env python3.6
from User import User
def create_user(fname,lname,usrname,pwd):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,usrname,pwd)
    return new_user

def save_users(User):
    '''
    Function to save contact
    '''
    User.save_user()
    
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
  

  print(f"\t\t\t\t*****WELCOME*****\n ")
  print("\t\t\t**************************************************\n")
  print("Choose What would you like to do")

  print('\n')
  while True:
                    print("Use these short codes : cc - create a new user,\n dc - display users, \n ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("Create an account")
                            print("-"*60)
                            print ("Enter your First name ....")
                            f_name = input()

                            print("Enter your Last name ...")
                            l_name = input()

                            print("Enter your username...")
                            user_name = input()

                            print("Enter your password...")
                            pswd = input()
                            save_users(create_user(f_name,l_name,user_name,pswd))
                            print(" ")
                            print(f'New Account Created for: {f_name} {l_name} using username: {user_name} and password: {pswd}')
                            
                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.username} {user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')
if __name__ == '__main__':

    main()

