# Exercise 8, Chapter 10


""" Exercise 8
This exercise pertains to the so-called Birthday Paradox, which you can read
about at http://en.wikipedia.org/wiki/Birthday_paradox.
If there are 23 students in your class, what are the chances that two of you
have the same birthday? You can estimate this probability by generating random
samples of 23 birthdays and checking for matches. Hint: you can generate random
birthdays with the randint function in the random module."""




def birthday_paradox(trial=1000):
    import random
    total = 0
    for trialNum in range(trial):
        bDayList = []
        for i in range(23):
            bDay = random.randint(0, 365)
            bDayList.append(bDay)
        bDayList.sort()
        sameDay = False
        for i in range(len(bDayList) - 1):
            if bDayList[i] == bDayList[i + 1]:
                sameDay = True
        if sameDay:
            total += 1
    prop = (total / trial) * 100
    print("The propability is ", prop, "percent" )


# birthday_paradox(50)

# I know I can seperate this into different functions to avoid bugs. The book has a different answer:
#http://greenteapress.com/thinkpython2/code/birthday.py
