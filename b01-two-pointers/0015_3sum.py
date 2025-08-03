from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        solutions = []

        for k, n in enumerate(nums):
            # skip duplicates
            if k != 0 and nums[k - 1] == n: continue

            # use two sum II solution for the remaining list items
            left, right = k + 1, len(nums) - 1
            while left < right:
                left_value = nums[left]
                right_value = nums[right]
                curr_sum = n + left_value + right_value

                # found possible solution
                if curr_sum == 0:
                    solutions.append([n, left_value, right_value])

                    # now, to prevent either pointer from being used again, we update either (only once)

                    # prevent left pointer from being trivially used again
                    # left += 1
                    # while nums[left] == nums[left - 1] and left < right:
                        # left += 1

                    # prevent right pointer from being trivially used again
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                # sum too small, increase left pointer
                elif curr_sum < 0:
                    left += 1
                # sum too large, decrease right pointer
                else:
                    right -= 1

        return solutions


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([-1, 0, 1, 2, -1, -4],), expected=[[-1, -1, 2], [-1, 0, 1]]),
        GenericTestCase(input=([0, 1, 1],), expected=[]),
        GenericTestCase(input=([0, 0, 0],), expected=[[0, 0, 0]]),
    ]

    run_tests(
        test_cases,
        [solution.threeSum],
        label=__file__
    )
