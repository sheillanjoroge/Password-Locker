#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_new_user(username,password):
    '''
    function that creates a user using a password and username
    '''
    new_user = User(username,password) 
    return new_user
def save_user(user):
    '''
    function that saves a new user
    '''
    user.save_user()

def display_user(user):
    '''
    function that displays user
    '''
    return User.display_user()

def login_user(password,username):
    '''
    a fumction that checks if the users already exist 
    '''
    checked_user = Creditials.verify_user(password,username)
    return checked_user

def create_new_credential(account,username,password):
    '''
    function that create new credential details for a new user
    '''
    new_credential = Creditials(account,username,password)
    return new_credential

def save_creditials(credentials):
    '''
    function that addes a new credential to the credential
    '''
    credentials.save_user_creditials()

def delete_credentials(credentials):
    '''
    function that deletes credentials from the credential list
    '''
    credentials.delete_creditials()
def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Creditials.find_by_number(account)

def check_credentials(account):
    '''
    function that checks if the credentials of the searching name exist and return true or false
    '''
    return Creditials.creditials_exist(account)

def generate_password(self):
    ''' 
    function tht generates password
    '''
    auto_password = Creditials.generate_password(self)
    return auto_password

