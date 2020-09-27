#(Find the smallest n such that n2 12,000) Use a while loop to find the smallest
#integer n such that n2 is greater than 12,000.

n = 2
nSquared = n ** 2
while nSquared < 12_000:
    n += 1
    nSquared = n ** 2

print("The smallest integer n such as n^2 > 12,000 is " + str(n))
