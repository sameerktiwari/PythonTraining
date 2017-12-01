class Account:
    accountNumber=0
    accountName=""
    balance=0

    def getAccountNumber(self):
        return self.accountNumber

    def setAccountNumber(self,accountNumber):
        self.accountNumber=accountNumber

    def getAccountName(self):
        return self.accountName

    def setAccountName(self,accountName):
        self.accountName=accountName

    def getBalance(self):
        return self.balance

    def setBalance(self,balance):
        self.balance=balance

    def __repr__(self):
        print("Account no: ",self.accountNumber,"AccountHolder Name: ",self.accountName,"Balance: ",self.balance)
        return ""