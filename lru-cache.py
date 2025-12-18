class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        first_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first_node
        first_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

if __name__ == "__main__":
    cap = int(input("Enter cache capacity: "))
    lru = LRUCache(cap)

    while True:
        print("\nOperations: 1. Put  2. Get  3. Exit")
        choice = input("Select operation: ")

        if choice == '1':
            k = int(input("Enter key: "))
            v = int(input("Enter value: "))
            lru.put(k, v)
            print(f"Inserted ({k}, {v})")
        elif choice == '2':
            k = int(input("Enter key to get: "))
            result = lru.get(k)
            print(f"Value: {result}")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")