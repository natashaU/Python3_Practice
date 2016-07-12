# Exercise 4
# Modify find so that it has a third parameter, the index in word
# where it should start looking.

# def find(word, letter):
#    index = 0
#    while index < len(word):
#        if word[index] == letter:
#            return index
#        index = index + 1
#    return -1

# Original. DPB: I've put a space after each comma, following Python standard
# style:

def find(word, letter, num):
    index = num
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# DPB: Here's an idea to make the program slightly more efficient. First, use
# "index" as an argument directly, rather than "num". Second, set a default
# argument of 0 on "index" — so that if the user doesn't supply a value, 0 is
# used without fuss.

def find_01(word, letter, index=0):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

