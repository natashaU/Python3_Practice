# As an exercise, write a function that takes a string as an argument and
# displays the letters backward, one per line.

# DPB: Use snake-case rather than camel-case for all function/variable names
# (but use camel-case for class-names).

# Original, with snake-case change made, and shortened argument name:

def string_backwards(s):
    i = len(s) - 1
    while i >= 0:
        letter = s[i]
        print(letter)
        i = i - 1

# DPB: This is fine.

# DPB: Ideas:

# 1. You can iterate through a string, backwards or forwards, just as though it were 
# a list. Actually, strings are implemented as arrays of a kind in Python.

# 2. Here are two ways to reverse a string: the first is actually a "generator"
# in Python 3. Ask me if you have any trouble understanding that.

def reverse_string_01(s):
    for c in s[::-1]:
        print(c)

def reverse_string_02(s):
    for c in reversed(s):
        print(c)

# 3. Given the kind of output you are planning to produce, in this case you can
# actually create a one-liner pretty easily, using the str.join method, as
# below.

def reverse_string_03(s):
    print('\n'.join(s[::-1]))

def reverse_string_04(s):
    print('\n'.join(reversed(s)))
