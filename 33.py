income=int(input("Enter your monthly income "))
y_income=12*income
rate=0

if(y_income>0 and y_income<300000):
    rate=5
elif(y_income>=300000 and y_income<500000):    
    rate=10
elif(y_income>=500000 and y_income<800000):
    rate=20
elif(y_income>=800000):    
    rate=30
else:
    rate=0


tax=(y_income*rate)/100
total=y_income-tax


if(rate==0):
    print("Invalide Input ")
else:
    print(f"Final Yearly Income : {total}")

