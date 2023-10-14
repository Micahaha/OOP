from transaction.transaction import *
from sys import exit

class account(transaction):
    """The Account class includes methods to manage the balance
    of bank account.   

    Args:
        transaction (transaction): abstract class that defines methods
        that may be implemented by an account class
    """    
    def __init__(self, *args):
        """Constructs an account with a specified balance if args length
        is 1, else constructs an account with a balance of 0.

        Raises:
            ValueError: indicates args[0] is less than 0.
        """        
        if(len(args) == 1):
            try:
                if(args[0] < 0.0):
                    raise ValueError("Balance is less than zero.")
            except ValueError as e:
                exit(e)
            finally:
                self._balance = float(args[0]) # this is a private instance variable 
                self.public = 'public'         # this is a public instance variable 
                self._protected = 'protected'  # this is a protected instance variable 
        else:   
            self._balance = 0.0
            self.public = 'public' # this is a public instance variable 
            self._protected = 'protected'  # this is a protected instance variable  

    def __privateMethod(self):
        print('Private Method')
    
    def _protectedMethod(self):
        print('Protected Method')

    def publicMethod(self):
        print('Public Method')
   
    def getBalance(self):
        """Returns the balance of the calling account.

        Returns:
            float: the balance 
        """        

        return self._balance
    
    def isEmpty(self):
        """Checks if the balance for the calling account is zero.

        Returns:
            Boolean: True if the balance for the calling account is zero,
            else False. 
        """        
        return self._balance == 0
    
    def credit(self, amount: float):
        """Increases the balance of the calling account by the specified amount.

        Args:
            amount (float): the amount to increase the balance by.

        Raises:
            ValueError: indicates the specified amount is less than zero. 
        """        
        try:
            if(amount < 0.0):
                raise ValueError("Credit amount is less than zero.")
        except ValueError as e:
            exit(e)
        finally:
            self._balance += amount

    def debit(self, amount: float):
        """Decreases the balance of the calling account by the specified amount.

        Args:
            amount (float): the amount to decrease the balance by

        Raises:
            ValueError: Indicates the specified amount is less than 0
            ValueError: Indicates the specified amount is geater than the balance 
            of the calling acount
        """

        try:  
            if amount < 0.0:
                raise ValueError('Debit amount is less than zero. ')
            if amount > self._balance:
                raise ValueError('Debit amount is greater than the balance.')
        except ValueError as e:
            exit(e)
        else:
            self._balance = self._balance - amount
    
    def __str__(self):
        """returns string when calling object directly that indicates the balance and 
        class visibility

        Returns:
            string: string implementation of class
        """                             
        return f"account balance= {self._balance} public= {self.public}"
    
    def __eq__(self, other):
        """checks if classes are equal to one another           

        Args:
            other (_type_): Other object 

        Returns:
            boolean: returns true or false if objectrs are the same
        """        

        if other is not None:
            # check if other is an account type
            if isinstance(other, account):
                # check if other's balance is equal to the balance
                # of the calling object
                if other._balance == self._balance:
                    return True
            
        return False
    
    @staticmethod
    def sum(account1, account2):
        """Static method that adds the sum of both accounts 

        Args:
            account1 (account): account to retrieve balance from      
            account2 (account): second account to retrieve balance from

        Returns:
            float: sum of both balances from account objects
        """        
        if(account1 is None or account2 is None):
            return 0.0
        # if parameter type is not account: return 0.0 
        elif (not isinstance(account1, account) or not isinstance(account2, account)):
            return 0.0
        else:
            return account1._balance + account2._balance
        
    # static methods can be called without making an instance of the class 

    @staticmethod
    def transfer(a, amount: float):
        """Transfers a specified amount to account object a

        Args:
            a (account): Account object to transfer an amount to
            amount (float): amount to transfer into balance

        Raises:
            ValueError: If the amount is less than zero a value error will be returned
            ValueError: If object a is none a ValueError will return that it is nothing.
            ValueError: Check the type of a and check if it is of type account
            ValueError: The balance is too large to withdraw from the account

        Returns:
            account: returns a new account object   
        """        
        try:
            if (amount < 0.0):
                raise ValueError("Debit amount is less than zero")
            elif (a is None):
                # if no account in parameter: 
                raise ValueError("Account is None.")
                # if parameter is not account type: 
            elif (not isinstance(a, account)):
                raise ValueError("a is not an account type")
                # cannot use greater amount then what is in the balance: 
            elif (amount > a.getBalance()):
                raise ValueError("Debit amount is greater than the balance in the specified account.")
        except ValueError as e:
            exit(e)
        else:
            a.debit(amount)
            newAccount = account(amount)
            return newAccount
