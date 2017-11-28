#5.	Write a script to print out the first 20 Fibonacci numbers.
# You can use the internet to find the definition of the
# Fibonacci sequence if you need to.

num1=0
num2=1
num=0
for num3 in range(20):
    num=num1+num2
    print num1
    num1 = num2
    num2=num
