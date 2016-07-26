# Modify your program to prompt the user to enter a string of forbidden letters
# and then print the number of words that don’t contain any of them. Can you
# find a combination of 5 forbidden letters that excludes the smallest number of words?

def avoids_forbidden():
    user_input = input("Enter a string of forbidden letters!")
    fin = open("words.txt")
    count = 0
    for line in fin:
        words = line.strip()
        if user_input not in words:
            count = count + 1
    print(count)

# DPB: It seems to me that this increments the counter if the whole
# "user_input" string is not found, intact, in "words".

# Here's my attempt:

def avoids_forbidden_02():
    user_input = input("Enter a string of forbidden letters! ")
    fin = open("words.txt")
    count = 0
    for line in fin:
        words = line.strip()
        count += find_any_char(user_input, words)
    print(count)

def find_any_char(user_chars, word):
    """Return 1 if no char in user_chars found in word; 0 if any found"""
    for c in user_chars:
        if c in word:
            return 0
    return 1

# DPB: I've written a second function to do the work of actually checking —
# that second function can be tested separately, which makes the whole program
# more modular and easier to debug.

# Also, notice that I've added a space at the end of your input() argument —
# that makes the output look a litte better.
