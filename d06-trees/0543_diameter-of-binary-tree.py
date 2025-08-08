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
    Given the root of a binary tree, return the length
    of the diameter of the tree.

    The diameter of a binary tree is the length of the
    longest path between any two nodes in a tree. This path
    may or may not pass through the root.

    The length of a path between two nodes is represented by
    the number of edges between them.
    """

    def _maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(
            self._maxDepth(root.left),
            self._maxDepth(root.right)
        )
    
    def bruteDiameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Approach:
            For each node in the tree (traversed iteratively using a BFS):
                1. Compute the max depth of its left subtree.
                2. Compute the max depth of its right subtree.
                3. Update the diameter as the max of its current value and
                   and the sum of left and right depths (representing the
                   longest path passing through that node.

        Time:
            O(n^2) - For each of the n nodes, computing max depth takes
                     O(n) in the worst case (skewed tree).
        Space:
            O(n) - BFS queue can store up to O(w) nodes, where w is the max
                   width of the tree (O(n) in the worst case). The recursion
                   in _maxDepth also uses O(h) stack space (O(n) in worst case).
        """
        from collections import deque
        d = deque([root])
        diameter = 0

        while d:
            node = d.popleft()

            if not node:
                continue

            left = self._maxDepth(node.left)
            right = self._maxDepth(node.right)
            diameter = max(
                diameter,
                left + right
            )

            d.append(node.left)
            d.append(node.right)

        return diameter


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Approach:
            Performs a DFS where each call:
                1. Recursively computes the height of the left and 
                    right subtrees.
                2. Updates a global diameter attribute with the sum
                   of left and right heights (representing the longest path
                   passing through this node).
                3. Returns the height of the current node to its parent.
        
            Ensures we compute both the height and diameter in a single DFS pass.

        Time:
            O(n) - Each of the n nodes is visited exactly once.
        Space:
            O(h) - Where h is the height of the tree due to recursion stack usage.
                   Best case (balanced tree): O(log(n)).
                   Worst case (skewed tree): O(n).
        """
        self.diameter = 0

        def dfs(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.diameter


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
