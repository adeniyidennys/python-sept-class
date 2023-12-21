"""
print("WELCOME TO THE UNIVERSITY OF IBADAN")
english = input("Enter student's English score: ")
math = input("Enter student's Math score: ")

print(f'your english score is {english}')
print(f'your math score is {math}')

if english.isnumeric() and math.isnumeric():
    english = int(english)
    math = int(math)

    if english <0 or english >100 or math <0 or math >100:
        print("\n invalid score \n")
    else:
        if english >= 50 and math >= 50:
            print("Congratulations! The student is eligible for admission to the University of Ibadan.")
        else:
            print("Sorry, the student does not meet the admission requirements for the University of Ibadan.")


else:
    print('invalid characters')

"""

print("WELCOME TO OAU")
english = input("Enter student's English score: ")
math = input("Enter student's Math score: ")

print(f'your english score is {english}')
print(f'your math score is {math}')

if english.isnumeric() and math.isnumeric():
    english = int(english)
    math = int(math)

    if english <0 or english >100 or math <0 or math >100:
        print("\n invalid score \n")
    else:
        if english >= 50 or math >= 50:
            print("Congratulations! The student is eligible for admission to the University of Ibadan.")
        else:
            print("Sorry, the student does not meet the admission requirements for the University of Ibadan.")


else:
    print('invalid characters')
