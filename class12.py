# FIBONACCI SEQUENCE

# a, b = 0, 1

# while a < b :
#     a = b
#     c = a
#     print(c)



# n = 5
# num1 = 0
# num2 = 1
# next_number = num2
# count = 1

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    return fib_sequence

n = 10  # Change this value to generate the Fibonacci sequence of desired length
fib_sequence = fibonacci(n)

last_value = fib_sequence[-1]
result = (last_value * 5) / 2


print(f" Fibonacci sequence  {fib_sequence} \n \n  last valu * 5 / 2 = {result}")



name = "palazo"
print(name.center(50))