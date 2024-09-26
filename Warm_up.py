# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = "abracadabra"
# a. Retrieve the 5th character.
print(magic[4:5])
# b. Retrieve the second to last character.
print(magic[9:10])
# c. Find the first occurrence of the letter 'c'.
substring = magic.find("c")
print(substring)

# Advanced Slicing:
# Given the string 
alphabet = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:26:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the 
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
substring = quote.find("John")
print(substring)
substring = quote.find("Kennedy")
print(substring)
print(quote[83:98])

# Manipulating Words:
info = "Python is fun. Fun is good. Good is subjective."
a = "Python"
b = "is"
c = ".fun"
d = "Fun"
f = ".good"
g = "Good"
h = ".subjective"
# a. Extract the word 'subjective' without knowing its exact position.
substring = info.find("subjective")
print(substring)
substring = info[36:47]
print(substring)
# b. Extract every third word.
print(info[0:47:3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(a[::-1], b[::-1], c[::-1], d[::-1], b[::-1], f[::-1], g[::-1], b[::-1], h[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
star_wars = "MAY THE FORCE BE WITH YOU."
print(star_wars.lower())

# String Joining and Splitting:
# Given the list 
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
joined_list = " ".join(motto)
print(joined_list)
# b. Now, split the string at every occurrence of the letter 'a'.
split_sentence = joined_list.split()
print(split_sentence)

# Replacing Words:
# Modify the 
sentence = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
new_sentence = sentence.replace("busy","distracted").replace("plan","mistakes")
print(new_sentence)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repetition = "Iteration" * 7
print(repetition)

# Word Search:
# Check if the word "moonlight" appears in the 
quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
substring = quote2.find("moonlight")
print(substring)

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word:
# b. Count the number of times the letter 'i' appears in the same word/phrase.
phrase = "Supercalifragilisticexpialidocious"
substring = phrase.find("us")
print(substring)