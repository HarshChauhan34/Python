'''
    * * * * *
    
  * * * * * * *
  
* * * * * * * * *

  * * * * * * *
  
    * * * * *
'''

print("")
i=5
k=4
while i<=9:
    j1=1
    while j1<=k:
        print(" ",end='')
        j1+=1
    j2=1
    while (j2<=i):
        if (i%2==1):
            print("* ",end='')
        j2+=1
    print("")
    i+=1
    k-=1
print("")

i=1
k=7
i2=2
while i<=4:
    j1=1
    while j1<=i2:
        if(i2<9):
            print(" ",end='')
        j1+=1
    j2=1
    while j2<=k:
        if (i%2==1 and i<=3):
            print("* ",end='')
        j2+=1
    print("")
    i+=1
    k-=1
    i2+=1