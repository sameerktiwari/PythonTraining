from AccountException import AccountException
from Transaction import Transaction
class AccountOperations:
    accounts=[]

    def getAccount(self,accno):
        for ac in self.accounts:
            if(ac.accountNumber==accno):
                return ac
        return None

    def createAccount(self,account):
        for ac in self.accounts:
            if(ac.accountNumber==account.accountNumber):
                raise Exception("Account number already exists")
        self.accounts.append(account)

    def depositAmount(self,accno,amount):
        for ac in self.accounts:
            if(ac.accountNumber==accno):
                ac.setBalance(ac.getBalance()+amount)
                transaction=Transaction()
                transaction.setAccountNumber(accno)
                transaction.setBeneAcNo(accno)
                transaction.setAmount(amount)
                ac.addTransaction(transaction)
                return ac
        return None

    def withdrawAmount(self,accno,amount):
        for ac in self.accounts:
            if(ac.accountNumber==accno):
                if(ac.getBalance()<amount):
                    raise AccountException("Insufficient Balance")
                else:
                    ac.setBalance(ac.getBalance() - amount)
                    transaction = Transaction()
                    transaction.setAccountNumber(accno)
                    transaction.setBeneAcNo(accno)
                    transaction.setAmount(0-amount)
                    ac.addTransaction(transaction)
                    return ac
        return None

    def fundTransfer(self,srcacno,desacno,amount):
        for ac in self.accounts:
            if (ac.accountNumber == srcacno):
                for ac2 in self.accounts:
                    if(ac2.accountNumber == desacno):
                        self.depositAmount(desacno,amount)
                        self.withdrawAmount(srcacno,amount)
                        transaction = Transaction()
                        transaction.setAccountNumber(srcacno)
                        transaction.setBeneAcNo(desacno)
                        transaction.setAmount(amount)
                        ac.addTransaction(transaction)
                        return ""
                raise AccountException("Invalid receiver Account number")
            raise AccountException("Invalid receiver Account number")