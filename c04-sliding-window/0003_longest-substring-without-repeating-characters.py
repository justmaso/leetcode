from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest
        substring without duplicate characters.
        """

        """
        Optimal solution that builds out all potential non-repeating
        substrings and tracks the current length.

        Time: O(n)
        Space: O(n)
        """
        charSet = set()
        left = 0
        maxLength = 0

        # vary the right pointer
        for right in range(len(s)):
            # while this isn't a valid substring, remove repeated chars
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=("abcabcbb",), expected=3),
        GenericTestCase(input=("bbbbb",), expected=1),
        GenericTestCase(input=("pwwkew",), expected=3),
    ]

    run_tests(
        test_cases,
        [solution.lengthOfLongestSubstring],
        label=__file__
    )
