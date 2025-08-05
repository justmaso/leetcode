from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def evaluateReversePolishNotation(self, tokens: list[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in ops:
                # get the last two tokens as ints
                laterValue = stack.pop()
                earlierValue = stack.pop()
                operationResult = int()

                # perform the appropriate operation
                if token == "+": operationResult = earlierValue + laterValue
                elif token == "-": operationResult = earlierValue - laterValue
                elif token == "*": operationResult = earlierValue * laterValue
                else:
                    if abs(laterValue) > earlierValue: operationResult = 0
                    else: operationResult = earlierValue // laterValue

                # in case of heavily nested RPN, we must generalize
                stack.append(operationResult)
            else:
                # append
                stack.append(int(token))
            print(stack)

        # reverse polish notation should be flattened
        return stack[0]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=(["2", "1", "+", "3", "*"],), expected=9),
        GenericTestCase(input=(["4", "13", "5", "/", "+"],), expected=6),
        GenericTestCase(input=(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],), expected=22),
    ]

    run_tests(
        test_cases,
        [solution.evaluateReversePolishNotation],
        label=__file__
    )
