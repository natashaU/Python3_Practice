# Chapter 8 Exercises

#8.3

# As an exercise, write a function that takes a string as an argument and
# displays the letters backward, one per line.

def stringBackwards(stringHere):
    i = len(stringHere) - 1
    while i >= 0:
        letter = stringHere[i]
        print(letter)
        i = i - 1

# To test function: stringBackwards("Natasha")



# In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings
# are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
# This loop outputs these names in order:

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
#     print(letter + suffix)

# The output is:
# Jack
# Kack
# Lack
 #Mack
# Nack
# Oack
# Pack
# Qack
# Of course, that’s not quite right because “Ouack” and “Quack” are misspelled.
# As an exercise, modify the program to fix this error.


def ducklings(stringHere):
    prefixes = 'JKLMNOPQ'
    for i in range(len(prefixes)):
        if i < 5 or i == 6:
            print(prefixes[i] + suffix)
        else:
            print(prefixes[i] + "u" + suffix)

# To test function:
# suffix = 'ack'
# ducklings(suffix)

    # An alternative way to do it:
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

# Fizz Buzz
for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
         print("FizzBuzz")
    elif num % 3 == 0:
         print("Fizz")
    elif num % 5 == 0:
         print("Buzz")
    else:
         print(num)


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

def find(word,letter,num):
    index = num
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


# Exercise 5
# Encapsulate this code in a function named count, and generalize it so that
# it accepts the string and the letter as arguments.

# word = 'banana'
# count = 0
# for letter in word:
#    if letter == 'a':
#        count = count + 1
# print(count)

def count(letterHere, word):
    count = 0
    for letter in word:
        if letter == letterHere:
            count = count + 1
    print(count)

# to check: count("a", "natasha")

# Exercise 6
# Rewrite this function so that instead of traversing the string, it uses
# the three-parameter version of find from the previous section.

def count(letterHere,word,num):
    count = 0
    for letter in word:
        i = num
        if letter == letterHere:
            count = count + 1
    print(count)

# to check: count("a", "natasha", 2)

# Exercise 7
# There is a string method called count that is similar to the function in
# the previous exercise. Read the documentation of this method and write
# an invocation that counts the number of as in 'banana'.

"banana".count("an")

# 8.11  Debugging

# When you use indices to traverse the values in a sequence, it is
# tricky to get the beginning and end of the traversal right.
# Here is a function that is supposed to compare two words and return True
# if one of the words is the reverse of the other, but it contains two errors.
# Fix them.

# def is_reverse(word1, word2):
#    if len(word1) != len(word2):
#        return False
#    i = 0
#    j = len(word2)

#    while j > 0:
#        if word1[i] != word2[j]:
#            return False
#        i = i+1
#        j = j-1

#    return True

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j >= 0:
        if word1[1] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

is_reverse("pots", "stop")

# 8.13 Exercises

# Exercise 2
# There is a string method called count that is similar to the function in Section 8.7.
# Read the documentation of this method and write an invocation that counts
# the number of a’s in 'banana'.

"banana".count("a")

# or the "longer" way:

def countLetters(word, yourLetter):
    count = 0
    for letter in word:
        if letter == yourLetter:
            count = count + 1
    print(count)

# to check: countLetters("banana", "a")

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

# to check: is_palidrome("natasha")

# Exercise 5
# A Caesar cypher is a weak form of encryption that involves “rotating” each
# letter by a fixed number of places. To rotate a letter means to shift it
# through the alphabet, wrapping around to the beginning if necessary,
# so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.

# Write a function called rotate_word that takes a string and an integer
#  as parameters, and returns a new string that contains the letters from
#  the original string rotated by the given amount.

# You might want to use the built-in function ord and chr
#  But beware: the numeric codes for upper case letters are different.

def rotate_word(word, num):
    returnValue = ""
    for letter in word:
        if letter.isupper():
            letter = letter.lower()
        letterToNum = ord(letter) + num
        rotatedLetter = chr(letterToNum)
        returnValue += rotatedLetter
    print(returnValue)

rotate_word("cheer", 7)
