class LinkedLst:
    node = None

    def put(self, value):
        if not self.node:
            self.node = Node(value, None)
        else:
            self.node.save_next(value)

    def remove(self, index):
        previous_node = None
        next_node = None
        current_node = self.node
        count = 1

        while count <= index:
            previous_node = current_node
            current_node = current_node.next
            if current_node.next:
                next_node = current_node.next
            count += 1

        previous_node.next = next_node

    def get(self, index):
        if index == 0:
            return self.node.value
        count = 1
        current_node = self.node.next
        while count <= index:
            if count == index:
                return current_node.value
            current_node = current_node.next
            count += 1

    def print(self):
        current_node = self.node
        while (current_node):
            print(current_node.value, end=" ")
            current_node = current_node.next


class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def save_next(self, value):
        if not self.next:
            self.next = Node(value, None)
        else:
            self.next.save_next(value)


if __name__ == '__main__':
    list = LinkedLst()
    list.put(1)
    list.put(2)
    list.put(3)

    print(list.get(0))
    print(list.get(1))
    print(list.get(2))

    list.print()
    list.remove(1)
    print()
    list.print()
    list.remove(1)
    print()
    list.print()