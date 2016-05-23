#Exercise 3
#Note: This exercise should be done using only the statements and other features we have learned so far.
#Write a function that draws a grid like the following:
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print(arg,end="")
    print(arg,end="")

def print_twice_newline(arg):
    print(arg)
    print(arg)

def do_four(f, arg):
    do_twice(f,arg)
    do_twice(f,arg)

# do_twice(print_twice, "natasha")
# do_four(print_twice, "natasha")

def make_grid():
    print_twice("+" + "----")
    print("+")
    do_twice(print_twice_newline, "|" + "    " + "|" + "    " + "|")
    print_twice("+" + "----")
    print("+")
    do_twice(print_twice_newline, "|" + "    " + "|" + "    " + "|")
    print_twice("+" + "----")
    print("+")

make_grid()
