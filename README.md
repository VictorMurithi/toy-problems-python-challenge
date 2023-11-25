##         PYTHON CODING CHALLENGES 
## Description
Welcome to the Coding Challenges! This is a collection of Python challenges that cover a variety of topics. Each challenge comes with a description, examples, and a solution to help you enhance your coding skills.
## Project setup
To get started with this repository, follow these steps:
1. Clone the repository

git clone https://github.com/your-username/coding-challenges.git

cd coding-challenges

2. Set Up Virtual Environment (Optional)

python -m venv venv

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies

pip install -r requirements.txt

## Challenge 1: Converting 12-hour time to 24-hour time
## Overview
Converting a 12-hour time format (e.g., "8:30 am" or "8:30 pm") to a 24-hour format (e.g., "0830" or "2030") is a common programming task. The challenge involves implementing a function that performs this conversion and returns a formatted four-digit string representing the time in the 24-hour format.

## Instructions
Your task is to define a function that takes an hour (1 to 12), a minute (0 to 59), and a period ("am" or "pm") as input. The function should validate the input and return a four-digit string representing the time in the 24-hour format.

## Examples
For "8:30 am", the function should return "0830".
For "2:45 pm", the function should return "1445".
For "12:00 pm", the function should return "1200".
For "12:15 am", the function should return "0015".

## Notes
Noon is represented as 12:00 pm.
Midnight is represented as 12:00 am.
The 12-hour clock has no 0 hour.
Times just after midnight (e.g., 12:15 am) are denoted as, for example, 0015 in the 24-hour clock.

## Challenge 2: Two numbers are positive.
## Overview
This challenge involves creating a function that takes three integers, a, b, and c, as arguments and returns True if exactly two of the three integers are positive numbers (greater than zero), and False otherwise.

## Instructions
Your function should handle cases where all, none, or only one of the integers are positive. It should return True only if exactly two of the three integers are positive.

## Examples
For (2, 4, -3), the function should return True.
For (-4, 6, 8), the function should return True.
For (4, -6, 9), the function should return True.
For (-4, 6, 0), the function should return False.
For (4, 6, 10), the function should return False.
For (-14, -3, -4), the function should return False.

## Challenge 3: Consonant value
## Overview
This challenge involves creating a function that, given a lowercase string with alphabetic characters only and no spaces, returns the highest value of consonant substrings. Consonants are defined as any letters of the alphabet except "aeiou". Each consonant is assigned a value from a = 1 to z = 26.

## Instructions
Implement a function that calculates the value of consonant substrings and returns the highest value among them.

## Examples
For the word "zodiacs", solve("zodiacs") should return 26.
For the word "strength", solve("strength") should return 57.
## Notes
Vowels ("aeiou") are excluded from consonant substrings.
The values assigned to consonants are a = 1, b = 2, c = 3, ..., z = 26.

## Author & License
## Author
Victor Murithi

## License
This repository is licensed under the MIT License. Feel free to use the code for learning and personal projects. If you contribute to this repository, please ensure to follow the license terms.

Feel free to explore and solve these challenges. Happy coding!