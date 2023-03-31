str=input('enter your string\n')
str=str.lower()

str=str.replace('a','')
str=str.replace('e','')
str=str.replace('i','')
str=str.replace('o','')
str=str.replace('u','')

print(f'string after remove all vowels is {str}')