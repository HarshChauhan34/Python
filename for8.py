
k=5
for i in range(6): 
    for j1 in range(i):
        print(" ",end='')
    for j2 in range(k):
        print("* ",end='')
    print("")
    k-=1
    
#     *
#    * *
#   * * *
#  * * * *
# * * * * *