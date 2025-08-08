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
    Given the root of a binary tree, return its
    maximum depth.

    A binary tree's max depth is the number of nodes
    along the longest path from the root down to the
    furthest node.
    """

    def iterativeMaxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Computes the max depth of a binary tree iteratively using BFS.

        A queue stores pairs of (level, node). Each node is processed
        once and its children are added to the queue with their
        corresponding level.

        Time:
            O(n) - Each of the n nodes is dequeed, processed, and its children
                   are enqueued exactly once.
        Space:
            O(w) - Where w is the max width of the tree (max number of nodes
                    stored in the queue at once).
                    Worst case occurs for a complete binary tree: O(n)
        """
        from collections import deque
        d = deque([(0, root)])
        max_depth = 0

        while d:
            level, node = d.popleft()

            if not node:
                continue
            
            max_depth = max(max_depth, level + 1)
            last_level = level
            d.append(level + 1, node.left)
            d.append(level + 1, node.right)

        return max_depth

    def recursiveMaxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Computes the max depth of a binary tree recursively using DFS.

        For each node, the maximum depth is 1 (the current node) plus the
        greater of the maximum depths on its left and right children.

        Time:
            O(n) - Each of the n nodes is visited exactly once.
        Space:
            O(h) - Where h is the height of the tree due to recursion stack usage.
                   Best case (balanced tree): O(log(n))
                   Worst case (skewed tree): O(n)
        """
        # no depth to count
        if not root:
            return 0

        # count this node + the max depth from its children
        return 1 + max(
            self.recursiveMaxDepth(root.left),
            self.recursiveMaxDepth(root.right)
        )


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
