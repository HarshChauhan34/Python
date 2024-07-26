#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *

n=int(input("Enter Number of Rows : "))
row=1
temp=n
while row<=n:
    col1=1
    while col1<=temp:
        print(" ",end='')
        col1+=1
    col2=1
    while col2<=row:
        print("* ",end='')
        col2+=1
    row+=1
    temp-=1
    print("")