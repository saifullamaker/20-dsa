# Find the sum of digits using recursion

def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(number))
