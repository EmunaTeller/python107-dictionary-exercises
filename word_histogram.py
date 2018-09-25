# Write a word_histogram program that asks the user for a 
# sentence as its input, and prints a dictionary containing the 
# tally of how many times each word in the alphabet was used in 
# the text.

user_string = input("Please enter a sentence: ")

# iterate over user_string, adding chars to temp_string until
# space is found. when space is found, add temp_string to new
# list, creating list of words in user_string
word_list = []
temp_string = ""
for char in user_string:
    if char == " ":
        word_list.append(temp_string)
        temp_string = ""
    else:
        temp_string = temp_string + char

# create dictionary of words as keys and count as value
# iterate over list of words, if word is not in dictionary
# add word as key and give it count of 1. if word is in 
# dictionary, increment count

word_dict = {}
for word in word_list:
    if word.lower() not in word_dict:
        word_dict[word.lower()] = 1
    else:
        word_dict[word.lower()] += 1

for word in word_dict:
    print("%s: %s" % (word, word_dict[word]))
