try:
    file=open("d:\\sametiwa\problem13.txt",'a+')
    str = input("Enter the data you want to put in a file and end it with 'END'\n")
    while(1):
        if (str == "END"):
            break
        file.write(str)
        str=input()
    file.seek(0)
    print(file.read())
except IOError:
    file.close()
    print("Problem in writing or reading data from file")