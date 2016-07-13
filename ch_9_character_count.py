# 9.2  Exercises

# Download file "words.txt" here:  http://greenteapress.com/thinkpython2/code/words.txt
# Exercise 1   Write a program that reads words.txt and prints only the words with more than 20 characters
# (not counting whitespace).


def character_count():
    fin = open("words.txt")
    for line in fin:
        words = line.strip()
        if len(words) > 19:
            print(words)

# DPB: A safer way to open a file — safer because it prevents the file from
# locking if the program crashes for some reason — is to use a "context
# manager" in the form of the "with" keyword:

def character_count_02():
    with open("words.txt", 'r') as f:
        for line in f:
            words = line.strip('\n')
            if len(words) > 19:
                print(words)

# DPB: If the program crashes, "with" will automatically close the file. Note
# that I've passed '\n' explicitly to strip.
