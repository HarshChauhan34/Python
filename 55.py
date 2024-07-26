def Fact(num):
    
    if (num>1):
        
        fact=num*Fact(num-1)
        
        return fact
    else:
        
        return 1
    
Number = int(input("Enter number you want factorial : "))

Factorial = Fact(Number)

print(f"{Number}! = {Factorial}")