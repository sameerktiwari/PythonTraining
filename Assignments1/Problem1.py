#1.	Write a Python program that prints all the numbers from 0 to 9 except 3,6 and 9

for num in range(10):
    if (num%3)!=0:
        print num