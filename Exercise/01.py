class student:
    
    def __init__(self):
        self.name = input("Enter the name of the student : ")
        self.std = int(input("Enter the standard of the student : "))
        self.age = int(input("Enter the age of the student : "))
        
    def learn(self):
        print("Student can learn")
        
    def write(self):
        print("Student can write")
        
        
class teacher(student):
    
    def __init__(self):
        self.Name = input("Enter the name of the teacher : ")
        self.Age = int(input("Enter the age of the teacher : "))
        
    def teach(self):
        print("Teacher can teach")
        
        
class principal(student):
    
    def __init__(self):
        self.name = input("Enter the name of the principal : ")
        self.age = input("Enter the age of the principal : ")
        
    def manage(self):
        print("Principal can manage")
        
s1=principal()

s1.manage()
s1.write()