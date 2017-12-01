from AccountException import AccountException

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
                return ac
        return None

    def withdrawAmount(self,accno,amount):
        for ac in self.accounts:
            if(ac.accountNumber==accno):
                if(ac.getBalance()<amount):
                    raise AccountException("Insufficient Balance")
                else:
                    ac.setBalance(ac.getBalance() + amount)
                    return ac
        return None

    def fundTransfer(self,srcacno,desacno,amount):
        for ac in self.accounts:
            if (ac.accountNumber == srcacno):
                for ac2 in self.accounts:
                    if(ac2.accountNumber == desacno):
                        self.depositAmount(desacno,amount)
                        self.withdrawAmount(srcacno,amount)
                        return ""
                raise AccountException("Invalid receiver Account number")
            raise AccountException("Invalid receiver Account number")