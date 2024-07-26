mark=int(input("Enter Marks : "))

if (mark>=85 and mark<=100):
    print("Your Grade is A")
elif (mark>=65 and mark<=84):
    print("Your Grade is B")
elif (mark>=45 and mark<=64):
    print("Your Grade is C")
elif (mark>=33 and mark<=44):
    print("Your Grade is D")
elif (mark>=0 and mark<33):
    print("Your Grade is F")
else:
    print("Invalid Marks")