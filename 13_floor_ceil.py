# Find the floor and ceil of a value in a sorted list

def floor_ceil(arr, target):
    floor_value = None
    ceil_value = None

    for value in arr:
        if value <= target:
            floor_value = value
        if value >= target:
            ceil_value = value
            break

    return floor_value, ceil_value


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted numbers: ").split()))
    target = int(input("Enter target: "))
    floor_value, ceil_value = floor_ceil(arr, target)
    print("Floor:", floor_value)
    print("Ceil:", ceil_value)
