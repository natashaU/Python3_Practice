# In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings
# are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
# This loop outputs these names in order:

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
#     print(letter + suffix)

# The output is:
# Jack
# Kack
# Lack
 #Mack
# Nack
# Oack
# Pack
# Qack
# Of course, that’s not quite right because “Ouack” and “Quack” are misspelled.
# As an exercise, modify the program to fix this error.


# Original:

def ducklings(stringHere):
    prefixes = 'JKLMNOPQ'
    for letter in prefixes:
	if letter == "O" or letter == "Q":
	    print(letter + "u" + suffix)
	else:
	    print(letter + suffix)

# To test function:
# suffix = 'ack'
# ducklings(suffix)

# DPB: Note: you should use "suffix" as the name of the argument. The only
# reason the program was working in your test is that you had declared the
# variable "suffix" elsewhere in the REPL.

def ducklings(suffix):
    prefixes = 'JKLMNOPQ'
    for letter in prefixes:
	if letter == "O" or letter == "Q":
	    print(letter + "u" + suffix)
	else:
	    print(letter + suffix)


# DPB: Rather than use two separate "predicates" in the "if" block, here is a
# shorter way:

def ducklings_01(suffix):
    prefixes = 'JKLMNOPQ'
    for c in prefixes:
        if c in ['O', 'Q']:
            print(c + "u" + suffix)
        else:
            print(c + suffix)

# Also, I use "c" to stand for "character", which is a more usual name for
# "letter" (and can include characters other than plain letters).

# DPB: Another idea is to have a single print statement, but prepare the
# content you plan to print in the if-else block. That's better practice, since
# we sometimes like to keep printing (in fact, any user-interaction) separate
# from the "business logic" of the program. For example:

def ducklings_02(suffix):
    prefixes = 'JKLMNOPQ'
    for c in prefixes:
        if c in ['O', 'Q']:
            to_print = c + "u" + suffix
        else:
            to_print = c + suffix
        print(to_print)

# DPB: An even terser way to do this:

def ducklings_03(suffix):
    prefixes = 'JKLMNOPQ'
    for c in prefixes:
        infix = 'u' if c in ['O', 'Q'] else ''
        print(c + infix + suffix)

# Please take a close look at how the line beginning "infix" works.
