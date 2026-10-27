# Merge two sorted lists into one sorted list

def merge_sorted_arrays(first, second):
    i = j = 0
    merged = []

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    merged.extend(first[i:])
    merged.extend(second[j:])
    return merged


if __name__ == "__main__":
    first = list(map(int, input("Enter first sorted list: ").split()))
    second = list(map(int, input("Enter second sorted list: ").split()))
    print("Merged list:", merge_sorted_arrays(first, second))
