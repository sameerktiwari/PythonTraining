from NumberException import NumberException
try:
    num=int(input("Enter a number\n"))
    if((num>10)or(num<0)):
        raise NumberException()
    sum=1
    for i in range(1,num+1):
        sum*=i
    print("Factorial of givenm number is ",sum)
except ValueError:
    print("Please enter a number")