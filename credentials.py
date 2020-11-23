class Credentials:
    '''
    Class that stores the credetials of the user
    '''

    def __init__(self, account, email, password):
        self.account = account
        self.email = email
        self.password = password
    
    def get_account(self):
        '''
        Returns a credentials account and determines which platform the password is used for.
        '''
        return self.account

    def get_email(self):
        '''
        Get email of the particular credential.
        '''
        return self.email  

    def get_password(self):
        '''
        Returns a credential's password.
        '''
        return self.password