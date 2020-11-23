import unittest
from user import User
import csv, os

class TestUsers(unittest.TestCase):

    def setUp(self):
        '''
        Set up data to be used in all the tests.
        '''
        self.new_user = User('Sheilla', 'Njoroge', 'sheilla@gmail.com','zay22' )

    def tearDown(self):
        '''
        Clean up data after all tests.
        '''
        if os.path.isfile(User.database):
            os.remove(User.database)
       
    def test_read_file(self):
        '''
        Test to ensure method can read data from the db.
        '''
        #Setup
        with open(User.database, 'w') as write_file:
            data_to_write = "This is a test to see if it works"
            write_file.write(data_to_write)
        
        #Perform
        data_after_read = self.new_user.read_file()
            
        #Test
        self.assertEqual(data_to_write, data_after_read)

    def test_create_user(self):
        #Test
        self.assertEqual('sheilla', self.new_user.get_first_name())
        self.assertEqual('njoroge', self.new_user.get_last_name())
        self.assertEqual('sheilla@gmail.com', self.new_user.get_email())
        self.assertEqual('zay22', self.new_user.get_password())
    
    def test_check_account_exist(self):
        '''
        Test to ensure method can search if a user exists on th db.
        '''
        #Setup 
        self.new_user.create_account()

        #Perform
        account_exists = User.check_account_exist(self.new_user.get_email(), self.new_user.get_password())

        self.assertTrue(account_exists)

    def test_create_account(self):
        '''
        Test to rndure method can succussfully create a user account on the db.
        '''
        #Perform
        first = self.new_user.create_account()
 
        #Test
        if first:

            with open(User.database, 'r') as file_read:
                data = csv.DictReader(file_read)
                
                counter = 0
                record_exists = False
                for line in data:
                    if line['email'] == self.new_user.get_email() and line['password'] == self.new_user.get_password():
                        counter +=1
                        record_exists = True
            self.assertTrue(record_exists)


    def test_delete_account(self):
        '''
        Test to ensure method can successfully delete a user from the db.
        '''
        #Setup
        self.new_user.create_account()
        data_on_file_before = self.new_user.read_file()

        #Perform
        self.new_user.delete_account()
        
        #Test
        data_on_file_after = self.new_user.read_file()
        self.assertNotEqual(data_on_file_before, data_on_file_after)

if __name__ == '__main__':
    unittest.main()