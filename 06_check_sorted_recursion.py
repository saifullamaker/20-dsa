# Check whether a list is sorted using recursion

def is_sorted(arr, index=0):
    if index >= len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted(arr, index + 1)


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Sorted" if is_sorted(arr) else "Not sorted")
