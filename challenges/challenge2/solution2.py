# write a function thats takes 3 integers as arguments and returns true if 
# two arguments of the three integers are positive numbers and false otherwise

def two_positive(a, b, c):
    # Initialize a counter to keep track of the number of positive integers
    positive_count = 0

    # Check if 'a' is positive, and increment the counter if true
    if a > 0:
        positive_count += 1

    # Check if 'b' is positive, and increment the counter if true
    if b > 0:
        positive_count += 1

    # Check if 'c' is positive, and increment the counter if true
    if c > 0:
        positive_count += 1

    # Return True if exactly two out of the three numbers are positive, and False otherwise
    return positive_count == 2

# Examples
print(two_positive(2, 4, -3))
