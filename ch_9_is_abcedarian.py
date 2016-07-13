# Exercise 6
# Write a function called is_abecedarian that returns True if the letters in a word appear in
# alphabetical order (double letters are ok).
# How many abecedarian words are there?

def is_abcedarian(word):
    i = 0
    while i < len(word) - 1:
        if word[i] > word[i + 1]:
            return False
        i = i + 1
    return True

# DPB: Looks good at first, but...

# In [1]: import ch_9_is_abcedarian
# 
# In [2]: ch_9_is_abcedarian.is_abcedarian('bad')
# Out[2]: False
# 
# In [3]: ch_9_is_abcedarian.is_abcedarian('Bad')
# Out[3]: True

# DPB: "B" is considered "smaller" than "a" because the capital letters appear
# before the lower case letters in Unicode, and that's the what you're
# comparing when you use the greater-than sign. You can find the Unicode
# codepoint (in decimal) using "ord(c)", where c is a string containing the
# character you are asking about

# Here's one idea: convert the word to lower case first:

def is_abcedarian_02(word):
    word = word.lower()
    i = 0
    while i < len(word) - 1:
        if word[i] > word[i + 1]:
            return False
        i = i + 1
    return True

# Now check the output:

# In [4]: dreload(ch_9_is_abcedarian)
# Out[4]: <module 'ch_9_is_abcedarian' from 'ch_9_is_abcedarian.py'>
#
# In [5]: ch_9_is_abcedarian.is_abcedarian_02('Bad')
# Out[5]: False
# 
# In [6]: ch_9_is_abcedarian.is_abcedarian_02('accent')
# Out[6]: True
# 
# In [7]: ch_9_is_abcedarian.is_abcedarian_02('accEnt')
# Out[7]: True

