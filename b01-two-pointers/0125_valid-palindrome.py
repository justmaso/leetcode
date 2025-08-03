from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True

        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1

            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
    
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=("A man, a plan, a canal: Panama",), expected=True),
        GenericTestCase(input=("race a car",), expected=False),
        GenericTestCase(input=(" ",), expected=True),
    ]

    run_tests(
        test_cases,
        [solution.isPalindrome],
        label=__file__
    )
