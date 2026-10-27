# Print numbers from 1 to N using recursion

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)


if __name__ == "__main__":
    number = int(input("Enter N: "))
    print_numbers(number)
