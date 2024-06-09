class node:
    Data = None
    prev = None
    next = None

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class stack:
    head = None
    tail = None
    length = None

    def __init__(self, head, tail, length):
        self.head = head
        self.length = length

    def push(self, data):
        temp = node(data, None, None)
        temp.data = data

        if self.length == 0:
            self.head = temp
            self.length = 1
        else:
            temp.next = self.head
            self.head = temp
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        self.length += 1
        return temp

    def peek(self):
        return self.head.data

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def isFull(self):
        None

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def search(self, data):
        curr = self.head

        while (curr.next != None):
            if curr.data == data:
                break
            curr = curr.next
        return curr


s1 = stack(None, None, 0)


s1.push("hello")
s1.push("world")
s1.push("How")
s1.push("are")
s1.push("you")

print(s1.peek())
s1.pop()
print(s1.peek())
s1.push("world")
print(s1.peek())
