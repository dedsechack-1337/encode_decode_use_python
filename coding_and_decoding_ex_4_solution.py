import random
import string
#dev by -Amit Roy
while(True):
    while True:
        inp = input("For Encode  Enter 1 & decode Enter 2 For Exit type 0 : ")
        if(inp not in [0,1,2,"0","1","2"]):
            print("enter  Number 0/1/2")
        else:
            inp = int(inp)
            break    



    if (inp==1):
        str = input("Enter Your Word to Encode: ")
        words = str.split(" ")
        output_words =[]
        for word in words:
            if len(word)>=3:
                str3random = ''.join(random.choices(string.ascii_lowercase,k=3))
                output = str3random+word[1:]+ word[0]+str3random

                

            else:
                output = word[::-1]
            output_words.append(output)

        print(" ".join(output_words))

    elif inp==2:
        str = input("Enter Your Word to Decode: ")
        words = str.split(" ")
        output_words =[]
        for word in words:
            if len(word)>=3:
                str3random = word[-4]+ word[3:-4]
                output = str3random
                

            else:
                output = word[::-1]

            output_words.append(output)

        print(" ".join(output_words))
    else:
        print("Thank u for using our decode/encode programe: - dev by Amit Roy")   
        break 



    
