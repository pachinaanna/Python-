class Queue:
    items = []

    def put(self, item):
        self.items.append(item)
        return (self.items)

    def get(self):
        value = None
        if len(self.items) != 0:
            value = self.items[0]
            del self.items[0]
        return value

    @staticmethod
    def print():
        print("xxxx")

if __name__ == '__main__':
    queue = Queue()
    queue.put(1)
    print(queue.items)
    queue.put(2)
    print(queue.items)
    queue.get()
    print(queue.items)
    queue.get()
    print(queue.items)
    queue.get()
    print(queue.items)
