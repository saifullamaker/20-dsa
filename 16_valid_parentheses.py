# Check whether brackets are balanced using a stack

def is_valid_parentheses(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    text = input("Enter brackets: ")
    print("Valid" if is_valid_parentheses(text) else "Invalid")
