"""

FUNCTION:  
            -Block of codes that is reusable
            -only runs when invoked 
            -can accept data
            -return data as output

        
"""


"""
def greetings():
    print("hello World")


greetings()

def students():
    print('Tade')

#print(greetings(),students())

"""

def greeting():
    name = "parach"
    print("Hello", name)



name = "Money"

def greetings(person):
    school = "university of ibadan"
    print(f"{person} attended {school}")
    print(f"{name} is a friend to {person}")

greeting()
greetings("Tade")
greetings("Pasuma")


def add_nums(num1, num2):
    print(num1 + num2)

add_nums(6,4)
add_nums(30,30)

def sub_nums(num1, num2):
    print(num1 - num2)

sub_nums(6,4)

def mut_nums(num1, num2):
    print(num1 * num2)

mut_nums(6,4)

def div_nums(num1, num2):
    print(num1 / num2)
div_nums(6,4)

#naira_to_dollar

def naira_to_dollar (amount):
    print( amount / 1100)

naira_to_dollar(50000)

# dollar to naira

def dollar_to_naira (amount):
    print(amount * 1100)

dollar_to_naira(500)


# celcius to fahrenheit

def cel_to_fah(degree):
    print(degree * 1.8 + 32) 

cel_to_fah(32)

# fahrenheit to celcius

def fah_to_celcius(degree):
    print((degree - 32) / 1.8)

fah_to_celcius(89.6)




scorelists = [32,46,59,67,80]


"""

def gradefunction(result):
    score = [40, 50, 60, 70]
    grade = ["F","D", "C", "B", "A"]


    if result.isnumeric():
        result = int(result)
        if result < 0 or result >100:
            print('\n\n=====')
            print('you have entered invalid result. \n enter a value between 0 - 100 \n\n')

        else:
            for mark in score:
                index = score.index(mark)
                if result < mark:
                    print(f'student grade for {result} - {grade[index]}')
                    break
                else:
                    # print(f"student grade for {result} - A")
                    print(f"student grade for {result} - {grade[-1]}")
                    break

    else:
        print('input contains invalid characters')
    


for score in scorelists:
    gradefunction(score)


"""


def gradefunction(result):
    score = [40, 50, 60, 70]
    grade = ["F","D", "C", "B", "A"]

    if isinstance(result, int) or result.isnumeric():
        if isinstance(result, str):
            result = int(result)
        if result < 0 or result > 100:
            print('\n\n=====')
            print('you have entered invalid result. \n enter a value between 0 - 100 \n\n')
        else:
            for mark in score:
                index = score.index(mark)
                if result < mark:
                    print(f'student grade for {result} - {grade[index]}')
                    break
            else:
                print(f"student grade for {result} - {grade[-1]}")
    else:
        print('input contains invalid characters')

scorelists = [32,46,59,67,80]
for score in scorelists:
    gradefunction(score)




#  RECURSIVE FUNCTION

def recursive_function(option):
    if option.isalpha():
        if option.casefold() == 'a':
            print('the recursive function have been called')
            recursive_function(input("Enter another command: "))
            # exit() 
        if option.casefold() == 'b':
            print('the recursive function have been called')
            recursive_function(input("Enter another command: "))


        else:
            print('the end of the recursive function')
    

a = "A"
recursive_function(a)