tupple1 =("parach","Joshua","42",["Hello", "wold"])
tupple2 = (1,2,3,4,5)
tupple3 = (tupple1+tupple2)
print(tupple1)
print(tupple2)
print(tupple3)
for x in  tupple1:
    print(x)


str1 = ""
for x in tupple1:
    str1+= str(x)
    print(x)


# mathResult = int(input("Enter student math result: "))
# englishResult = int(input("Enter your English result:"))

"""
mathResult = input("Enter student math result: ")
englishResult = input("Enter your English result:")

result = int(mathResult) + int(englishResult)
print(result) 

"""

tuppleString = ""

for x in tupple1:
    tuppleString = tuppleString + str(x) + ', '
    print(tuppleString)

print(tuppleString)

a = tuppleString.split(",")
a.pop()
print(a)
