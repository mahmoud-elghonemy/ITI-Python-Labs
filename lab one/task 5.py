str=input('enter your string\n')
str=str.lower()



# print([pos for pos, char in enumerate(str) if char == 'i'])


for pos, char in enumerate(str):
    if char == 'i':
        print(pos)
