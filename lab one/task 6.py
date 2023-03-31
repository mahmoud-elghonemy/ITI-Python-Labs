num= input('Enter a number: ')

if num.isnumeric():
    num= int(num)
    myList=[]
    num2=1
    for i in range(1,num+1):
        newls=[]
        num2=i
        for j in range(1,i+1):
            newls.append(num2)
            num2=num2+i

        myList.append(newls)
        

    print(myList)

else:
   print("please enter number only ")
