# ---------- Node definition ----------
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# ---------- LRU Cache implementation ----------
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}          # hashmap: key -> Node
        self.cap = capacity

        # dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from doubly linked list
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # insert node at right (most recently used)
    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove least recently used
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# ---------- Test run ----------
if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 1

    cache.put(3, 3)      # evicts key 2
    print(cache.get(2))  # -1

    cache.put(4, 4)      # evicts key 1
    print(cache.get(1))  # -1
    print(cache.get(3))  # 3
    print(cache.get(4))  # 4
