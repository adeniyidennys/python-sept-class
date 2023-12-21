# set array  
setlist = {'banana', 'apple'}
setlist.add('mango')
print(setlist)

""" methods
.copy()
.clear()
.difference()
"""

setlist1 = {'apple', 'banana','cherry'}
setlist2 = {'apple', 'mango','pear'}

print(setlist1.difference(setlist2))
print(setlist2.difference(setlist1))



""" dictionary {key:value}
unordered, mutable and indexed
"""

student1 = {

"name" : "samuel",
"age" : 52,
"favourite" : "programming",
"status" : "single",
"genotype" : "AA",
"location" : "Ibadan",
"siblings" : ["Olamide", "Asake", "Fireboy"]


}
print(type(student1))
print(student1["name"])
print(student1["status"])


student2 = {

"name" : "Adeniyi",
"age" : 32,
"favourite" : "pytonist",
"status" : "married",
"genotype" : "As",
"location" : "osogbo",
"siblings" : ["Don jazzy", "Rema", "Crayon"]


}


student3 = {

"name" : "Pasuma",
"age" : 65,
"favourite" : "agba_singer",
"status" : "complicated",
"genotype" : "SS",
"location" : "Ikere",
"siblings" : ["taye_curency", "Osupa", "Mr money"]


}

studentList = [student1, student2, student3]


print(studentList)

print(type(studentList))

print(studentList[1]["name"])

print(studentList[2]["siblings"][2][3:].upper())



#  loop in Python
for x in studentList: 
    print(x, '\n\n\n')

for x in studentList:
    print(x["name"])
for x in studentList:
    print(x["siblings"])

for x in studentList:
    siblings = x["siblings"]
    print(siblings)