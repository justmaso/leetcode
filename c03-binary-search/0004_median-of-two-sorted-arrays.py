from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def bruteFindMedianSortedArray(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Brute force solution that just combines the two lists
        and computes the median.

        Time complexity: O(m + n)
        Space complexity: O(m + n)
        """
        fullList = nums1 + nums2
        fullList.sort()
        newN = len(fullList)

        if newN % 2 == 0:
            rightIdx = newN // 2
            return (fullList[rightIdx] + fullList[rightIdx - 1]) / 2
        else:
            return fullList[newN // 2]

    def findMedianSortedArray(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n
        respectively, return the median of the two sorted arrays.

        The overall run time complexity should be O(log (m+n)).
        """
        A, B = nums1, nums2
        M, N = len(A), len(B)
        total = M + N
        half = total // 2

        if N < M:
            A, B = B, A
            M, N = N, M

        l, r = 0, M - 1

        # solution is guaranteed, so just run the algorithm until median is found
        while True:
            midA = l + (r - l) // 2
            midB = half - midA - 2

            aLeft = A[midA] if midA >= 0 else float("-inf")
            aRight = A[midA + 1] if (midA + 1) < M else float("inf")
            bLeft = B[midB] if midB >= 0 else float("-inf")
            bRight = B[midB + 1] if (midB + 1) < N else float("inf")

            # left partition is correct; found median
            if aLeft <= bRight and bLeft <= aRight:
                # even case
                if total % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                # odd case
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                r = midA - 1
            else:
                l = midA + 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([1, 3], [2]), expected=2.0),
        GenericTestCase(input=([1, 2], [3, 4]), expected=2.5),
    ]

    run_tests(
        test_cases,
        [
            solution.bruteFindMedianSortedArray,
            solution.findMedianSortedArray
        ],
        label=__file__
    )
