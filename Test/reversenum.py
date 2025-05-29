myInt = str(input("What number would you like me to reverse?: "))

lenInt = len(str(myInt))
print(lenInt)
newInt = []

while lenInt > 0:
    newInt.append(myInt[lenInt - 1])
    lenInt -=1

print(newInt)
