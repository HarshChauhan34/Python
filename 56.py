X=[]

x=int(input("Enter the Numbers of X : "))

for i in range(x):
    num=int(input(f"Enter number {i+1} : "))
    X.append(num)
    
# print(X)

Y=[]

y=int(input("Enter the Numbers of Y : "))

for i in range(y):
    num=int(input(f"Enter number {i+1} : "))
    Y.append(num)
    
# print(Y)

def Add(num):
    sum=0
    for i in num:
        sum+=i
    return sum

# Addition=Add(Y)
# print(Addition)