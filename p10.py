row=1
temp=5
while row<=5:
    col1=1
    while col1<=temp:
        print(" ",end='')
        col1+=1
    col2=1
    while col2<=row:
        if (row==5 or col2==1 or row==col2):
            print("* ",end="")
        else:
            print("  ",end="")
        col2+=1
    row+=1
    temp-=1
    print("")
    
#      * 
#     * *
#    *   *
#   *     *
#  * * * * *