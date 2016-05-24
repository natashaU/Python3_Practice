# Exercise 3
# Write a function named is_triangle that takes three integers as arguments,
# and that prints either “Yes” or “No”, depending on whether you can or
# cannot form a triangle from sticks with the given lengths.

def is_triangle(a,b,c):
    if a > b + c or b > a + c or c > a + b:
        print("No")
    else:
        print("yes")

# is_triangle(3,4,5)

# Write a function that prompts the user to input three stick lengths, converts
# them to integers, and uses is_triangle to check whether sticks with the
# given lengths can form a triangle.

def user_input():
    a = int(input("What's the value of one side of a triangle?\n"))
    b = int(input("What's the length of the second side?\n"))
    c = int(input("Whats the length of the third side?\n"))
    is_triangle(a,b,c)

# user_input()
