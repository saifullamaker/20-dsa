# Find the Fibonacci number using recursion

def fibonacci(n):
    if n < 0:
        raise ValueError("Enter a non-negative number")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    number = int(input("Enter the position: "))
    print("Fibonacci number:", fibonacci(number))
