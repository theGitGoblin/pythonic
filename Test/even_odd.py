def even_odd(x:int):
    if x % 2 == 0:
        return True
    else:
        return False

myNum = int(input("What is your number: "  ))

print(even_odd(myNum))
