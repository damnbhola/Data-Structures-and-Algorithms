class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    top = None

    def __len__(self):
        return self.length()

    def clear(self):
        self.top = None

    def push(self, value):
        temp = Node(value)
        if self.top is not None:
            temp.next = self.top
        self.top = temp

    def pop(self):
        if self.top is None:
            print("IndexError: pop from an empty stack")
            return
        temp = self.top
        self.top = self.top.next
        return temp.value

    def display(self):
        if self.top is None:
            print("stack is Empty")
            return
        start = self.top
        while start is not None:
            print(start.value, end=" ")
            start = start.next
        print()

    def length(self):
        count = 0
        if self.top is not None:
            start = self.top
            while start is not None:
                count += 1
                start = start.next
        return count

    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def stackTop(self):
        if self.top is None:
            print("stack is Empty")
            return
        return self.top
