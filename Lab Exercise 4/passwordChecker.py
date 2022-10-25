#Password Checker

import re
#input your password and match it with re
password = input("Type your password... length should be at least 8 digit long for a valid password: \n")

if(len(password)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@!#$%&\'*+-.^_`|~:]))',password))==True):
        print("The password is strong")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([@!#$%&\'*+-.^_`|~:]*))',password))==True):
        print("The password is weak")
    else:
        print("You have entered an invalid password.")
 
    #counter score 
    lowerscore = 0
    upperscore = 0
    specialscore = 0
    numberscore = 0

    #Check the password for specific characters  
    lowercase = False
    uppercase = False
    specialsymbol = False
    number = False

    for c in password:  
        if c in "abcdefghijklmnopqrstuvwxyz":  
            lowercase = True
            lowerscore += 1
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  
            uppercase = True
            upperscore += 1
        if c in "@!#$%&\'*+-.^_`|~:":  
            specialsymbol = True
            specialscore += 1
        if c in "0123456789":  
            number = True
            numberscore += 1
    
    if lowercase == True:
        print("Your password contains lowercase characters (a-z): " + str(lowerscore))
    if uppercase == True:
        print("Your password contains uppercase characters (A-Z): " + str(upperscore))
    if specialsymbol == True:
        print("Your password contains at least one of these characters (@!#$%&\'*+-.^_`|~:): " + str(specialscore))
    if number == True:
        print("Your password contains at least one of the numbers (0-9): " + str(numberscore))


