import intro

# Get user input that determies the loop range.

userInput = input ("Enter Even number ?  ")

# check user input 
try:
    val = int(userInput)

    # check input value should be even
    if val % 2 == 0 :
        if val < 0 : # check for negative number
            print ("Number can not be negative. I am not converting that to positive and iterating ")
        elif val == 0 : # just having fun hahaha
            print ("What !!!! seriously 0 . Go back to school mate")   
        else: 
            for x in range(1,val + 1) : # used val + 1 since i started with index 1
                print(str(x) + ". Hello World" )
    else :
        print ( "Do you know what a even number is ? God!! ") 
    
    print ("\n")
except ValueError: # for all non interger input display error
    print("Why are you not reading the instructions properly. ENTER EVEN NUMBER : )") 
   