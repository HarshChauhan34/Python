a=int(input("Enter 1st side of Triangle : "))
b=int(input("Enter 2ndt side of Triangle : "))
c=int(input("Enter 3rd side of Triangle : "))

if (a==b==c):
    print("Your Triangle is Equilateral !!!")
elif (a==b or b==c or c==a):
    print("Your Triangle is Isosceles !!!")
elif (a!=b or b!=c or c!=a):
    print("Your Triangle is Scalene !!!")
else:
    print("Invalid Input !!!")