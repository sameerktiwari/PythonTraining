from AccountOperations import AccountOperations
from Account import Account
accountOps=AccountOperations()
while(1):
    choice=input("Enter your choice\n1. Create Account\n2. Deposit Amount\n3. Withdraw Amount\n4. Fund Transfer\n5. View Account details\n6. Exit\n")
    if(choice=="1"):
        account=Account()
        try:
            acNo=int(input("Enter Account number\n"))
        except ValueError:
            raise Exception("Enter valid account number")
        acName = input("Enter AccountHolder name\n")
        try:
            acBalance = int(input("Enter starting balance\n"))
        except ValueError:
            raise Exception("Enter valid amount")
        account.setAccountNumber(acNo)
        account.setAccountName(acName)
        account.setBalance(acBalance)
        accountOps.createAccount(account)
    elif(choice=="2"):
        try:
            acNo = int(input("Enter Account number\n"))
        except ValueError:
            raise Exception("Enter valid account number")
        try:
            amount = int(input("Enter amount\n"))
        except ValueError:
            raise Exception("Enter valid amount")
        accountOps.depositAmount(acNo,amount)
    elif (choice == "3"):
        try:
            acNo = int(input("Enter Account number\n"))
        except ValueError:
            raise Exception("Enter valid account number")
        try:
            amount = int(input("Enter amount\n"))
        except ValueError:
            raise Exception("Enter valid amount")
        accountOps.withdrawAmount(acNo,amount)
    elif (choice == "4"):
        try:
            srcacNo = int(input("Enter your Account number\n"))
        except ValueError:
            raise Exception("Enter valid account number")
        try:
            desacNo = input("Enter Beneficiary Account number\n")
        except ValueError:
            raise Exception("Enter valid account number")
        try:
            amount = int(input("Enter amount\n"))
        except ValueError:
            raise Exception("Enter valid amount")
        accountOps.withdrawAmount(acNo,amount)
        accountOps.fundTransfer(srcacNo,desacNo,amount)
    elif (choice == "5"):
        acNo =int(input("Enter your Account number\n"))
        acc=accountOps.getAccount(acNo)
        print(acc)
    elif (choice == "6"):
        break;


