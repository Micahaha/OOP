from transaction.transaction import *
from account.account import *

# adding my own comments to help my understanding of the program


# extending account class
class savingsaccount(account):
    def __init__(self, balance, interestRate):
        super().__init__(balance)
        self.__interestRate = interestRate
    

    
    def setInterestRate(self, interestRate: float):        
        self.__interestRate = interestRate

    def getInterestRate(self):
        return self.__interestRate
    
    def getInterest(self):
        return self.getBalance() * self.__interestRate
    
    # overriding credit method from account class to be multipled by interest rate

    def credit(self, amount: float):
        return super().credit(amount * self.__interestRate)
    
    # overriding __str__ to return new string with interest rate
    
    def __str__(self):
        return f"Savings account balance= {self._balance} InterestRate={self.__interestRate}"

    def __eq__(self, other):
        """Compare the two objects to see if they're the same

        Args:
            other (savingsaccount): The savings account object to compare to

        Returns:
            boolean: Returns true if the objects are the same 
        """            
        if other is not None:
                # check if other is an account type
                if isinstance(other, savingsaccount):
                    # check if other's balance is equal to the balance and the interest rate are the same
                    # of the calling object
                    return (other.getBalance() == self.getBalance()) and (other.getInterestRate() == self.getInterestRate())
                
        return False