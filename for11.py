
k=5
for i in range(6): 
    for j1 in range(k):
        print(" ",end='')
    for j2 in range(i):
        if(j2==0 or i==5 or i==j2+1):
            print(f"* ",end='')
        else:
            print("  ",end='')
    print("")
    k-=1
    
    
#     *
#    * *
#   *   *
#  *     *
# * * * * *