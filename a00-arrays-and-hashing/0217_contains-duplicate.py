from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([1, 2, 3, 1],), expected=True),
        GenericTestCase(input=([1, 2, 3, 4],), expected=False),
        GenericTestCase(input=([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), expected=True),
        GenericTestCase(input=([],), expected=False),
    ]

    run_tests(
        test_cases,
        [solution.containsDuplicate],
        label=__file__
    )
