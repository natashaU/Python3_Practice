#Exercise 2
#Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
#(a to the power of n) + (b to the power of n) = (c to the power of n)

#for any values of n greater than 2.
#Write a function named check_fermat that takes four parameters—a, b, c and n—and checks to see if Fermat’s theorem holds. If n is greater than 2 and
#an + bn = cn
#the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”
#Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.



def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, fermat was wrong!")
    else:
        print("No, that doesn't work. You are a LOSER.")


def user_inputs_fermat():
    a = int(input("Pick a number for a\n"))
    b = int(input("Pick a number for b\n"))
    c = int(input("Pick a number for c\n"))
    n = int(input("Pick a number for n\n"))
    check_fermat(a,b,c,n)


check_fermat(1,2,3,3)
user_inputs_fermat()
