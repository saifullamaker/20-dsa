# Check whether a subset with the required sum exists

def has_subset_sum(arr, target, index=0):
    if target == 0:
        return True
    if index == len(arr):
        return False

    include = has_subset_sum(arr, target - arr[index], index + 1)
    exclude = has_subset_sum(arr, target, index + 1)
    return include or exclude


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter target sum: "))
    print("Subset exists" if has_subset_sum(arr, target) else "No subset found")
