'''
Here are my monthly subscriptions

Crunchyroll : $12
Spotify:  $6
Amazon Prime $8
App Store Sub???: $9


Credit Card Debt:
    Apple:
        $1554

    Navy Federal: $3150


    Credit One:
        $500

    Discover:
        $1488

'''
navyFed = 3147.42
navyFedInterest = 1.18

Apple = 1554
AppleInterest = 1.2324

Discover = 1488
DiscoverInterest = (1486.47 + 47.00) / 1486.47

CreditOne = 500
CreditOneInterest = 60/500 + 1

numMonths = int(input("How many months are we talking about: "))

for month in range(1, numMonths + 1):
    temp_navyFed = navyFed
    navyFed *= navyFedInterest
    navyFed_interest = navyFed - temp_navyFed

    temp_Apple = Apple
    Apple *= AppleInterest
    Apple_interest = Apple - temp_Apple

    temp_Discover = Discover
    Discover *= DiscoverInterest
    Discover_interest = Discover - temp_Discover

    temp_CreditOne = CreditOne
    CreditOne *= (1 + CreditOneInterest)
    CreditOne_interest = CreditOne - temp_CreditOne

    print(f"Year {month}:")
    print(f"  NavyFed Interest: {navyFed_interest:.2f}, Total: {navyFed:.2f}")
    print(f"  Apple Interest: {Apple_interest:.2f}, Total: {Apple:.2f}")
    print(f"  Discover Interest: {Discover_interest:.2f}, Total: {Discover:.2f}")
    print(f"  CreditOne Interest: {CreditOne_interest:.2f}, Total: {CreditOne:.2f}")
    print("-")
