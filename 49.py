nums=int(input("ENter numbers you want : "))

numbers=[]

for i in range(nums):
    num=int(input(f"ENter Number {i+1} : "))
    numbers.append(num)
    
print(numbers)


if(numbers[0]>numbers[1]):
    print()