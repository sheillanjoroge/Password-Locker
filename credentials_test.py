import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class
from user import User
import csv, os

Class TestCredentials(unittest.TestCase):

'''

def setUp(self):
    '''
    Setup up method to run before each test cases.
    '''
    self.test_user_credential = Credential('sheillan.njoroge@gmail.com', 'instagram', 'zay22')
    self.test_other_user_credential = Credential('sheillan.njoroge@gmail.com', 'twitter', 'zay22')

def tearDown(self):
        '''
        Delete the credentials database after every test.
        '''
        if os.path.isfile(Credential.database):
            os.remove(Credential.database)
 
def test_init(self):
     '''
     test_init test case to test if the object is initialized properly
     '''

     self.assertEqual('sheillan.njoroge@gmail.com', self.test_user_credential.get_email())
     self.assertEqual('Instagram', self.test_user_credential.get_account())
     self.assertEqual('zay22', self.test_user_credential.get_password())

def test_create_credentials_file(self):
        '''
        Test that the db is created successfully.
        '''

        with open(Credential.database, 'w+') as test_file:
            file_exists = os.path.isfile(Credential.database)
            self.assertTrue(file_exists)

def test_record_a_credential(self):
        '''
        Test that a credential is always created and stored in the db successfully
        '''

        self.test_user_credential.create_credential()
        self.test_other_user_credential.create_credential()
        with open(Credential.database, 'r')as read_file:
            fields = ['account', 'email', 'password']
            data_read = csv.DictReader(read_file, fields, lineterminator='\n')
            self.add_success = False
            counter = 0
            for line in data_read:
                counter += 1
                if line['email'] == 'sheillan.njoroge@gmail.com' and line['account'] == 'Twitter' and line['password'] == 'zay22':
                    self.add_success = True 
   
            self.assertTrue(self.add_success)

def test_check_account_exist(self):
        '''
        From the instance method. Search the db and ensure an account exists
        '''
        self.test_user_credential.create_credential()

        account_exist = self.test_user_credential.check_account_exist()
        self.assertTrue(account_exist)

def test_check_account_exist(self):
        '''
        From the class method. Search the db and ensure an account exists
        '''
        self.test_user_credential.create_credential()

        account_exist = Credential.check_an_account_exist(self.test_user_credential.get_email(), self.test_user_credential.get_account())
        self.assertTrue(account_exist)

def test_check_account_exist_without_db(self):
        '''
        Tests and ensures check_an_account_exist() does not return True if the db is nonexistent.
        '''
        account_exist = Credential.check_an_account_exist(self.test_user_credential.get_email(), self.test_user_credential.get_account())
        self.assertFalse(account_exist)

def test_randomizer(self):
        '''
        Tests and ensures the radomizer() generates a legit passwords
        '''
        random_password = Credential.randomizer()
        self.assertGreater(len(random_password), 7)
        self.assertLess(len(random_password), 9)

def test_display_accounts(self):
        self.test_other_user_credential.create_credential()
        self.test_user_credential.create_credential()

        list_of_credentials = Credential.display_accounts(self.test_user_credential.get_email())
        for a_credential in list_of_credentials:
            a_credential_exist = Credential.check_an_account_exist(a_credential['email'], a_credential['account'] )
            if not a_credential_exist:
                return False
        
        self.assertTrue(a_credential_exist)            


def test_delete_account(self):
        '''
        Tests and ensures delete op occurs successfully.
        '''
        self.test_user_credential.create_credential()
        account_created = Credential.check_an_account_exist(self.test_user_credential.get_email(), self.test_user_credential.get_account())
        is_deleted = Credential.delete_account(self.test_other_user_credential.get_email(), self.test_other_user_credential.get_account())

        list_of_credentials = Credential.display_accounts(self.test_user_credential.get_email())

        account_exist = False
        for account in list_of_credentials:
            if account['account'] == self.test_user_credential.get_account():
                account_exist = False
            else:
                account_exist = True
        self.assertTrue(account_created)
        self.assertTrue(is_deleted)
        self.assertFalse(account_exist)


if __name__ == '__main__':
    unittest.main()