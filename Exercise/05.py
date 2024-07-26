import random
ch=1
while(ch!=0):
    Numbers=[1,2,3,4,5,6]

    Num=random.choice(Numbers)

    # print(Num)

    if(Num==1):
        print("-----")
        print("| . |")
        print("-----")
    elif(Num==2):
        print("-----")
        print("| . |")
        print("| . |")
        print("-----")
    elif(Num==3):
        print("-------")
        print("| . . |")
        print("|  .  |")
        print("-------")
    elif(Num==4):
        print("-------")
        print("| . . |")
        print("| . . |")
        print("-------")    
    elif(Num==5):
        print("-------")
        print("| . . |")
        print("|  .  |")
        print("| . . |")
        print("-------") 
    else:
        print("-------")
        print("| . . |")
        print("| . . |")
        print("| . . |")
        print("-------") 
        
    ch=int(input("Press 0 if exit... "))