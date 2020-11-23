import csv, os
class User:
    '''
    Create User's instance
    '''

    database = 'users.csv'
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def get_first_name(self):
        '''
        Return user instance first name
        '''
        return self.first_name

    def get_last_name(self):
        '''
        Return user instsnce lsst name
        '''
        return self.last_name

    def get_email(self):
        '''
        Return user instance email
        '''
        return self.email
       
    def get_password(self):
        '''
        Return user instance password
        '''
        return self.password
    
    def set_password(self, password):
        '''
        Set user instance password
        '''
        self.password = password
