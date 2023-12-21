# python conditional statement

x = 20
y = 50

if x > y :
    print("x is greater than y")
else :
    print("y is grater tham x")



if (x!= y) and (x > y) :
    print("x is greater")
else:
    print("y is greater than x")

if x == y:
    print("x is equal y")
elif x > y :
    print("x is greater than y")
elif x < y :
    print("x is lesser")
else :
    ("x is invalid")


#input score Grading


#score = int(input("add score:"))
#if (score < 0) or (score > 100): 
#    print("invalid score")
#else:
 #   print(score)


"""

#if method

score = input("enter your score:")

print(f'your input is {score}')
if score.isnumeric():
    score = int(score)
    if score < 0 or score > 100:
        print('\n\n=====')
        print('you have entered invalid scor.\n enter a value between 0 - 100\n\n')
    else:
        if score < 40:
            print(f'student grade for {score}' is F)
        elif score < 50:
            print(f'student grade for {score} is D')
        elif score < 60:
            print(f'student grade for {score} is C')
        elif score < 70:
            print(f'student grade for {score} is B')
        else:
            print(f'student grade for {score} is A')
else:
        print('score contains other characters')   


"""





#loop method

# 



# studentlist = ['samuel', 'Parach', 'Joshua']
# age = [95, 102, 83]

# for student in studentlist:
#     index = studentlist.index(student)
#     print(student,age[index])


score = [40, 50, 60, 70]
grade = ["F","D", "C", "B", "A"]
result = (input("enter student score: "))

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
    
