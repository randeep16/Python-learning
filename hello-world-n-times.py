import intro

# Get user input that determies the loop range.
userInput = input ("How many time you want to print ?  ")

# check user input 
try:
    val = int(userInput)

    # input cannot be negative number
    if val < 0 :
        print (" Do not enter negative numbers\n")
    elif val == 0 : # just having fun hahaha
        print (" What !!!! seriously \n")    
    else: 
        # print the range
        for x in range(1,val + 1) : # used val + 1 since i started with index 1
            print(str(x) + ". Hello World " )

        print("\n")    
except ValueError: 
    # for all non interger input display error
    print("Invalid input. Starting Self Destruction ....\n") 
