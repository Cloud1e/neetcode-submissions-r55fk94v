class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_tail.prev = self.dummy_head
        self.dummy_head.next = self.dummy_tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
        else:
            self.cache[key].val = value
            node = self.cache[key]
            self._move_to_head(node)
        if len(self.cache) > self.capacity:
                node_to_delete = self.dummy_tail.prev
                self._delete_node(node_to_delete)
                del self.cache[node_to_delete.key]

    def _add_to_head(self, node: Node) -> None:
        self.dummy_head.next.prev = node
        node.next = self.dummy_head.next
        node.prev = self.dummy_head
        self.dummy_head.next = node

    def _delete_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: Node) -> None:
        self._delete_node(node)
        self._add_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)