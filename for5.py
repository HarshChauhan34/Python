k=5
for i in range(6):
    for j in range(k):
        if(j==0 or i==0 or k-1==j):
            print(f"* ",end='')
        else:
            print("  ",end='')
    print("")
    k-=1
    
    
# * * * * * 
# *     *
# *   *
# * *
# *