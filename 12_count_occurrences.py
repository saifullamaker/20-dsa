# Count occurrences of a value in a sorted list

def count_occurrences(arr, target):
    first = -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if first == -1:
        return 0

    last = first
    left, right = first + 1, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last - first + 1


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted numbers: ").split()))
    target = int(input("Enter target: "))
    print("Occurrences:", count_occurrences(arr, target))
