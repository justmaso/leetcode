from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def isValid(self, s: str) -> bool:
        # close to open dict
        cto = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for p in s:
            # closed reached, check if it matches against the stack
            if p in cto:
                # stack is empty or the last added char doesn't match
                if not stack or stack.pop() != cto[p]:
                    return False
            # new opening reached, add it to the stack
            else:
                stack.append(p)

        # if the stack isn't empty, some pair(s) haven't collapsed" 
        return not stack


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=("()",), expected=True),
        GenericTestCase(input=("()[]{}",), expected=True),
        GenericTestCase(input=("(]",), expected=False),
        GenericTestCase(input=("([])",), expected=True),
    ]

    run_tests(
        test_cases,
        [solution.isValid],
        label=__file__
    )
