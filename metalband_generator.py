"""
Earlier today, in the Recurse Center Slack Room, one of my mentors jokingly suggested
a project idea for a "cool metal band generator." I thought that was a fun idea,
so I made one. Whether the names generated are cool or not is up for debate.

Some examples:
* asses vile
* enfeeble revocation
* dominie dying fetus
* overexercise nile
* brain drill meathook

"""

import random

def make_list(filehere):
    with open(filehere) as infile:
        lines = infile.readlines()

        return [l.strip() for l in lines]



def metal_bands(names_generated=1):
    for _ in range(names_generated):
        metal_word = random.choice(make_list("metalbands.txt")).lower()

        question = input("Do you want to choose a word? Type YES/NO: ").upper()
        if question.upper() == "YES":
            user_word = input("Type a random word: ")
            print(user_word + " " + metal_word)
        else:
            random_word = random.choice(make_list("words.txt"))
            print(random_word + " " + metal_word.lower())


if __name__ == '__main__':
    metal_bands()
