i=1
k=5
while i<=5:
    j=1
    while j<=k:
        if (i==1 or j==1 or k==j):
            print("* ",end="")
        else:
            print("  ",end='')
        j+=1
    i+=1
    k-=1
    print("")
    
# * * * * * 
# *     *
# *   *
# * *
# *
