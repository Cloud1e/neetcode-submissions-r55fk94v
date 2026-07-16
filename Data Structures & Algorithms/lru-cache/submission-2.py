class DoublyLinkedListNode:
    def __init__(self, key: int = 0, value: int = 0, prev: DoublyLinkedListNode = None, next: DoublyLinkedListNode = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.dummy_head = DoublyLinkedListNode()
        self.dummy_tail = DoublyLinkedListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = DoublyLinkedListNode(key, value)
            self.dict[key] = node
            self._add_to_head(node)
            if len(self.dict) > self.capacity:
                node_to_delete = self.dummy_tail.prev
                self._remove_node(node_to_delete)
                del self.dict[node_to_delete.key]

    def _add_to_head(self, node) -> None:
        old_head_node = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = old_head_node
        old_head_node.prev = node
    
    def _remove_node(self, node) -> None:
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None
    def _move_to_head(self, node) -> None:
        self._remove_node(node)
        self._add_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)