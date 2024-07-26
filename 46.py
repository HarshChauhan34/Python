number=int(input("Enter number of students : "))
print("")
data=[]

def get_studentdata(number):
    
    for i in range(number):
        print(f"---Enter information of student {i+1}---")
        name=input("Enter Name : ")
        age=int(input("Enter Age : "))
        contact_number=int(input("Enter Mobile Number : "))
        
        data.append(name)
        data.append(age)
        data.append(contact_number)
        print("")
        


def display_data(data):
    lenth=len(data)
    n=1
    for i in range(0,lenth,3):
        print(f"---Detail of Student {n}---")
        print(f"Name : {data[i]}")
        print(f"Age : {data[i+1]}")
        print(f"Mobile Number : {data[i+2]}")
        n+=1
        print("")
    
get_studentdata(number)

display_data(data)