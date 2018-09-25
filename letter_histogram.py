# Write a letter_histogram program that asks the user for input, 
# and prints a dictionary containing the tally of how many times 
# each letter in the alphabet was used in the word. 

user_string = input("Please enter a word: ")

char_dict = {}

for char in user_string:
    char_dict[char] = 0

for char in user_string:
    char_dict[char] += 1

print(char_dict)