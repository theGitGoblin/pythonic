"""
Imagine a "bubble" holding 2 values, as the values compare with each other they will swap
and continue this process until


this is a O(n^2) algorithm due to a secondary for loop

it guarantees that the last index that is subtracted will always be the largest number
"""

def bubblesort(a):
    n = len(a)
    for i in range(0,n):
        for j in range (0, n - i - 1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

    return a
print(bubblesort([2, 4, 56, 1,45,9,10]))
