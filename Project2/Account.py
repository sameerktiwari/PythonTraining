class Account:
    accountNumber=0
    accountName=""
    balance=0
    transactions=[]

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

    def addTransaction(self,transaction):
        self.transactions.append(transaction)

    def getTransactions(self):
        return self.transactions

    def __repr__(self):
        print("Account no: ",self.accountNumber,"AccountHolder Name: ",self.accountName,"Balance: ",self.balance)
        return ""

    def __init__(self):
        self.accountNumber = 0
        self.accountName = ""
        self.balance = 0
        self.transactions = []