# Exercise 3
# A string slice can take a third index that specifies the “step size”;
# that is, the number of spaces between successive characters. A step
# size of 2 means every other character; 3 means every third, etc.
# >>> fruit = 'banana'
# >>> fruit[0:5:2]
# 'bnn'
# A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
# Use this idiom to write a one-line version of is_palindrome from Exercise 3.

def is_palidrome(stringHere):
    if stringHere[::-1] == stringHere:
        print(True)
    else:
        print(False)

# DPB: There's a way this can be condensed, and some people consider this to be
# an important design principle. Instead of printing an explicit True or False
# based on the True or False value of the conditional predicate, we just report
# the value of the predicate directly:

def is_palidrome(stringHere):
    print(stringHere[::-1] == stringHere)


