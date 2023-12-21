x = "hello"
listItem =[]

# for i in listItem:
#     print(i)

for i in x:
   # print(i)
    listItem.append(i)

listItem.reverse()
x2 = "".join(listItem)
print(x2)




# a = 0
# while a < 10:
#     print(a)
#     a = a + 1
    
studentList = ["Joshua", "Samuel", "Parach"]
student1 = {
        "name": "Joshua",
        "age":20,
        "gender" : "M",
        "PhoneNumber": "08157206357",
        "Dob":"20-2-1998"

}    

student2 = {
        "name": "Samuel",
        "age":27,
        "gender" : "M",
        "PhoneNumber": "08037865784",
        "Dob": "29-9-1996"

}    
student3 = {
        "name": "Parach",
        "age":37,
        "gender" : "F",
        "PhoneNumber": "09057206357",
        "Dob": "27-8-1990"

}
student4 = {
        "name": "Adeniyi",
        "age":29,
        "gender" : "M",
        "PhoneNumber": "07066444138",
        "Dob":"4-10-1998"

}    
student5 = {
        "name": "Ayra",
        "age":22,
        "gender" : "F",
        "PhoneNumber": "07022444571",
        "Dob":"26-2-1876"

}


# QUESTION
"""
    CRATE A FUNCTIN THAT CREATES LISTS OF THE DICT ITEMS
        FIND THE MEAN OF ALL THE STUDENTS AGE
    create another function that changes the int month to the months in words 

    FIND THE MEAN
Create a function that accepts List of dict Items as object.
From the objects, the function gets the "age" of all objects. and find the Mean on the range of objects, "age"

        CREATE a function that accepts list of dict items as objects, from the objects, the function gets the date of birth of each object. the function
        converts the days to position value and the month number number to month in shorth words. i.e {
        
        1-11-2023 = 1st-Nov-2023,
        31-10=2023 = 31st-Oct-2023
        }


"""

#    1

def find_mean_age(student_list):
    ages = [student["age"] for student in student_list]
    if len(ages) == 0:
        return 0
    mean_age = sum(ages) / len(ages)
    return mean_age

# Sample usage with the list of student dictionaries
student_list = [student1, student2, student3, student4, student5]
mean_age = find_mean_age(student_list)
print(f"The mean age of the students is {mean_age}")


#    2


def convert_dob_to_readable_date(student_list):
    month_dict = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
        7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }
    
    for student in student_list:
        dob_parts = student["Dob"].split('-')
        day = int(dob_parts[0])
        month = int(dob_parts[1])
        year = dob_parts[2]
        
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]

        month_name = month_dict.get(month, 'Invalid Month')
        new_dob = f"{day}{suffix}-{month_name}-{year}"
        student["Dob"] = new_dob
    return student_list

# Example usage with the provided list of student dictionaries
student_list = [student1, student2, student3, student4, student5]
converted_list = convert_dob_to_readable_date(student_list)
for student in converted_list:
    print(f"{student['name']}'s date of birth is {student['Dob']}")

