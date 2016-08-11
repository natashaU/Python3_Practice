""" Exercise 12
Two words “interlock” if taking alternating letters from each forms a new word.
For example, “shoe” and “cold” interlock to form “schooled”.

Solution: http://thinkpython2.com/code/interlock.py.
Credit: This exercise is inspired by an example at http://puzzlers.org.

Write a program that finds all pairs of words that interlock.
Hint: don’t enumerate all pairs!
 """

import bisect
from ch10ex10 import listWords2
import pprint

# From ch10Ex10
""" def listWords2():
    fin = open("words.txt")
    t = []
    for line in fin:
        words = line.strip()
        t += [words]
    return t """

def in_bisect(word_list, word):
    y = bisect.bisect_left(word_list, word)
    if y == len(word_list):
        return False

    return word_list[y] == word


def interlock(word_list, word):

    first = word[::2]
    second = word[1::2]
    return in_bisect(word_list, first) and in_bisect(word_list, second)


def interlock_search():
    if __name__ == '__main__':
        list1 = listWords2()
    interlocked_words = []
    for word in list1:
        if interlock(list1, word):
            interlocked_words += [word + ": " + word[::2] + " and " + word[1::2]]
    pprint.pprint(interlocked_words)

interlock_search()
