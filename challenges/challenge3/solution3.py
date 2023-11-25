# given a lowercase string that has alphabetic characters only and no spaces ,return  the highest
# value of a constant substring.

#values = a=1 , b=2 , c=3 , d=4 , e=5 ,upt0 z 
#consonants are all characters except aeiou 

def check_highest_consonant_value(string):
    lowercase_string = string.lower()
    max_value = 0
    current_value = 0

    for char in lowercase_string:
        # Check if the character is a consonant
        if char.isalpha() and char not in "aeiou":
            # Calculate the value of the consonant based on its position in the alphabet
            value = ord(char) - ord('a') + 1

            # Accumulate the value for the current substring
            current_value += value
        else:
            # If a non-consonant is encountered, update the maximum value and reset the current value
            max_value = max(max_value, current_value)
            current_value = 0

    # Update the maximum value for the last substring (if any)
    max_value = max(max_value, current_value)

    return max_value

# Example
input_string = "abczd"
result = check_highest_consonant_value(input_string)
print(result)
