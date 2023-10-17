from transaction.transaction import *
from account.account import *

# adding my own comments to help my understanding of the program


# extending account class
class savingsaccount(account):
    """The SavingsAccount class has methods to manage the balance
        and interest rate of a savings account

     Args:
        account (account): class that includes methods to manage the balance
    """      
      
    def __init__(self, balance, interestRate):
        """_summary_

        Args:
           :ivar __balance: balance of this savingsaccount
           :ivar __interestRate: interest rate of this savingsaccount 
        """        
        super().__init__(balance)
        self.__interestRate = interestRate
    
<<<<<<< HEAD
    def setInterestRate(self, interestRate: float):
        """Set the interest rate attribute of the current object  

        Args:
            interestRate (float): New Interest rate of the object
        """        
=======

    
    def setInterestRate(self, interestRate: float):        
>>>>>>> b054dfd9c4e3953a7eacf1acffaa354cca887427
        self.__interestRate = interestRate
    

    def getInterestRate(self):
        """Gets the interest rate attribute of the object

        Returns:
            float: Return the interest rate of the object
        """
        return self.__interestRate
    
    def getInterest(self):
<<<<<<< HEAD
        """Get the interest rate of the object 

        Returns:
            float: returns the current interest rate multiplied by the
        """        
        return self._balance * self.__interestRate
=======
        return self.getBalance() * self.__interestRate
>>>>>>> b054dfd9c4e3953a7eacf1acffaa354cca887427
    
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