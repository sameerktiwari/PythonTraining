class Transaction:
    accountNumber=0
    beneAcNo=0
    amount=0

    def getAccountNumber(self):
        return self.accountNumber

    def setAccountNumber(self,accountNumber):
        self.accountNumber=accountNumber

    def getBeneAcNo(self):
        return self.accountName

    def setBeneAcNo(self,beneAcNo):
        self.beneAcNo=beneAcNo

    def getAmount(self):
        return self.balance

    def setAmount(self,amount):
        self.amount=amount

    def __repr__(self):
        print("Account no: ",self.accountNumber,"Beneficiay Account no: ",self.beneAcNo,"Balance: ",self.amount)
        return ""