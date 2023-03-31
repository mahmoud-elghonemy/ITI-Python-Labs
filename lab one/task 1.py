str=input('enter your string\n')
str=str.lower()
count=0
for ch in str:
   if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
       count+=1

print(f'Number of vowels is {count}')