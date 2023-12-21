"""
CREATE STATE AND CAPITAL
READ LIST
UPDATE/EDIT A STATE OR/AND ITS CAPITAL
DELETE A STATE AND ITS CAPITAL



"""

"""

state_capital = [


    {
        "state": "Abia",
        "capital": "Umuahia"
    },
    {
        "state": "Ebonyi",
        "capital": "Abakaliki"

        
    },
    {
        "state": "Taraba",
        "capital": "Jalingo"
    },
    {
        "state": "Delta",
        "capital": "Asaba"
    },
    {
        "state": "Akwa-Ibom",
        "capital": "Uyo"
    }
    

]

print("enter Option A - D")
print("A to view the list of states and capital")
print("B to create a state and capital")
print("C to edit a state and capital ")
print("D to delete a state and capital")
user_input = str(input("Enter your option: ")).casefold()

if user_input == 'a':
    numbering = 0
    for item in state_capital:
        numbering+=1
        (print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}"))

elif user_input == 'b': 
    state = str(input("The new state: "))
    capital = str(input(f" Enter the capital of {state}: "))
    new_state_capital = {
            "state": state,
            "capital": capital
            }
    state_capital.append(new_state_capital)
    numbering = 0
    for item in state_capital:
        numbering+=1
        (print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}"))

elif user_input == 'c':
    numbering = 0
    for item in state_capital:
        numbering+=1
        (print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}"))
    edit_number = input("enter the number of state to edit ")
    target_state_capital = state_capital[int(edit_number)-1]
    state = input("Enter the correct state: ")
    capital = input("enter the correct capital: ")
    
    if state:
        target_state_capital["state"] = state
    if capital:
        target_state_capital["capital"] = capital
    numbering = 0
    for item in state_capital:
        numbering+=1
        (print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}"))

elif user_input == 'd':
    numbering = 0
    for item in state_capital:
        numbering+=1
        print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}")
    delete_number = input("enter the number of state to delete ")
    state_capital.pop(int(delete_number)-1)
    numbering = 0
    for item in state_capital:
        numbering+=1
        print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}")



"""





state_capital = [
    {"state": "Abia", "capital": "Umuahia"},
    {"state": "Ebonyi", "capital": "Abakaliki"},
    {"state": "Taraba", "capital": "Jalingo"},
    {"state": "Delta", "capital": "Asaba"},
    {"state": "Akwa-Ibom", "capital": "Uyo"}
]

print("Enter Option A - D")
print("A to view the list of states and capitals")
print("B to create a state and capital")
print("C to edit a state and capital")
print("D to delete a state and capital")

user_input = str(input("Enter your option: ")).casefold()

if user_input == 'a':
    numbering = 0
    for item in state_capital:
        numbering += 1
        print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}")

elif user_input == 'b':
    state = input("Enter the new state: ")
    capital = input(f"Enter the capital of {state}: ")
    new_state_capital = {
        "state": state,
        "capital": capital
    }
    state_capital.append(new_state_capital)
    numbering = 0
    for item in state_capital:
        numbering += 1
        print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}")

elif user_input == 'c':
    numbering = 0
    for item in state_capital:
        numbering += 1
        print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}")
    edit_number = input("Enter the number of the state to edit ")

    if edit_number.isdigit() and 0 < int(edit_number) <= len(state_capital):
        target_state_capital = state_capital[int(edit_number) - 1]
        state = input("Enter the correct state: ")
        capital = input("Enter the correct capital: ")
        if state:
            target_state_capital["state"] = state
        if capital:
            target_state_capital["capital"] = capital
        numbering = 0
        for item in state_capital:
            numbering += 1
            print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}")
    else:
        print("Invalid input. Please enter a valid number.")

elif user_input == 'd':
    numbering = 0
    for item in state_capital:
        numbering += 1
        print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}")
    delete_number = input("Enter the number of the state to delete ")
    if delete_number.isdigit() and 0 < int(delete_number) <= len(state_capital):
        state_capital.pop(int(delete_number) - 1)
        numbering = 0
        for item in state_capital:
            numbering += 1
            print(f"{numbering}. the state {item['state']}, the capital - {item['capital']}")
    else:
        print("Invalid input. Please enter a valid number.")
else:
    print("Invalid input. Please enter a valid option (A, B, C, or D).")




