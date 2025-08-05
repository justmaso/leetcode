from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def generateParentheses(self, n: int) -> list[str]:
        """
        Given n pairs of parentheses, generate all combinations
        of well-formed parenthesis.
        """
        stack = []
        solutions = []

        def backtrack(nOpen: int, nClosed: int, spacing: int = 0) -> None:
            print(f"{spacing * ' '}{''.join(stack)}")
            if nOpen == nClosed == n:
                solutions.append("".join(stack))
                return
            
            if nOpen < n:
                stack.append("(")
                backtrack(nOpen + 1, nClosed, spacing + 1)
                stack.pop()
            
            if nClosed < nOpen:
                stack.append(")")
                backtrack(nOpen, nClosed + 1, spacing + 1)
                stack.pop()

        # start backtracking from empty
        backtrack(0, 0)

        # backtracking populates solutions
        return sorted(solutions)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=(1,), expected=sorted(["()"])),
        GenericTestCase(input=(2,), expected=sorted(["()()", "(())"])),
    ]

    run_tests(
        test_cases,
        [solution.generateParentheses],
        label=__file__
    )
