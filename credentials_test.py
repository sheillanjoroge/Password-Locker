import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

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
        '''Test that the db is created successfully.'''

        with open(Credential.database, 'w+') as test_file:
            file_exists = os.path.isfile(Credential.database)
            self.assertTrue(file_exists)

def test_record_a_credential(self):
        '''Test that a credential is always created and stored in the db successfully'''

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
