import intro

from datetime import datetime
 
#Prompt user for date input 
userInputDate1 = str(input('Enter date(yyyy-mm-dd): '))



try:
    # convert to datettime
    userInputDate1 = datetime.strptime(userInputDate1, '%Y-%m-%d')

    #Prompt user for date input
    userInputDate2 = str(input('Enter date(yyyy-mm-dd): '))

    try:
        # Convert to datetime type
        userInputDate2 = datetime.strptime(userInputDate2, "%Y-%m-%d")

        # get date difference
        dateDifference = abs ( (userInputDate1 - userInputDate2).days )

        print ( "\nDate difference is ",str(dateDifference) + " day(s)" )
    except ValueError:
        print ("Invalid date format")    
except ValueError:
    print ("Invalid date format")




