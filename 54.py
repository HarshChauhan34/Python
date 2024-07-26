def add(num):
    
    if (num>0):
        
        Add=num+add(num-1)
        
        return Add
    else:
        
        return 0
    
Number = int(input("Enter number you want addition : "))

Addition = add(Number)

print(f"Addition : {Addition}")