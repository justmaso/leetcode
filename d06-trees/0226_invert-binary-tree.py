from __future__ import annotations
from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, invert the tree,
    and return its root.
    """

    def iterativeInvertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts the binary tree iteratively using a double-ended
        queue (BFS approach).

        Each valid node is visited exactly once, swapping its left
        and right children. The children are then added to the queue
        for later processing until all nodes have been processed.

        Time:
            O(n) - Each of the n nodes is dequeued, swapped, and 
                   enqueued exactly once.
        Space:
            O(w) - Where w is the maximum width of the tree.
                   Worst case (complete binary tree) is O(n) space in the queue. 
        """
        from collections import deque
        d = deque([root])

        # continue swapping valid nodes until finished
        while d:
            node = d.popleft()

            # skip null nodes
            if not node:
                continue

            # swap this nodes children
            node.left, node.right = node.right, node.left

            # add this nodes children
            d.append(node.left)
            d.append(node.right)

        return root

    def recursiveInvertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts the binary tree recursively (DFS approach).

        At each node, the left and right children are swapped, and
        the function recursively inverts the subtrees. Recursion depth
        equals the height of the tree.

        Time:
            O(n) - Each of the n nodes is visited and swapped exactly once.
        Space:
            O(h) - Where h is the height of the tree due to recursion stack usage.
                   Best case (balanced tree): O(log(n))
                   Word case (skewed tree): O(n)
        """
        # no nodes to swap
        if not root:
            return root

        root.left, root.right = root.right, root.left  # swap children
        self.recursiveInvertTree(root.left)            # invert left child
        self.recursiveInvertTree(root.right)           # invert right child
        
        return root


if __name__ == "__main__":
    solution = Solution()

    """
    test_cases = [
        GenericTestCase(input=(), expected=None),
        GenericTestCase(input=(), expected=None),
        GenericTestCase(input=(), expected=None),
    ]

    run_tests(
        test_cases,
        [solution.solution],
        label=__file__
    )
    """
