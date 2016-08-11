""" Exercise 11
Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
 Solution: http://thinkpython2.com/code/reverse_pair.py. """

import bisect
from ch10ex10 import listWords2

if __name__ == '__main__':
    word_list = listWords2()
    print(word_list)

"""def listWords2():
    fin = open("words.txt")
    t = []
    for line in fin:
        words = line.strip()
        t += [words]
    return t


def in_bisect(word_list, word):
    y = bisect.bisect_left(word_list, word)
     if y == len(word_list):
        return False

    if word_list[y] == word:
        print(word)




def reverse_pair():
    list1 = listWords2()
    for firstword in list1:
        firstword = firstword[::-1]
        in_bisect(list1, firstword)

reverse_pair() """
