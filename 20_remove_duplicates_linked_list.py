# Remove duplicates from a sorted singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def print_list(head):
    values = []
    while head:
        values.append(str(head.data))
        head = head.next
    print(" -> ".join(values))


if __name__ == "__main__":
    values = list(map(int, input("Enter sorted values: ").split()))
    head = None
    tail = None

    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    head = remove_duplicates(head)
    print_list(head)
