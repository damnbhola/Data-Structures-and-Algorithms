class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Sll:
    root = None

    def __len__(self):
        return self.length()

    def __reversed__(self):
        return self.reverse()

    def clear(self):
        self.root = None

    def append(self, value):
        temp = Node(value)
        if self.root is None:
            self.root = temp
            return
        start = self.root
        while start.next is not None:
            start = start.next
        start.next = temp

    def insert(self, value, pos):
        if pos >= len(self):
            self.append(value)
            return
        temp = Node(value)
        start = self.root
        if pos == 0:
            temp.next = start
            self.root = temp
        elif pos > 0:
            count = 1
            while count < pos:
                count += 1
                start = start.next
            temp.next = start.next
            start.next = temp
        else:
            print("Position cannot be less than zero")

    def pop(self, pos=None):
        if self.root is not None:
            start = self.root
            if pos == 0 or start.next is None:
                self.root = start.next
                return start.value
            count = 1
            if pos is None:
                pos = self.length() - 1
            while start.next.next is not None and count < pos:
                count += 1
                start = start.next
            temp = start.next
            start.next = temp.next
            return temp.value
        print("IndexError: Index out of range")

    def remove(self, value):
        if self.root is not None:
            start = self.root
            if start.value == value:
                self.root = start.next
                return
            else:
                while start.next is not None and start.next.value != value:
                    start = start.next
                if start.next is not None:
                    start.next = start.next.next
                    return
        print("ValueError: Value not in sll")

    def display(self):
        if self.root is None:
            print("sll is Empty")
            return
        start = self.root
        while start is not None:
            print(start.value, end=" ")
            start = start.next
        print()

    def length(self):
        count = 0
        if self.root is not None:
            start = self.root
            while start is not None:
                count += 1
                start = start.next
        return count

    def index(self, value):
        if self.root is not None:
            start = self.root
            count = 0
            while start is not None:
                if start.value == value:
                    print(count)
                    return
                count += 1
                start = start.next
        print("ValueError: Value not in sll")

    def loc(self, pos):
        if self.root is not None:
            start = self.root
            count = 0
            while start is not None:
                if count == pos:
                    print(start.value)
                    return
                count += 1
                start = start.next
        print("IndexError: Index out of range")

    def reverse(self):
        if self.root is None:
            print("sll is Empty")
            return
        start = self.root
        if start.next is not None:
            t1 = start.next
            start.next = None
            while t1 is not None:
                temp = start
                start = t1
                t1 = t1.next
                start.next = temp
        self.root = start

    def sort(self, reverse=False):
        # Selection Sort
        if self.root is None:
            print("sll is Empty")
            return
        t1 = self.root
        while t1.next is not None:
            val = t1.value
            t2 = t1.next
            t3 = t1
            while t2 is not None:
                if val < t2.value and reverse:
                    val = t2.value
                    t3 = t2
                elif val > t2.value and not reverse:
                    val = t2.value
                    t3 = t2
                t2 = t2.next
            if t1 != t3:
                temp = t1.value
                t1.value = t3.value
                t3.value = temp
            t1 = t1.next
