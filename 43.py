fact=int(input("Enter factber as you want factorial : "))
num=fact
temp=fact-1


for i in range(fact,1,-1):
    fact=fact*temp
    temp-=1

print(f"{num}! = {fact}")

# fact=fact*temp #60
# temp-=1 #2
# fact=fact*temp #120
# temp-=1 #1
# fact=fact*temp #120