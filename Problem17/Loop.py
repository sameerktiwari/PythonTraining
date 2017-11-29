flag=0
for i in range(10):
    for j in range(10):
        print(i," ",j)
        if(j==2):
            continue
        if(j==3):
            break;
    i=-1        