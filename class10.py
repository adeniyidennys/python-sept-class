"""

Given an integer 'n', perform the following conditional actions

If n is odd, print "Weird' 
If n is even and in the inclusive range of 2 to 5, print 'Not Weird'

If n is even and in the inclusive range of 6 to 20, print "Weird"

If n is even and greater than 28, print 'Not Weird




1,

    step 1:
        get an input - convert your input to integer

    step 2:
        check input is odd, if it is odd,
            print output is "weird"
        else input is even
            if input is between 2 to 5   
                output "Not weird"
            else input is between 6 to 20
                output "weird"
            else input is greater than 20
                output 'NOT WEird'

            





"""

"""

def check_number(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n > 20:
            print("Not Weird")


# Testing the function with some example values
check_number(3)  # Example odd number
check_number(4)  # Example even number in the range 2 to 5
check_number(6)  # Example even number in the range 6 to 20
check_number(30)  # Example even number greater than 28



"""


try:
    n = int(input("Enter an integer: "))
except ValueError:
    print("Invalid characters. Please enter an integer.")
    exit()

if n % 2 != 0:
    print("Weird")
else:
    if n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n > 20:
        print("Not Weird")
