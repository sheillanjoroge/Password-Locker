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
 
 def test_init(self):
     '''
     test_init test case to test if the object is initialized properly
     '''

     self.assertEqual('sheillan.njoroge@gmail.com', self.test_user_credential.get_email())
     self.assertEqual('Instagram', self.test_user_credential.get_account())
     self.assertEqual('zay22', self.test_user_credential.get_password())