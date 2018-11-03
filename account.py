import string
from random import choice

class Account:
    """

    Class is suppossed to generate new instance of accounts
    """

    account_list = [] #Empty account list

    def __init__(self,password,username):
        """
        __init__method that defines properties for our objects

        Args:
           password:new  account password
           username:new  account username
        """    

        self.password = password
        self.username = username

    def save_account(self):
        """
        save_account method saves objects into list
        """
        Account.account_list.append(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a account that matched that username.
        Args:
            username: username to search for
        Returns:
             account  that matched the username.
        '''

        for account in cls.account_list:
            if account.username == username:
                return account


    @classmethod
    def account_exist(cls,username):
            '''
            Method that checks if a account exists from the account list.
            Args:
                username: Username to search if it exists
            Returns :
                Boolean: True or false depending if the account exists
            '''
            for account in cls.account_list:
                if account.username == username:
                        return True

            return False    
    
class Credential:
    """
    Class that generates new instances of credential
    """

    credential_list = [] #Empty credential 

    def __init__(self,acc_name,login_name,pword):
        """
        __init__ method that defines properties for our objects

        Args:
            acc_name: New credential acc_name.
            login_name: New credential login_name.
            pword: New credential pword.
        """
       
        self.acc_name = acc_name
        self.login_name = login_name
        self.pword = pword

    def save_credential(self):
        """
        save_credential method saves objects into list
        """
        Credential.credential_list.append(self)

    

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_acc_name(cls,acc_name):
        '''
        Method that takes in a number and returns a credential that matches that account name.
        Args:
            acc_name: Account name to search for
        Returns :
            Credential of account that matches the account name.
        '''

        for credential in cls.credential_list:
            if credential.acc_name == acc_name:
                return credential

    @classmethod
    def credential_exist(cls,acc_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            acc_name: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.acc_name == acc_name:
                    return True

        return False
    
    @classmethod
    def credential_display(cls,):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
    
    # @classmethod
    # def copy_login_name(cls,acc_name):
    #     credential_found = credential.find_by_acc_name(acc_name)
    #     pyperclip.copy(credential_found.login_name)