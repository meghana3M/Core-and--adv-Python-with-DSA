n = int(input("enter a number"))
for i in range(2,n):
    if(n%i)==0:
        print("false")
        break
else :
    print("true")