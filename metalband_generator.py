
# A program that generates random metal band names

""" Earlier today, in the Recurse Center Slack Room, one of my mentors jokingly suggested
a project idea for a "cool metal band generator." I thought that was a fun idea,
so I made one. Whether the names generated are cool or not is up for debate. Some examples:
asses vile
enfeeble revocation
dominie dying fetus
overexercise nile
brain drill meathook
"""

import random

def make_list(stringHere):
    fin = open(stringHere)
    t = []
    for line in fin:
        words = line.strip()
        t+=[words]
    fin.close()
    return t




def metal_bands(words_generated=1):
    for phrases in range(words_generated):
        metal_word = random.choice(make_list("metalbands.txt"))
        question = input("Do you want to choose a word? Type YES or NO: ")
        if question.upper() == "YES":
            user_word = input("Type a random word: ")
            print(user_word + " " + metal_word.lower())
        else:
            random_word = random.choice(make_list("words.txt"))
            print(random_word + " " + metal_word.lower())

metal_bands()

# fin.close()
