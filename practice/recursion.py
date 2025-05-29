def factorials(n):
    z = 1
    if n > z:
        z = n * factorials(n - 1)
    return z

print(factorials(5))

def rpower ( b , n ) :
    z=1
    if n > 0:
        z= b * rpower ( b , n - 1)
        return z

print ( rpower ( 2 , 5 ) )
