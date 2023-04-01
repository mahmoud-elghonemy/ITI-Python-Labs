def generateArr(length,start):
    if isinstance(length,int) and isinstance(start,int):
        arr=list(range(start,start+length+1,1))
        print(arr)
    else:
        print("please parameters are integer only")


generateArr(5,1)