def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

def main():
    try:
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci sequence:")
            fibonacci(num_terms)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
