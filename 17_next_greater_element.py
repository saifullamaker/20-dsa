# Find the next greater element for each item in a list

def next_greater_elements(arr):
    result = [-1] * len(arr)
    stack = []

    for i, value in enumerate(arr):
        while stack and arr[stack[-1]] < value:
            index = stack.pop()
            result[index] = value
        stack.append(i)

    return result


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Next greater elements:", next_greater_elements(arr))
