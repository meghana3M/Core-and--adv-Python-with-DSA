# factorial using for loop
# 5  === 5*4*3*2*1
n = int(input("enter a number"))
product = 1
for i in range(1,n+1):
    product = product*i
print(product)