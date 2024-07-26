class person:
    def __init__(self):
        self.name=input("Enter Name : ")
        self.h_foot=int(input("Enter Height in foot : "))
        self.h_inch=int(input("Enter Height in inch : "))
        self.weight=float(input("Enter Weight : "))
        
    def foot_to_meter(self):
        f_to_m=(self.h_foot)/3.281
        print(f"Height in Meter of Foot of {self.name} : {f_to_m}")
        
    def inch_to_meter(self):
        i_to_m=(self.h_inch)/39.37
        print(f"Height in Meter of Inch of {self.name} : {i_to_m}")
        
    def get_height(self):
        f_to_m=(self.h_foot)/3.281
        i_to_m=(self.h_inch)/39.37
        t_height=f_to_m+i_to_m
        print(f"Height of {self.name}: {t_height} Meters")
            
    def get_bmi(self):
        f_to_m=(self.h_foot)/3.281
        i_to_m=(self.h_inch)/39.37
        t_height=f_to_m+i_to_m
        bmi=(self.weight)/(t_height**2)
        print(f"BMI of {self.name} : {bmi}")
        return bmi
        
    def get_weight(self):
        print(f"Weight of {self.name} : {self.weight} KG")
        
    def bmi_Categories(self):
        i=self.get_bmi()
        
        if(i<=18.5):
            print("Underweight")
        elif(i>18.5 and i<=24.9):
            print("Normal Weight")
        elif(i>=25 and i<=29.9):
            print("Overweight")
        elif(i>=30):
            print("Obesity")