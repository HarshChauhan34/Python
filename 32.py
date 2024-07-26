num=int(input("Enter Integer Number : "))

if num>0:
    print("Your Number is Positive !!!")
    if num%2==0:
        print("Your Number is Even !!!")
    else:
        print("Your Number is Odd !!!")
elif num<0:
    print("Your Number is Negetive !!!")
else:
    print("Your Number is Zero !!!")