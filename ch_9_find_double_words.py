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

# DPB: This program prints just two words:

# masslessness
# masslessnesses

# which are not correct. We are looking for an uninterrupted run of three pairs
# of double letters. I happen to know that "bookkeeper" is one such word.

# I've revised your code and added comment-lines.

def is_double_02(word):
    i = 0
    count = 0
    while i < len(word) - 1: # Good; no pair can extend past word's end.
        if word[i] == word[i+1]:
            count = count + 1
            # If pair found, only then skip ahead two letters
            i += 2
            # Check count and return immediately if goal met, rather than reset.
            if count == 3:
                return True
        else:
            # If pair not found, skip ahead only one letter.
            i += 1
            # Reset count
            count = 0

def find_double_words_02():
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if is_double_02(word):
            print(word)

# Output:

# In [1]: import ch_9_find_double_words
# 
# In [2]: ch_9_find_double_words.is_double_02('bookkeeper')
# Out[2]: True
# 
# In [3]: ch_9_find_double_words.find_double_words_02()
# bookkeeper
# bookkeepers
# bookkeeping
# bookkeepings

