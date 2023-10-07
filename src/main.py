from account.account import *

def main():
    # Create an account object named a1 that has a balance of $100.00
    a1 = account(100.0)
    a2 = account(0.00)
    # a1 = account(100.0, 200.0, 300.0, 400.0)
    # a1 = account(-100.0) a balance less than zero will result in our code raising a ValueError
    # print(a1.public) referencing a public instance variable will not result in an error
    # print(a1._balance) referencing a private instance variable will result in an error
    # print(a1._protected) referencing a protected instance variable will not result in an error 

    # a1.__privateMethod() referencing a private instance method will result in an error
    # a1._account__privateMethod()
    # a1._protectedMethod()  referencing a protected method will not result in an error
    a1.publicMethod() # referencing a public method will not result in an error 


    # display the balance of a1
    print("$%.2f" % a1.getBalance())

    # increase the balance of a1 by $50 
    a1.credit(50.0)

    # display the balance of a1
    print("$%.2f" % a1.getBalance())

    # decrease the balance of a1 by $75
    a1.debit(75.0)


    # display the balance of a1
    print('is a1 Empty? ', a1.isEmpty())

    # create a second object named a2 and initialize
    # its balance to zero
    a2 = account()

    # display the balance of a2
    print("$%.2f" % a2.getBalance())

    # increase the balance of a2 by $50
    a2.credit(150)
    
    # display the balance of a2
    print("$%.2f" % a2.getBalance())

    # decrease the balance of a2 by $75
    a2.debit(75)

    # display the balance of a2
    print("$%.2f" % a2.getBalance())

    # display if the balance of a2 is empty
    print('is a2 empty? ', a2.isEmpty())

    # display a string representation of a1 and a2
    print(f'new balance:',a1)
    print(f'new balance:',a2)

    # create an object named a3 that is equal to none 
    a3 = None

    # test if a1 is equal to a3
    print('is a1 equal to a3? ', a1.__eq__(a3))

    # create a string object named s1
    s1 = 'I love Python'

    # test if a1 is equal to s1
    print('Is a1 equal to a3?', a1.__eq__(s1))

    # test if a1 is equal to a2
    print('is a1 equal to a2? ', a1.__eq__(a2))

    # change the balance of a2
    a2.credit(75.0)

    # test if a1 is equal to a2
    print('is a1 equal to a2? ', a1.__eq__(a2))

    # display the sum of balances a1 and a2
    print("$%.2f" % account.sum(a1, a2))

    # display the sum of balances a1 and a3
    print("$%.2f" % account.sum(a1, a3))


if __name__ == "__main__":
    main()