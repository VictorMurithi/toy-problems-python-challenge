# given a lowercase string that has alphabetic characters only and no spaces ,return  the highest
# value of a constant substring.

#values = a=1 , b=2 , c=3 , d=4 , e=5 ,upt0 z 
#consonants are all characters except aeiou 

def check_highest_consonant_value(string):
    # Define the vowels and create a dictionary to map consonants to their values
    vowels = "aeiou"
    consonant_values = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}

    # Function to calculate the value of a consonant substring
    def calculate_consonant_value(substring):
        return sum(consonant_values[char] for char in substring)

    # Initialize variables for maximum and current values
    max_value = 0
    current_substring = ""

    # Iterate through each character in the input string
    for char in string:
        # Check if the character is not a vowel (i.e., it's a consonant)
        if char not in vowels:
            # Append the consonant to the current substring
            current_substring += char
        else:
            # If a vowel is encountered, update the maximum value and reset the current substring
            max_value = max(max_value, calculate_consonant_value(current_substring))
            current_substring = ""

    # Check the last substring if the word ends with a consonant
    max_value = max(max_value, calculate_consonant_value(current_substring))

    # Return the overall maximum value of consonant substrings
    return max_value

# Example
result = check_highest_consonant_value("zodiacs")
print(result)
