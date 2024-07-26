
k=5
for i in range(6): 
    for j1 in range(i):
        print(" ",end='')
    for j2 in range(k):
        if(i==0 or j2==0 or k-1==j2):
            print("* ",end='')
        else:
            print("  ",end='')
    print("")
    k-=1
    
# * * * * * 
#  *     *
#   *   *
#    * *
#     *