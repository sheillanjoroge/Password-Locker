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

    def set_password(self, password):
        '''
        Sets the credential's password.
        '''
        self.password = password

    def create_credential(self):
        '''
        Stores the credential to the db (csv file)
        '''

        file_exist = os.path.isfile(Credential.database)
        with open(Credential.database, 'a')as file_to_write:
            if not file_exist:
                fields = ['account', 'email', 'password']
                file_data = csv.DictWriter(file_to_write, fieldnames=fields, lineterminator='\n')
                file_data.writeheader()
                file_data.writerow({
                    'account': self.get_account(),
                    'email': self.get_email(),
                    'password': self.get_password() 
                })
                return True
            else:
                fields = ['acount', 'email', 'password']
                file_data = csv.DictWriter(file_to_write, fieldnames=fields, lineterminator='\n')
                file_data.writerow({
                    'account': self.get_account(),
                    'email': self.get_email(),
                    'password': self.get_password() 
                })
                return True
    def check_account_exist(self):
        '''
        Returns True of False if the Credential exists for the user.
        '''
        with open(Credential.database, 'r')as read_file:
            fields = ['account', 'email', 'password']
            read_data = csv.DictReader(read_file, fieldnames=fields)
            for line in read_data:
                if line['account'] == self.get_account() and line['email'] == self.get_email():
                   return True
            return False

    @classmethod
    def check_an_account_exist(cls, account, email):
        '''
        check_account_exist but not called from a credential instance.
        '''

        db_present = os.path.isfile(Credential.database)
        if db_present:
            with open(Credential.database, 'r')as read_file:
                fields = ['account', 'email', 'password']
                file_data = csv.DictReader(read_file, fieldnames=fields)
                for line in file_data:
                    if line['account'] == account and line['email'] == email:
                        return True
                return False
        else: return False