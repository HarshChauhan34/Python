# * 
# * *
# *   *
# *     *
# * * * * *

i=1
while i<=5:
    j=1
    while j<=i:
        if (i==5 or j==1 or i==j):
            print("* ",end="")
        else:
            print("  ",end="")
        j+=1
    i+=1
    print()