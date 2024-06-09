class node:
    key = None
    value = None
    next = None

    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class hashtable:
    length = None
    buckets = None
    size = None

    def __init__(self, size):
        self.buckets = [None] * size
        self.length = 0
        self.size = size

    def hash_function(self, key):
        return hash(key) % self.size

    def insertion(self, key, value):
        index = self.hash_function(key)
        temp = node(key, value, None)
        if not self.buckets[index]:
            self.buckets[index] = temp
        else:
            bucket = self.buckets[index]
            while bucket.next:
                bucket = bucket.next
            bucket.next = temp
        self.length += 1

    def search(self, key, value):
        index = self.hash_function(key)
        current = self.buckets[index]
        while current:
            if current.key == key and current.value == value:
                return current
            current = current.next
        return None

    def deletion(self, key, value):
        index = self.hash_function(key)
        current = self.buckets[index]
        if current.key == key and current.value == value:
            self.buckets[index] = current.next
            return current

        while current.next:
            if current.next.key == key and current.next.value == value:
                temp = current.next
                current.next = current.next.next
                return temp
            current = current.next
        return None


ht = hashtable(4)


ht.insertion("cars", "Chevy")
ht.insertion("cars", "toyota")
ht.insertion("cars", "camry")
ht.insertion("toys", "cars")
ht.insertion("toys", "truck")
ht.insertion("toys", "spaceship")
ht.insertion("people", "me")
ht.insertion("people", "Fahad")
ht.insertion("people", "marcus")

print(ht.search("cars", "Chevy").value)
ht.deletion("cars", "Chevy")
print(ht.search("cars", "Chevy"))
print(ht.search("cars", "toyota").value)
