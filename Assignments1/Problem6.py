#6.	Create three lists, each of which can hold 3 values:
#the first list should contain 3 names
#the second list should contain the ages of the people with the names above
#the third list should contain the email addresses
#Using the following construct, enter values into the three lists:
#for counter in range(0,3):
#Now print out each of the lists.


names=[]
ages=[]
emails=[]
for counter in range(3):
        names.append(raw_input("Enter name"))
        ages.append(raw_input("Enter age"))
        emails.append(raw_input("Enter email"))
print names
print ages
print emails