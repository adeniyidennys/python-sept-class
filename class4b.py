fruitlist = ["banana", "Apple", "pineapple","mango", "orange", "pawpaw"]

for fruit in fruitlist:
    print(fruit.upper())

school = "parach"
for x in school:
    print(x)

for letter in school:
    print(letter, school.index(letter))


for x in range(0,10):
    print("hello")




student1 = {

"name" : "samuel",
"age" : 52,
"favourite" : "programming",
"status" : "single",
"genotype" : "AA",
"location" : "Ibadan",
"siblings" : ["Olamide", "Asake", "Fireboy"]


}



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

for x in studentList:
    print("Hello "+ x['name']+", welcome "+school.upper())




