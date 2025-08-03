from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        longest = 0

        for n in values:
            # found the start of a sequence
            if (n - 1) not in values:
                curr_consecutive = 1

                # determine the length of the current sequence
                while (n + curr_consecutive) in values:
                    curr_consecutive += 1

                # update longest
                longest = max(longest, curr_consecutive)

        return longest


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([100, 4, 200, 1, 3, 2],), expected=4),
        GenericTestCase(input=([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), expected=9),
        GenericTestCase(input=([1, 1, 0, 2],), expected=3),
        GenericTestCase(input=([],), expected=0),
    ]

    run_tests(
        test_cases,
        [solution.longestConsecutive],
        label=__file__
    )
