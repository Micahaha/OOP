from transaction.transaction import *

class account(transaction):
    def __init__(self, *args):
        print(args)
        if(len(args) == 1):
            try:
                if(args[0] < 0.0):
                    raise ValueError("Balance is less than zero.")
            except ValueError as e:
                exit(e)
            finally:
                self._balance = float(args[0])
        else:
            self._balance = 0.0 