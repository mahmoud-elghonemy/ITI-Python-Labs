def divisble(num):
    if isinstance(num,int):
        if num%3==0 and num%5==0:
            return "FizzBuzz"
        elif num%3==0:
            return "Fizz"
        elif num%5==0:
            return "buzz"
        else:
            return None
    else:
        print("please enter number only in paramter function")

print(divisble(5))
print(divisble(3))
print(divisble(15))