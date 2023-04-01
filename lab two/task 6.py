lnum=[]
while True: 
    num=input("enter number\n")
    if num.isnumeric() and num!="done":
        num=int(num)
        lnum.append(num)
    elif num=="done":
         print(f"total is {sum(lnum)} ,count is {len(lnum)} ,average is {sum(lnum)/len(lnum)}")
         break
    else:
        print("please enter numbers only")
        
