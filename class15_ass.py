"""
class Products:
    def __init__(self, name, description, brand, model, price, discount_percentage):
        self.name = name
        self.description = description
        self.brand = brand
        self.model = model
        self.price = price
        self.discount_percentage = discount_percentage

def calculate_discounted_price(product):
    discount_amount = product.price * product.discount_percentage / 100
    discounted_price = product.price - discount_amount
    return discounted_price

# Creating instances of the Products class
product1 = Products(
    name="rice",
    description="Foreign",
    brand="mamagold",
    model="2020",
    price=44000,
    discount_percentage=15
)

product2 = Products(
    name="beans",
    description="drum",
    brand="dangote",
    model="2022",
    price=60000,
    discount_percentage=15
)

product3 = Products(
    name="spaghetti",
    description="tiny",
    brand="golden penny",
    model="2023",
    price=15000,
    discount_percentage=15
)

# Calculating and printing the sum of new prices for the products
products_list = [product1, product2, product3]
total_new_prices = sum(calculate_discounted_price(product) for product in products_list)
print(f"The sum of all the new prices for the products is: {total_new_prices}")

"""



class product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    

    def calculate_discount(self,discount = 10):
        try:
            discount_price = self.price * (discount/100)
        
        
        except TypeError:
            return 'price is a number'
        except:
            return 'error occured'
        return discount_price
    
    def new_price(self):
        discount = self.calculate_discount()
        return self.price - discount

    
product1 = product(
    name="rice",
    description="Foreign",
    
    price=44000,
    
)

product2 = product(
    name="beans",
    description="drum",
    price=60000,
    
)

product3 = product(
    name="spaghetti",
    description="tiny",
    
    price=15000,
   
)

print(product1.price)
print(product1.calculate_discount())
print(product1.new_price())


def cal_all_price(*args):
    all_price = 0
    for product in args:
        all_price += product.new_price()
    return all_price


print(cal_all_price(product1,product2))





