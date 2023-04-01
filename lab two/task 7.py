ll={'apple','banana','orange'} 
correctWord=ll.pop()
gessWord="-"*len(correctWord)
newWord=""
charNum=0
correctChars=""
lastTry=7
print(correctWord,gessWord)
i=0
while True:
    print("please gess characters of word")
    print(gessWord)
    askchar=input(f"please enter your gessing {charNum} char in round {i} ")
    if len(askchar)==1:
        if correctWord[charNum]==askchar:
            correctChars+=askchar
            _word="-"*(len(correctWord)-len(correctChars))
            newWord=correctChars+_word
            gessWord=newWord
            charNum+=1
        else:
            print("please try to gess correct character")
            i+=1

    else:
        i+=1

    if gessWord==correctWord:
        print(f"Bravo the word is {correctWord}")
        print("-------- yooou are wiiinnnnnnner :)--------")
        break
    elif i==lastTry:
        print("---- you are losser !! ------")
        break

    