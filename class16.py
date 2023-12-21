import class15_ass


all_price = class15_ass.cal_all_price
productClass = class15_ass.product

product4 = productClass('yam', 'ewura',5000)
product5 = productClass('macaroni', 'mamagold',7000)

print(product4.price)
print(product4.new_price())

print(all_price(product4,product5), 'All price')

