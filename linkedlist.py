class node:
    Data = None
    prev = None
    next = None

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class doubleLinked:
    head = None
    tail = None
    length = None

    def __init__(self, head, tail, length):
        self.head = head
        self.tail = tail
        self.length = length

    def insertion(self, data):
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

    def deletion(self):
        None

    def search(self, data):
        curr = self.head

        while (curr.next != None):
            if curr.data == data:
                break
            curr = curr.next
        return curr

    def getNode(self, index):
        if self.length < index - 1:
            return None

        curr = self.head
        cnt = 0
        while (cnt <= index - 1):
            curr = curr.next
            cnt += 1

        return curr

    def updateNode(self, index, data):
        curr = self.getNode(index)
        curr.data = data
        None


list1 = doubleLinked(None, None, 0)

list1.insertion("hello")
list1.insertion("world")
list1.insertion("!")

temp = list1.getNode(0)
print(temp.data)
print(list1.search("world").data)
