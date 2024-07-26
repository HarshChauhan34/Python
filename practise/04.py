numbers = []

for i in range(5):
    num = int(input(f"ENter Number {i+1} : "))
    numbers.append(num)


# print(numbers)

max = numbers[0]

for i in numbers:
    if i > max:
        max = i
    
print(max)