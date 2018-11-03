import unittest #Importing the unittest module
import pyperclip
from account import Account , Credential # Importing the contact class

class TestAccount(unittest.TestCase):

    """
    Test class that defines test cases for the account class behaviours.

    Args:
    unittest.TestCase: Testcase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_account = Account("juliieemugz","julakamau") # create account object

    
    def tearDown(self):
        """
        tearDown method that does the clean-up after each test has run
        """ 
        Account.account_list = []



    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_account.username,"julakamau")



    def test_save_account(self):
        """
        test to check if the account object is saved on account list
        """
        self.new_account.save_account() #save account
        self.assertEqual(len(Account.account_list),1)



 
    def test_save_multiple_account(self):
        """
        To check if we can save multiple objects into list
        """
        self.new_account.save_account()
        test_account = Account ("Test","jamezzz")
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)

   
    def test_find_account_by_username(self):
        '''
        test to check if we can find an account by username and display information
        '''

        self.new_account.save_account()
        test_account = Account ("muthoni","muthonzz27") # new account
        test_account.save_account()

        found_account = Account.find_by_username("muthoni")


    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''
        self.new_account.save_account()
        test_account = Account("Test","jjjjjjjdd") # new account
        test_account.save_account()

        account_exists = Account.account_exist("Test")

        self.assertFalse(account_exists)


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the account class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_credential = Credential ("jada","jaydee","otiesh") #create account object

    def tearDown(self):
        """
        tearDown method that does the clean-up after each test has run
        """ 
        Credential.credential_list = []

    def test_save_credential(self):
        """
        test to check if the credential object is saved on credential list
        """
        self.new_credential.save_credential() #save account
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        """
        To check if we can save multiple objects into list
        """
        self.new_credential.save_credential()
        test_credential = Credential ("Twitter","muthoni","muthonzzz")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    
    def test_delete_credential(self):
            '''
            test_delete_contact to test if we can remove credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential ("Twitter","muthoni","muthonzzz") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)


    def test_find_credential_by_acc_name(self):
        '''
        test to check if we can find a credential by account name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential ("Twitter","muthoni","muthonzzz") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_acc_name("Twitter")

        self.assertEqual(found_credential.pword,test_credential.pword)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential ("Twitter","muthoni","muthonzzz") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Twitter")

        self.assertTrue(credential_exists)

    def test_display_all_credential(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.credential_display(),Credential.credential_list)

        # def test_copy_login_name(self):
    #     '''
    #     Test to confirm that we are copying the login name from a found credential
    #     '''

    #     self.new_credential.save_credential()
    #     credential.copy_login_name("Twitter")
    #     self.assertEqual(self.new_credential.login_name,pyperclip.paste())
    
if __name__ =='__main__':
    unittest.main()