from transaction.transaction import *
from sys import exit

class account(transaction):
    def __init__(self, *args):
        """Constructs a savings account with a specified balance and interest rate.

        :ivar __balance: balance of this savingsaccount
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
        return self._balance
    
    def isEmpty(self):
        return self._balance == 0
    
    def credit(self, amount: float):
        try:
            if(amount < 0.0):
                raise ValueError("Credit amount is less than zero.")
        except ValueError as e:
            exit(e)
        finally:
            self._balance += amount

    def debit(self, amount: float):
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
        return f"account balance= {self._balance} public= {self.public}"
    
    def __eq__(self, other):
        if other is not None:
            # chec kfi other is an account type
            if isinstance(other, account):
                # check if other's balance is equal to the balance
                # of the calling object
                if other._balance == self._balance:
                    return True
            
        return False
    
    @staticmethod
    def sum(account1, account2):
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
