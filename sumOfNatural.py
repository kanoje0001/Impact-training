def squareOfNatural(n):
    sum=0
    for i in range( 1, n+1):
        sum = sum + (i*i)
    return sum
n = int(input("Enter the number :- ")) 
sq = squareOfNatural(n)
print(sq)   