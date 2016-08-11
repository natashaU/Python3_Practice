""" Chapter 10 short exercises, # 1 - #7 Exercises"""

from __future__ import print_function, division
import time # (for Ex. 9 exercises )

# Exercise 1
# Write a function called nested_sum that takes a list of lists of integers and
# adds up the elements from all of the nested lists. For example:

# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21

t = [[1, 2], [3], [4, 5, 6]]
def nested_sum(t):
    count = 0
    for nestedList in t:
        count += sum(nestedList)
    return count

# nested_sum(t)

""" Exercise 2
Write a function called cumsum that takes a list of numbers and returns the
cumulative sum; that is, a new list where the ith element is the sum of the
first i+1 elements from the original list. For example:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6] """

t = [1, 2, 3]
def cumsum(t):
    t2 = []
    count = 0
    for i in t:
        count += i
        t2.append(count)
    return t2

# cumsum(t)

"""Exercise 3
Write a function called middle that takes a list and returns a new list that
contains all but the first and last elements. For example:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3] """

t = [1, 2, 3, 4]

def middle(t):
    t2 = t[1:-1]
    return t2

# middle(t)

"""Exercise 4
Write a function called chop that takes a list, modifies it by removing the
first and last elements, and returns None. For example:

>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3] """

t = [1, 2, 3, 4]
def chop(t):
    t.pop(0)
    t.pop()

#chop(t)

""" Exercise 5   Write a function called is_sorted that takes a list as a parameter
and returns True if the list is sorted in ascending order and False otherwise.
For example:

>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False """

t = [1, 2, 3]

def is_sorted(t):
    return t == sorted(t)

#is_sorted(t)

""" Exercise 6
Two words are anagrams if you can rearrange the letters from one to spell the
other. Write a function called is_anagram that takes two strings and returns
True if they are anagrams. """

t = "cinema"
t2 = "iceman"
def is_anagram(firstString, secondString):
    return sorted(firstString) == sorted(secondString)

# is_anagram(t, t2)

""" Exercise 7
Write a function called has_duplicates that takes a list and returns True if
there is any element that appears more than once. It should not modify
the original list. """

def has_duplicates(listName):
    t = listName[:]
    t.sort()
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False

""" Exercise 8
This exercise pertains to the so-called Birthday Paradox, which you can read
about at http://en.wikipedia.org/wiki/Birthday_paradox.
If there are 23 students in your class, what are the chances that two of you
have the same birthday? You can estimate this probability by generating random
samples of 23 birthdays and checking for matches. Hint: you can generate random
birthdays with the randint function in the random module."""




def birthday_paradox(trial=1000):
    import random
    total = 0
    for trialNum in range(trial):
        bDayList = []
        for i in range(23):
            bDay = random.randint(0, 365)
            bDayList.append(bDay)
        bDayList.sort()
        sameDay = False
        for i in range(len(bDayList) - 1):
            if bDayList[i] == bDayList[i + 1]:
                sameDay = True
        if sameDay:
            total += 1
    prop = (total / trial) * 100
    print("The propability is ", prop, "percent" )


# birthday_paradox(50)

# I know I can seperate this into different functions to avoid bugs. The book has a different answer:
#http://greenteapress.com/thinkpython2/code/birthday.py


""" Exercise 9
Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. Which one takes longer to run? Why?
Solution: http://thinkpython2.com/code/wordlist.py. """

def listWords():
    fin = open("words.txt")
    t = []
    for line in fin:
        words = line.strip()
        t.append(words)
    return t

# listWords()

def listWords2():
    fin = open("words.txt")
    t = []
    for line in fin:
        words = line.strip()
        t += [words]
    return t

# listWords2()

def timeWords():
    startTime = time.time()
    listWords()
    endTime = time.time()
    totalTime = endTime - startTime

    startTime2 = time.time()
    listWords2()
    endTime2 = time.time()
    totalTime2 = endTime2 - startTime2

    if totalTime > totalTime2:
        print("The append method takes longer!")
    elif totalTime2 > totalTime:
        print("The t = t + [x] method takes longer!")
    else:
        print("I must have written this with a bug!")

timeWords()
