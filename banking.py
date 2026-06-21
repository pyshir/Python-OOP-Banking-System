from abc import ABC, abstractmethod
import sys

class Account(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        if type(balance) in (int, float) and balance >= 0:
            self._balance = balance
        else:
            self._balance = 0
            
    def show_balance(self):
        return self._balance
    
    def _valid_amount(self, amount):
        return type(amount) in (int, float) and amount > 0

    
    def deposit(self, amount):
        if self._valid_amount(amount):
            self._balance += amount
            return True

        return False

    
    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingAccount(Account):
    def __init__(self, account_number, owner, balance=0):
        super().__init__(account_number, owner, balance)

    def withdraw(self, amount):
        if self._valid_amount(amount) and self._balance >= amount:
            self._balance -= amount
            return True
        return False
    
class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance=0):
        super().__init__(account_number, owner, balance)

    def withdraw(self, amount):
        over_draft = 500
        if self._valid_amount(amount) and self._balance + over_draft >= amount:
            self._balance -= amount
            return True
        return False


if __name__ == '__main__':
    saving_account = SavingAccount(123456, 'jahid')
    current_account = CurrentAccount(123456, 'jahid')

    while True:
        operation = input('1.Show Balance\n2.Deposit\n3.Withdraw\n4.Exit\n=')        

        if operation == '1':
            account_type = input('1.Saving\n2.Current\n=')
            if account_type == '1':
                print(saving_account.show_balance())
            elif account_type == '2':
                print(current_account.show_balance())
            else:
                print("Invalid account type")

        elif operation == '2':
            amount = float(input('Enter amount\n='))
            account_type = input('1.Saving\n2.Current\n=')
            if account_type == '1':
                deposit = saving_account.deposit(amount)
            elif account_type == '2':
                deposit = current_account.deposit(amount)
            else:
                deposit = False
                print("Invalid account type")

            if deposit == True:
                print('Deposit Successful!')
            else:
                print('Invalid amount')
        
        elif operation == '3':
            amount = float(input('Enter amount\n='))
            account_type = input('1.Saving\n2.Current\n=')
            if account_type == '1':
                withdraw = saving_account.withdraw(amount)
            elif account_type == '2':
                withdraw = current_account.withdraw(amount)
            else:
                withdraw = False
                print("Invalid account type")

            if withdraw == True:
                print('Withdraw Successful!')
            else:
                print('Invalid amount')
        
        elif operation == '4':
            sys.exit()

        else:
            print('Please select a valid operation')
            continue