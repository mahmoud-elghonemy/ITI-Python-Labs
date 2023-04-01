import re   
name=input("Enter your name\n")
while True:
    if isinstance(name,str) and len(name)!=0:
         email=input("Enter your Email\n")
         regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
         while True:
            if re.search(regex,email):
                print(f"your name:{name} , your email :{email}")
                break
            else:    
                 print("please enter vaild email")
                 email=input("Enter your Email\n")
                 regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
         break

    else:
         print("please enter vaild name")
         name=input("Enter your name\n")   