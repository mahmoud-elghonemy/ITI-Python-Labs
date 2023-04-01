def reverseStr(sentance=""):
    if isinstance(sentance,str) and len(sentance) != 0:
       return sentance[::-1]
    else:
        return "you must enter one string only in parameter"

print(reverseStr())