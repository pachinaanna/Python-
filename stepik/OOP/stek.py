class Stack:
    items = []

    def put(self, item):
        self.items.append(item)
        return (self.items)

    def get(self):
        value = self.items[-1]
        del self.items[-1]
        return value


if __name__ == '__main__':
    stack = Stack()
    stack.put(1)
    print("put 1st elelent: " + str(stack.items))
    stack.put(2)
    print("put 2st elelent: " + str(stack.items))
    print("get 1st:" + str(stack.get()))
    print(stack.items)
    print("get 2nd: " + str(stack.get()))
    print(stack.items)
