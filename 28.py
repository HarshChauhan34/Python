m_income=int(input("Monthly Income : "))

y_income=m_income*12    

# print(f"Your Yearly Income is :{y_income}")

if (y_income<300000):
    tax1=(y_income*5)/100
    t_income1=y_income-tax1
    print(f"Total Income : {t_income1}")
elif (y_income>=300000 and y_income<500000):
    tax2=(y_income*10)/100
    t_income2=y_income-tax2
    print(f"Total Income : {t_income2}")
elif (y_income>=500000 and y_income<800000):
    tax3=(y_income*20)/100
    t_income3=y_income-tax3
    print(f"Total Income : {t_income3}")    
elif (y_income>=800000):
    tax4=(y_income*30)/100
    t_income4=y_income-tax4
    print(f"Total Income : {t_income4}")
else:
    print("Invalid Input !")