"""
Array
List []: ordered, mutable
tuple(): Ordered, Immutable
set{}: unordered
Dict {}: ordered, Mutable. keys and value
"""
    
# List
student = ["Joshua", "Abeeb", "Mr Money", "DA Tee"]
print(student[-2][2:])

#Editing List
#Replacing elements on the list
student[-2] = 'Samuel'
print(student)

#Deleting an element in a list
student.pop(-2)
print(student)
student.remove("Joshua")
print(student)

#Tuple
fruit = ('Orange', 'Apple', 'Banana')
print(fruit[0])
print(fruit[-1])

#Using Insert to copy fruit into the student list
student.insert(0, fruit[0])
print(student)

# student.insert(3, fruit[-1])
# print(student)

#adding new element to the student list
student.append(fruit[-1])

print(student)
student.append('James')
print(student)
student.pop(-1)
print(student)

#inserting the 2nd tuple element at the middle of student list
# x = len(student)
# y = x//2
student.insert(len(student)//2, fruit[1])
print(student)

# to print the index number of an array
print(student.index("Orange"))





















