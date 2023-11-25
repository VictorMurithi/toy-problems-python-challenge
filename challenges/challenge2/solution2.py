# write a function thats takes 3 integers as arguments and returns true if 
# two arguments of the three integers are positive numbers and false otherwise

def two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

print(two_positive(2, 4, -3)) 