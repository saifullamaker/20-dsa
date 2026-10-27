# Reverse a stack using recursion

def insert_at_bottom(stack, value):
    if not stack:
        stack.append(value)
        return
    top_value = stack.pop()
    insert_at_bottom(stack, value)
    stack.append(top_value)


def reverse_stack(stack):
    if not stack:
        return
    value = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, value)


if __name__ == "__main__":
    stack = list(map(int, input("Enter stack values from bottom to top: ").split()))
    reverse_stack(stack)
    print("Reversed stack:", stack)
