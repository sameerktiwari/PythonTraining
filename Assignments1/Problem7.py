#7.	Write a function that takes named parameters and returns the
# parameters as a Dictionary of parameter name -> value

dict={1:"Value1",2:"Value2",3:"Value3"}

def getValue(str):
    return dict.get(str)

key=input("Enter a key")
print getValue(key)
