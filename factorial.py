# Factorial
def factorial():
    temp=1

    num=int(input("Enter number as you want factorial : "))

    while num>=1:
        temp=num*temp
        num-=1

    print(temp)