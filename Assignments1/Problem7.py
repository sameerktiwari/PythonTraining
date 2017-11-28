dict={1:"Value1",2:"Value2",3:"Value3"}

def getValue(str):
    return dict.get(str)

key=input("Enter a key")
print getValue(key)
