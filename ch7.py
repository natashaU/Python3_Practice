# Chapter 7.9 Exercises

import math

# write a function that countdowns to zero
def countdown(n):
    while n != 0:
        print(n)
        n = n - 1

# countdown(5)

# EXERCISE 1
# One way of computing square roots is Newtons method.
# Encapsulate it in a function called mysqrt that takes a as a parameter,
# chooses a reasonable value of x, and returns an estimate of the
# square root of a.

def newtons_method(a,x):
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < 0.0000001:
            break
        x = y

# newtons_method(4, 3)


# To test it, write a function named test_square_root that prints a table
# like this:
# a   mysqrt(a)     math.sqrt(a)  diff
# -   ---------     ------------  ----
# 1.0 1.0           1.0           0.0
# 2.0 1.41421356237 1.41421356237 2.22044604925e-16
# 3.0 1.73205080757 1.73205080757 0.0
# 4.0 2.0           2.0           0.0
# 5.0 2.2360679775  2.2360679775  0.0
# 6.0 2.44948974278 2.44948974278 0.0
# 7.0 2.64575131106 2.64575131106 0.0
# 8.0 2.82842712475 2.82842712475 4.4408920985e-16
# 9.0 3.0           3.0           0.0


def mysqrt(a,x):
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.0000001:
            return x
            break
        x = y

def actual_square_method(a):
    return math.sqrt(a)



def test_square_root():
    from decimal import Decimal
    a = 1
    x = 4
    while a < 10:
        y = mysqrt(a,x)
        square_method = math.sqrt(a)
        diff = abs(y - square_method)
        print("\t", a,end=' ')
        print("\t", y, end=' ')
        print("\t", square_method, end=' ')
        y = format(y, ".5f")
        square_method = format(square_method, ".5f")
        y = Decimal(y)
        square_method = Decimal(square_method)
        diff = abs(y - square_method)
        print("\tdiff:", diff,)
        a = a + 1


test_square_root()

# Exercise 2 
# Write a function called eval_loop that iteratively prompts the user,
# takes the resulting input and evaluates it using eval, and prints the result.
# It should continue until the user enters 'done', and then return
# the value of the last expression it evaluated.

def eval_loop():
    while True:
        user_input = input("write a math equation! ")
        if user_input == "done":
            break
        else:
            user_input_eval = eval(user_input)
            print(user_input_eval)


# eval_loop()
