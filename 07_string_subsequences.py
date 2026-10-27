# Print all subsequences of a string

def print_subsequences(text, index=0, current=""):
    if index == len(text):
        print(current)
        return
    print_subsequences(text, index + 1, current)
    print_subsequences(text, index + 1, current + text[index])


if __name__ == "__main__":
    text = input("Enter a string: ")
    print_subsequences(text)
