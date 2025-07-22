# Simple Fibonacci generator in Python 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Ask the user for input
num = int(input("How many Fibonacci numbers do you want? 👉 "))
print("\nHere's your sequence:")
fibonacci(num)
