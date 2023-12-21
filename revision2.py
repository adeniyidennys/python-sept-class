import datetime
from changeDateFunc import changeDate


'''
FIND THE MEAN
Create a function that accepts list of dict items as object.
From the objects, the function gets the age of all objects.
and find the Mean on the range of objects' age.

CONFIRM AGE
Create a function that accepts list of dict items as object.
From the objects, the function gets the date of birth of each object.
The function converts the days to position value and month number to month in short words 
i.e { 
    1-11-2023 = 1st-Nov-2023, 
    31-10-23 = 31st-oct-2023 
    }
'''
student1 = {
    'name': 'Samuel',
    'age': 1,
    'gender': 'male',
    'phn_num': '07066444138',
    'DOB': '22-11-2023',
}
student2 = {
    'name': 'Irah',
    'age': 22,
    'gender': 'female',
    'phn_num': '07066444138',
    'DOB': '22-06-2001',
}
student3 = {
    'name': 'Joshua',
    'age': 27,
    'gender': 'male',
    'phn_num': '08066444138',
    'DOB': '29-09-1996',
}

def confirm_Age(*objects_list):
    todays_date = datetime.datetime.now()

    for item in objects_list:

        student_year = int(todays_date.year) - int(item['DOB'][-4:])
        print(student_year)
        if student_year != item['age']:
            print(f'Student age incorrect, please validate\nGiven age is {item["age"]},\nGiven Year of birth is {item["DOB"][-4:]}')
        changeDate(item['DOB'])

confirm_Age(student1, student2, student3)
