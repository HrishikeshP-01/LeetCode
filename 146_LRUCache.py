
"""
Hashmap + Doubly Linked List Approach
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Hashmap
        self.head = Node(0, 0) # Dummy node so we don't have to worry abt starting from empty
        self.tail = Node(0, 0) # Dummy node so we don't have to worry about updating the tail whenever the original last node is updated
        self.head.right = self.tail
        self.tail.left = self.head

    def remove(self, node:Node): # Remove node from the list
        left = node.left
        right = node.right
        left.right = right
        right.left = left

    def insertAtEnd(self, node:Node):
        left = self.tail.left
        self.tail.left = node
        left.right = node
        node.left = left
        node.right = self.tail

    def get(self, key: int) -> int:
        # Edge case - the key doesn't exist
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.remove(node)
        self.insertAtEnd(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        # What if another node exists in key
        # This node will also exits in the list
        # The key needs to be replaced & the node needs to be removed from the list
        node = self.cache.get(key, None)
        if node:
            self.remove(node)
        node = Node(key, value)
        self.cache[key] = node
        self.insertAtEnd(node)

        if len(self.cache.keys()) > self.cap:
            node_to_remove = self.head.right
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)