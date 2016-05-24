# Exercise 3, Chapter 6
# Write a function called is_palindrome that takes a string argument
# and returns True if it is a palindrome and False otherwise.
# Remember that you can use the built-in function len to check the length
# of a string.

def first(word):
    return (word[0])

def last(word):
    return (word[-1])

def middle(word):
    return (word[1:-1])


def is_palidrome(stringhere):
    if not isinstance(stringhere, str):
        return none
    else:
        middleLetters = middle(stringhere)
        lastLetter = last(stringhere)
        firstLetter = first(stringhere)
        backwards = lastLetter + middleLetters + firstLetter
        if backwards == stringhere:
            print(True)
        else:
            print(False)

is_palidrome("noon")
