import intro

# Get user input that determies the loop range.

userInput = input ("Enter Year  (e.g 2021 ) :  ")

# check user input 
try:
    val = int(userInput)

    # input value should be evenet
    if val % 2 == 0 :
        if val < 0 :
            print ("Have you ever seen negative year ?? Do you write -2021\n")
        elif val == 0 : # just having fun hahaha
            print ("Calendar was not invented at this time. People were really stupid at this year\n")   
        else: 
            if val % 4 == 0 :
                if val % 100 == 0 :
                    if val % 400 == 0 :
                         print ("This is a leap year\n")
                    else:
                        print ("This is not a leap year\n")
                else:
                    print ("This is a leap year\n")     
            else:
                    print ("This is not a leap year\n")    
    else :
        print ( "Do you know what a year is ? Google it\n") 
        
except ValueError: # for all non interger input display error
    print("Why are you not reading the instructions properly. ENTER YEAR : )\n") 