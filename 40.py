# write a program to findout compound interest of given amount, rate & year 
amount = int(input("Enter amount :"))
rate = int(input("Enter rate : "))
year = int(input("Enter year :"))
count = 0
interest = 0
original_amount = amount
while count<year:
    interest = (amount * rate * 1) / 100
    amount= amount + interest 
    count = count + 1

print(amount - original_amount)
