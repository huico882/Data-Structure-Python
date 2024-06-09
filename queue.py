class node:
    Data = None
    prev = None
    next = None

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class Queue:
    head = None
    tail = None
    length = 0

    def __init__(self, head, tail, length):
        self.head = head
        self.tail = tail
        self.length = length

    def enqueue(self, data):
        temp = node(data, None, None)
        temp.data = data

        if self.length == 0:
            self.head = temp
            self.tail = temp
            self.length = 1
        else:
            curr = self.head
            while (curr.next != None):
                curr = curr.next

            curr.next = temp
            temp.prev = curr
            self.tail = temp
            self.length += 1

    def dequeue(self, data):
        if (self.length <= 1):
            self.head = None
            self.length = 0
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

        return temp

    def peek(self, data):
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


queue1 = Queue(None, None, 0)

queue1.enqueue("hello")
queue1.enqueue("world")
queue1.enqueue("How")
queue1.enqueue("are")
queue1.enqueue("you")

print(queue1.search("you").data)
print(queue1.dequeue("you").data)
print(queue1.length)
queue1.clear()
print(queue1.length)
