
# A program that generates random metal band names

""" Earlier today, in the Recurse Center Slack Room, one of my mentors jokingly suggested
a project idea for a "cool metal band generator." I thought that was a fun idea,
so I made one. Whether the names generated are cool or not is up for debate. Some examples:
asses vile
enfeeble revocation
dominie dying fetus
overexercise nile
"""

import random

def make_list(stringHere):
    fin = open(stringHere)
    t = []
    for line in fin:
        words = line.strip()
        t+=[words]
    return t

def metal_bands():
    word_list = make_list("words.txt")
    first_word = random.choice(word_list)
    metal_words = make_list("metalbands.txt")
    print(first_word + " " + random.choice(metal_words).lower())

metal_bands()
