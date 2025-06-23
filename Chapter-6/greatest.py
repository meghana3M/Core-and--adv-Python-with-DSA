a = int(input("enter the number1"))
b = int(input("enter the number2"))
c = int(input("enter the number3"))
d = int(input("enter the number4"))
if(a>b and a > c and a > d):
    print("a is greater")
elif(b>a and b > c and b > d):
    print("b is greater")
elif(c>a and c>b and c>d):
    print("c is greater")
else :
    print("d is greater")
