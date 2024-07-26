#Given number is prime or not

num=int(input("ENter Number : "))

div = 2

while div<=num-1:
    if num%div==0:
        print("Given Number is not Prime Number !!!")
        break
    else:
        div+=1

if div==num:
    print("Given Number is Prime Number !!!")
