from math import floor
"""
YOU MUST HAVE A SORTED LIST TO GET A BINARYSEARCH

You must move the Left and Right depending on how high the number is,
when this happens you cleave how much is to be done.
Log(n) due to cutting things in half
or
1/2 size * number of times
"""

def binarysearch(myList, t):
    L = 0
    R = len(myList) - 1
    m = floor((L + R) / 2)
    while L <= R:
        if myList[m] < t:
            L = m + 1
        elif myList[m] > t:
            R = m - 1
        else:
            return m
    return -1

print(binarysearch([100, 200 ,205 , 300 ,315, 498, 500], 315))
