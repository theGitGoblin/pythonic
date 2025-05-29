# How do i turn this into a excel sheet?

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
pay = []

def wantsCalc(a):
    wants = float(a) * .2

    return  wants

def needsCalc(b):
    needs = float(b) * .3

    return needs

def debtCalc(c):
    debt =  float(c) * .5
    return debt


print("Welcome to the debt collector! In this program we will seperate the amount of money you make and allocate it to the places you deem fit!")

debtT = float(input("How much debt do you currently have?: "))

for x in months:
    payment = float(input("How much did you get paid this month? (in dollar amount): "))
    pay += [payment]
    print("With the amount you were paid you have " + "$" + str(wantsCalc(payment))+ " for wants, " + "$" + str(debtCalc(payment)) + " for paying off your credit cards, " + " and $" + str(needsCalc(payment)) + " for anything you need for the month of " + x + ".")
    debtT -= debtCalc(payment)
    if debtT <= 0:
        print("That's it! You're done and the month you will finish paying on is: " + x + ".")



print("And that concludes the calculation for the Debt Collector!")
