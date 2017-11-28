def fib(num):
    list=[]
    num1=0
    num2=1
    for num3 in range(num):
        num = num1 + num2
        print num1
        list.append(num1)
        num1 = num2
        num2 = num
    return list

nos=input("Enter how many numbers you want to print")
list=fib(nos)
