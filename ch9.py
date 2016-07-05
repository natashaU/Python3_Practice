# 9.2  Exercises

# Download file "words.txt" here:  http://greenteapress.com/thinkpython2/code/words.txt
# Exercise 1   Write a program that reads words.txt and prints only the words with more than 20 characters
# (not counting whitespace).


def characterCount():
    fin = open("words.txt")
    for line in fin:
        words = line.strip()
        if len(words) > 19:
            print(words)


# Exercise 2
# Write a function called has_no_e that returns True if the given word doesn’t have
# the letter “e” in it.

# Modify your program from the previous section to print only the words that have
# no “e” and compute the percentage of the words in the list that have no “e”.

def has_no_e_one():
    fin = open('words.txt')
    for line in fin:
        if line.find("e") == -1:
            return("True")


def has_no_e():
    fin = open("words.txt")
    number_of_words = 0
    count = 0
    for line in fin:
        number_of_words = number_of_words + 1
        words = line.strip()
        if words.find("e") == -1:
            print(words)
            count = count + 1
    percent_of_words = (count/number_of_words) * 100
    print("Percent:", percent_of_words)



# Exercise 3
# Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.

def avoids(word, stringHere):
    for letters in word:
        if stringHere in word:
            return False
    return True




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




# Exercise 4
# Write a function named uses_only that takes a word and a string of letters, and that returns True if the
# word contains only letters in the list. Can you make a sentence using only the letters acefhlo?
# Other than “Hoe alfalfa?”

def uses_only(word,string_of_letters):
    for letter in word:
        if letter not in string_of_letters:
            return False
    return True



# Exercise 5
# Write a function named uses_all that takes a word and a string of required letters,
# and that returns True if the word uses all the required letters at least once.
# How many words are there that use all the vowels aeiou? How about aeiouy?

def uses_all(word, required_letters):
    for letter in required_letters:
        if letter not in word:
            return False
    return True

# Exercise 6
# Write a function called is_abecedarian that returns True if the letters in a word appear in
# alphabetical order (double letters are ok).
# How many abecedarian words are there?

def is_abcedarian(word):
    i = 0
    while i < len(word) - 1:
        if word[i] > word[i + 1]:
            return False
        i = i + 1
    return True


# 9.7  Exercises

# Exercise 7
# This question is based on a Puzzler that was broadcast on the radio program Car Talk
# (http://www.cartalk.com/content/puzzlers):
# Give me a word with three consecutive double letters.
# I’ll give you a couple of words that almost qualify, but don’t.
# For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except
# for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i.
# If you could take out those i’s it would work. But there is a word that has
# three consecutive pairs of letters and to the best of my knowledge this may be
#  the only word. Of course there are probably 500 more but I can only think of one.
#  What is the word?
# Write a program to find it.


def is_double(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count = count + 1
        i = i + 2
    if count == 3:
        return True


def find_double_words():
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if is_double(word):
            print(word)



# Exercise 8   Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):

# “I was driving on the highway the other day and I happened to notice my odometer.
# Like most odometers, it shows six digits, in whole miles only. So, if my car had
# 300,000 miles, for example, I’d see 3-0-0-0-0-0.
# “Now, what I saw that day was very interesting. I noticed that the last 4 digits
# were palindromic; that is, they read the same forward as backward.
# For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.
# “One mile later, the last 5 numbers were palindromic.
# For example, it could have read 3-6-5-4-5-6. One mile after that, the middle
# 4 out of 6 numbers were palindromic. And you ready for this? One mile later,
# all 6 were palindromic!

# “The question is, what was on the odometer when I first looked?”

# Write a Python program that tests all the six-digit numbers and prints any
# numbers that satisfy these requirements

# Version 1
def is_palidrome(num, start):
    numString = str(num)
    i = start
    j = len(numString) - 1
    count = 0
    while i <= j:
        if numString[i] == numString[j]:
             print(numString)
        else:
             return False
        i = i + 1
        j = j - 1

# My answer is different than the book's answer: http://greenteapress.com/thinkpython2/code/cartalk2.py
# In my version, the user can pick where they would like to start testing the number
# to see if it is a palidrome so it works for other numbers besides the ones that
# are given to us in this example.


# Version 2

def is_palidrome_ex(num):
    numString = str(num)
    if numString[::-1] == numString:
        return True

def car_talk_paldromes(num):
    numString = str(num)
    if is_palidrome_ex(num):
        print(num)
    new_num = numString[2::]
    if is_palidrome_ex(new_num):
        print(num)
    new_num = numString[1:6]
    if is_palidrome_ex(new_num):
        print(num)
    new_num = numString[1:5:]
    if is_palidrome_ex(new_num):
        print(num)

# My second version tests to see if the specific examples given to us are palidromes
# It only works for numbers that are similar to the example.

# Exercise 9
# Here’s another Car Talk Puzzler you can solve with a search (http://www.cartalk.com/content/puzzlers):
#  “Recently I had a visit with my mom and we realized that the two digits that
# make up my age when reversed resulted in her age. For example, if she’s 73,
# I’m 37. We wondered how often this has happened over the years but we got
# sidetracked with other topics and we never came up with an answer.
# “When I got home I figured out that the digits of our ages have been reversible
# six times so far. I also figured out that if we’re lucky it would happen again
# in a few years, and if we’re really lucky it would happen one more time after that.
# In other words, it would have happened 8 times over all. So the question is, how old am I now?”
# Write a Python program that searches for solutions to this Puzzler. Hint:
# you might find the string method zfill useful.


def is_palidrome(motherAge, daughterAge):
    motherAge = str(motherAge)
    daughterAge = str(daughterAge)
    difference = len(motherAge) - len(daughterAge)
    daughterAge = daughterAge.zfill(len(motherAge))
    motherAge = motherAge[::-1]
    if motherAge == daughterAge:
        return True
    else:
        return False




# for ageAtBirth in range (1, 50):


# count = 0
#for motherAge in range (20, 120):
#    daughterAge = motherAge - ageAtBirth
#    if is_palidrome(motherAge, daughterAge):
#        count = count + 1
#    print(motherAge, daughterAge)
# print(count)

# this is the wrong answer!! 
count = 0
previousDiffAge = 0
for motherAge in range (15, 120):
    for daughterAge in range(1, 100):
        diffAge = motherAge - daughterAge
        if is_palidrome(motherAge, daughterAge) and diffAge == previousDiffAge:
            count = count + 1
            if count == 6:
                print(motherAge)
                print(daugtherAge)
    previousDiffAge = diffAge
