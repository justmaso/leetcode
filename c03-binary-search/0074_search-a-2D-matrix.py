from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def bruteSearchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Brute force solution that just searches the entire m x n matrix.

        Time complexity: O(m x n)
        Space complexity: O(1)
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == target: return True

        return False

    def nonOptimalSearchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Non-optimal solution that uses the matrix structure to find the row
        to perform the search on.

        Time complexity: O(m + log(n))
        Space compexity: O(1)
        """
        M = len(matrix)
        N = len(matrix[0])

        for r in range(M):
            if matrix[r][-1] >= target:
                left, right = 0, N - 1
                while left <= right:
                    midpoint = left + (right - left) // 2
                    midval = matrix[r][midpoint]

                    if midval == target: return True
                    elif midval < target: left = midpoint + 1
                    else: right = midpoint - 1

                return False
            else: continue

        return False

    def optimalSearchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        You are given an m x n matrix of integers with the following properties:
            (i) Each row is sorted in non-decreasing order.
            (ii) The first integer of each row is greater than the last 
                 integer of the previous row.
        
        Given an integer `target`, return `True` if `target` is in `matrix` or `False`
        otherwise.

        Your solution must have a time complexity of O(log(m * n)).
        """

        """
        Optimal solution that uses a double binary search across the entire matrix.

        Time complexity: O(log(m * n))
        Space complexity: O(1)
        """
        M = len(matrix)
        N = len(matrix[0])

        # perform a binary search on the leftmost column
        smallerRow, largerRow = 0, M - 1
        while smallerRow <= largerRow:
            midRow = smallerRow + (largerRow - smallerRow) // 2
            
            # target is larger than the max in this row; check rows after
            if target > matrix[midRow][-1]:
                smallerRow = midRow + 1
            # target is less than the min in this row; check rows before
            elif target < matrix[midRow][0]:
                largerRow = midRow - 1
            else: # target >= matrix[midRow][-1] and target <= matrix[midRow][0]
                break

        # target doesn't exist in any row
        if smallerRow > largerRow:
            return False

        targetRow = smallerRow + (largerRow - smallerRow) // 2

        # perform a binary search on the target row
        leftCol, rightCol = 0, N - 1
        while leftCol <= rightCol:
            midcol = leftCol + (rightCol - leftCol) // 2
            midval = matrix[targetRow][midcol]

            if target == midval: return True
            elif target > midval: leftCol = midcol + 1
            else: rightCol = midcol - 1

        return False

    def simplerSearchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Another optimal solution that uses a single binary search by treating the
        entire matrix as a concatenated list (row-wise).

        Time complexity: O(log(m * n))
        Space complexity: O(1)
        """
        M = len(matrix)
        N = len(matrix[0])

        left, right = 0, M * N - 1
        while left <= right:
            midpoint = left + (right - left) // 2
            midRow = midpoint // N
            midCol = midpoint % N
            midVal = matrix[midRow][midCol]

            if midVal == target: return True
            elif midVal < target: left = midpoint + 1
            else: right = midpoint - 1

        return False

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), expected=True),
        GenericTestCase(input=([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), expected=False),
    ]

    run_tests(
        test_cases,
        [
            solution.bruteSearchMatrix,
            solution.nonOptimalSearchMatrix,
            solution.optimalSearchMatrix,
            solution.simplerSearchMatrix
        ],
        label=__file__
    )
