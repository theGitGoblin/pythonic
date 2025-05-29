
jabArray = []


agreement = True
while agreement:
    x = int(input("What is the next number in list?: "))
    jabArray.append(x)
    y = str(input("Are you done? "))
    if y == 'Y' or y == 'y':
        agreement = False



max = 0
for i in jabArray:
    if i > max:
        max = i

print(max)
