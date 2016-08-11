""" Exercise 9, Chapter 10
Write a function that reads the file words.txt and builds a list with one element per word.
Write two versions of this function, one using the append method and the other
using the idiom t = t + [x]. Which one takes longer to run? Why?
Solution: http://thinkpython2.com/code/wordlist.py. """

from __future__ import print_function, division

import time


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
