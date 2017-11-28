a=raw_input("Enter an alphabet")
if ((a>="a")or(a>="A"))and((a<="z")or(a<="Z")):
    if ((a=="a")or(a=="e")or(a=="i")or(a=="o")or(a=="u")or(a=="A")or(a=="E")or(a=="I")or(a=="O")or(a=="U")):
        print "It's a vowel"
    else:
        print "It's a consonant"
else:
    print "Please enter an alphabet"
