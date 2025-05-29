userInput = int(input("What number would you like to see? "))

sum = 1

for i in range(1, userInput):
    sum *= i
    print(sum)
