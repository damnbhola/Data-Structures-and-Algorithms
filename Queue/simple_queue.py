class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SimpleQueue:
    front = None

    def __len__(self):
        return self.length()

    def clear(self):
        self.front = None

    def enqueue(self, value):
        temp = Node(value)
        if self.front is None:
            self.front = temp
            return
        start = self.front
        while start.next is not None:
            start = start.next
        start.next = temp

    def dequeue(self):
        if self.front is None:
            print("IndexError: pop from an empty queue")
            return
        temp = self.front
        self.front = self.front.next
        return temp.value

    def display(self):
        if self.front is None:
            print("queue is Empty")
            return
        start = self.front
        while start is not None:
            print(start.value, end=" ")
            start = start.next
        print()

    def length(self):
        count = 0
        if self.front is not None:
            start = self.front
            while start is not None:
                count += 1
                start = start.next
        return count

    def isEmpty(self):
        if self.front is None:
            return True
        return False
