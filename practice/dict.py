calculator = dict()


num1 = float(input("This is the first number in the operation: "))
num2 = float(input("This is the second number in the operation: "))

calculator['exponent'] = num1 ** num2
calculator['addition'] = num1 + num2
calculator['subtraction'] = num1 - num2
calculator['multiplication'] = num1 * num2
calculator['division'] = num1 / num2

calculatorOptions = str(input("What operation would you like to do?\n (You must choose between division,exponent,multiplication,division,addition, or subraction): "))

print(calculator[calculatorOptions])

for i in calculator:
    print(calculator[i])
