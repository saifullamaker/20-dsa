# Find x raised to the power n using recursion

def power(x, n):
    if n < 0:
        return 1 / power(x, -n)
    if n == 0:
        return 1
    return x * power(x, n - 1)


if __name__ == "__main__":
    x = float(input("Enter the base: "))
    n = int(input("Enter the exponent: "))
    print("Result:", power(x, n))
