arr=[]
for i in range(1,5):
    el=input('enter your number from array\n')
    if el.isnumeric():
        el=int(el)
        arr.append(el)
    else:
        print("please enter number only")


arr.sort()

print(f"ascending sort is {arr}")

arr.sort(reverse = True)

print(f"descending sort is {arr}")


