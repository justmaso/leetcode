from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # approach: variate sum using both ends of the list
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                # increase by one since list is 1-indexed
                return [left + 1, right + 1]
            elif curr_sum < target:
                # sum too small, increase it by updating left pointer
                left += 1
                # keep right pointer the same
            else: # (elif curr_sum > target)
                # sum too large, decrease it by updating right pointer
                # keep left pointer the same
                right -= 1

        # will never happen based on test cases
        raise ValueError

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([2, 7, 11, 15], 9), expected=[1, 2]),
        GenericTestCase(input=([2, 3, 4], 6), expected=[1, 3]),
        GenericTestCase(input=([-1, 0], -1), expected=[1, 2]),
    ]

    run_tests(
        test_cases,
        [solution.twoSum],
        label=__file__
    )
