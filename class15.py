class Student():
    
    def __init__(self, firstName, lastName, age, phn_num, DOB):
        self.firstName = firstName
        self.lastName = lastName
       
        self.age = age
        self.phn_num = phn_num
        self.DOB = DOB
    
    
    
    def changeDate(self):
        
        day = self.DOB.split('-')[0]
        mon = self.DOB.split('-')[1]
        year = self.DOB.split('-')[2]

        # Remove 0 on the days
        if day.startswith('0'):
            day = day[1:]

        # Remove 0 on the months
        if mon.startswith('0'):
            mon = mon[1:]

        # Putting position on day
        if day.endswith('11') or day.endswith('12') or day.endswith('13'):
            day += 'th'
        elif day.endswith('1'):
            day += 'st'
        elif day.endswith('2'):
            day += 'nd'
        elif day.endswith('3'):
            day += 'rd'
        else:
            day += 'th'

        mon_short_word = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        mon_Sht = mon_short_word[int(mon)-1]
            
        
        print(f'{day}-{mon_Sht}-{year}')
        return f'{day}-{mon_Sht}-{year}'


    def returnEmail (self):
        return f'{self.firstName.lower()}.{self.lastName.lower()}@parachdschl.com'





student1 = Student(
    firstName = 'Samuel',
    lastName = 'Pasuma',
    age = 1,
    phn_num = '07066444138',
    DOB = '22-11-2023',
)

student2 = Student(
    firstName= 'Cray',
    lastName = 'Way',
    age = 33,
    phn_num = '08066444138',
    DOB = '24-09-1990',
)



print(student1.firstName)
print(student1.changeDate())
print(student1.returnEmail())
 
"""

CREATE A PRODUCT OBJECTs with NAME , DESCRIPTION, BRAND, MOdEL, PRICE, DISCOUNT

CALCULATE THE TOTAL NUMBER OF all OBJECTS PRICe after removing the discounts


"""


class products():
    
    def __init__(self, name, description, brand, model, price, discount_percentage):
        self.name = name
        self.description = description
       
        self.brand = brand
        self.model = model
        self.price = price
        self.discount_percentage = discount_percentage



product1 = products(
    name = "rice",
    description = "Foreign",
    brand = "mamagold",
    model = "2020",
    price = 44000,
    discount_percentage = 15

)

product2 = products(
    name = "beans",
    description = "drum",
    brand = "dangote",
    model = "2022",
    price = 60000,
    discount_percentage = 15

)




product3 = products(
    name = "spaghetti",
    description = "tiny",
    brand = "golden penny",
    model = "2023",
    price = 15000,
    discount_percentage = 15

)


print(product1.name)





