from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if not nums: return []

        N = len(nums)
        output = [1] * N

        # accumulate what needs to be multiplied on the left
        prefix = 1
        for k in range(N):
            output[k] = prefix
            prefix *= nums[k]

        # accumulate what needs to be multiplied on the right
        postfix = 1
        for k in range(N - 1, -1, -1):
            output[k] *= postfix
            postfix *= nums[k]

        return output


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([1, 2, 4, 6],), expected=[48, 24, 12, 8]),
        GenericTestCase(input=([],), expected=[]),
        GenericTestCase(input=([-1, 0, 1, 2, 3],), expected=[0, -6, 0, 0, 0]),
    ]

    run_tests(
        test_cases,
        [solution.productExceptSelf],
        label=__file__
    )
