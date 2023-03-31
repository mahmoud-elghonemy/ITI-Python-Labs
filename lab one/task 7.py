num=input('enter your number\n')

if num.isnumeric():
    num=int(num)
    for i in range(0,num):
        for j in range(num-i,1,-1):
        
                print(" ",end=" ")
        for k in range(0,i+1):
            print("*",end=' ')
        print("\n")
else:
    print("please enter number only ")