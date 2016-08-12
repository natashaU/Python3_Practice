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

# DPB: I don't see how "num" is being used in the program. I'm not even sure
# how it's supposed to be used — the assignment is confusing.
