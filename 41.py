amout=int(input("Enter Amout : "))
rate=int(input("Enter Rate : "))
year=int(input("Enter Year : "))

o_amout=amout
count=0

while count<year:
    interest=(amout*rate*1)/100
    amout=amout+interest
    count+=1



print(amout-o_amout)