from __future__ import annotations
from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests
from typing import Optional


class Node:
    key: int
    val: int
    prev: Optional[Node]
    next: Optional[Node]

    def __init__(self, key: int = 0, val: int = 0, prev: Optional[Node] = None, next: Optional[Node] = None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    """
    A data structure that follows the constraints of
    a Least Recently Used (LRU) cache.

    The functions get and put must run in O(1) average
    time complexity.
    """
    capacity: int
    cache: dict[int, Node]
    left: Node
    right: Node

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = dict()
        
        # boundary nodes to avoid size edge cases
        self.left = Node()
        self.right = Node()

        # create linked structure
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert(self, node: Node) -> None:
        prev = self.right.prev
        next = self.right

        # update nodes that will point to this node
        prev.next = next.prev = node

        # update this node's pointers
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self._remove(lru_node)
            del self.cache[lru_node.key]


from collections import OrderedDict
class TrivialLRUCache:
    """
    A trivial solution to LRU Cache that uses
    an OrderedDict to delegate functionality to.
    """
    capacity: int
    cache: OrderedDict

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # make the MRU if already exists
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        # doesn't exist
        return -1

    def put(self, key: int, value: int) -> None:
        # make the MRU if already exists
        if key in self.cache:
            self.cache.move_to_end(key)

        # update the value regardless
        self.cache[key] = value

        # remove the LRU when at capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    lru_cache = LRUCache(2)

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)

    run_tests(
        [GenericTestCase(input=(1,), expected=1)],
        [lru_cache.get],
        label=__file__
    )

    lru_cache.put(3, 3)

    run_tests(
        [GenericTestCase(input=(2,), expected=-1)],
        [lru_cache.get],
        label=__file__
    )

    lru_cache.put(4, 4)

    run_tests(
        [
            GenericTestCase(input=(1,), expected=-1),
            GenericTestCase(input=(3,), expected=3),
            GenericTestCase(input=(4,), expected=4)
        ],
        [lru_cache.get],
        label=__file__
    )
