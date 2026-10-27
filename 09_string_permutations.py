# Generate all permutations of a string

def permutations(text, index=0):
    if index == len(text):
        print("".join(text))
        return

    for i in range(index, len(text)):
        chars = list(text)
        chars[index], chars[i] = chars[i], chars[index]
        permutations(chars, index + 1)


if __name__ == "__main__":
    text = input("Enter a string: ")
    permutations(list(text))
