"""
        Figure out how to vailidate a password for a website
"""

newPassword = str(input("What do you want your password to be???: "))

correctPass = False
attemptedTries = 0

while correctPass == False:
    passwordAttempt = str(input("Please enter your password: "))
    if passwordAttempt == newPassword:
        print("Successful Attempt!!")
        correctPass = True
        break
    attemptedTries +=1
    print(f"Failed password attempt # {attemptedTries}")
    if attemptedTries == 3:
        print("You have tried too many times in order to enter your password, you have been locked out. :( ")
        break
