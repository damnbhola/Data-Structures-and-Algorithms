class Node:
    def __init__(self, value):
        self.value = value
        self.next = self


class CSll:
    root = None

    def __len__(self):
        return self.length()

    def clear(self):
        self.root = None

    def append(self, value):
        temp = Node(value)
        if self.root is None:
            self.root = temp
            return
        start = self.root
        while start.next is not self.root:
            start = start.next
        start.next = temp
        temp.next = self.root

    def insert(self, value, pos):
        temp = Node(value)
        if self.root is None:
            self.root = temp
            return
        start = self.root
        count = 1
        while start.next is not self.root and count < pos:
            count += 1
            start = start.next
        if pos == 0:
            temp.next = self.root
            self.root = temp
        else:
            temp.next = start.next
        start.next = temp

    def pop(self, pos=None):
        if self.root is not None:
            start = self.root
            if start.next is self.root:
                self.root = None
                return start.value
            count = 1
            if pos is None:
                pos = self.length() - 1
            while start.next.next is not self.root and count < pos:
                count += 1
                start = start.next
            if pos == 0:
                start = start.next
                temp = self.root
                self.root = temp.next
            else:
                temp = start.next
            start.next = temp.next
            return temp.value
        print("IndexError: Index out of range")

    def display(self):
        if self.root is None:
            print("c_sll is Empty")
            return
        start = self.root
        while start.next is not self.root:
            print(start.value, end=" ")
            start = start.next
        print(start.value)

    def length(self):
        count = 0
        if self.root is not None:
            count += 1
            start = self.root
            while start.next is not self.root:
                count += 1
                start = start.next
        return count

    def index(self, value):
        if self.root is not None:
            start = self.root
            count = 0
            while start.value != value:
                if start.next is self.root:
                    break
                count += 1
                start = start.next
            else:
                print(count)
                return
        print("ValueError: Value not in sll")

    def loc(self, pos):
        if self.root is not None:
            start = self.root
            count = 0
            while count != pos:
                if start.next is self.root:
                    break
                count += 1
                start = start.next
            else:
                print(start.value)
                return
        print("IndexError: Index out of range")
