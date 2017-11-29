try:
    f=open("testfile.txt",'r')
except IOError:
    print("File not found")