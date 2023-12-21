

"""
food_items = ["rice", "beans", "spag", "indomie", "fish"]
utensils = ["knife", "pot", "spoons","fork", "table"]

# Printing items in odd index positions for food_items
print("Items in odd index positions for food_items:")
for i in range(1, len(food_items), 2):
    print(food_items[i])

# Printing items in even index positions for utensils
print("\nItems in even index positions for utensils:")
for i in range(0, len(utensils), 2):
    print(utensils[i])

"""


list1 = ['parach', 'tolu', 2, 'tosin' ,'samuel', 'hello', 'joshua']

list2 = ['pasuma', 'wonder', 7, 'isola' ,'kemuel', 'hi', 'yeshua']




def sortlist(item1, item2 ):

    newlist = []
    if type(item1) != list or type(item2) != list  :
        print('the first parameter is not a list')
    else:
        for eachItem in list1:
            index = list1.index(eachItem)
           # print(eachItem," - ", index)
            if index%2 == 0:
                newlist.append(eachItem)


        for eachItem in list2:
            index = list2.index(eachItem)
           # print(eachItem," - ", index)
            if index%2 == 1:
                newlist.append(eachItem)
                
 
            
    return newlist           





sortlist(list1, list2)



def loopAlist(list):
    try:
        for item in list:
            print(item)

    except NameError:
        print("does not exist")

    except ValueError:
        ('The value you entered can not be processed')
    except:
            print("check your input" )

    else:
        print("no error")

loopAlist(sortlist(list1,list2))

