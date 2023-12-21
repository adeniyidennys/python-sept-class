import mysql.connector

database1 = mysql.connector.connect(host = 'localhost' , user = 'root',passwd = 'adeniyi', database = 'pythonClass16_db' )
action = database1.cursor()
# action.execute(
#     'CREATE TABLE products (name VARCHAR(50), desc VARCHAR(100), price INT, disc_percent INT, new_price INT )')

# action.execute("SHOW TABLES")

print( "\n Tables created")


create1 = "INSERT INTO products (product_name, price, discount_percentage, new_price) VALUES (%s, %s, %s, %s)"
update = "UPDATE products SET price = %s WHERE product_name = %s "
delete = "DELETE FROM products WHERE product_name = %s"

# action.execute("UPDATE products SET price = 50000 WHERE product_name = 'spaghetti' ")


# action.execute('SELECT * FROM products')

# allProduct = action.fetchall()
# for product in allProduct:
#     print(product)



# # action.execute('SHOW TABLES')

# # print(action)
# # for item in action:
# #     print(item)





