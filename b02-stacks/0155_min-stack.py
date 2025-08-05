from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class MinStack:
    """
    A stack that supports push, pop, top, and retrieving
    the minimum element all in O(1) time complexity.
    """
    _mainStack: list[int]
    _minStack: list[int]

    def __init__(self) -> None:
        self._mainStack = []
        self._minStack = []

    def push(self, val: int) -> None:
        """pushes an element onto the stack"""
        newMinValue = min(val, self._minStack[-1] if self._minStack else val)
        self._mainStack.append(val)
        self._minStack.append(newMinValue)

    def pop(self) -> None:
        """removes the element on the top of the stack"""
        self._mainStack.pop()
        self._minStack.pop()

    def top(self) -> int:
        """gets the top element of the stack"""
        return self._mainStack[-1]

    def getMin(self) -> int:
        """retrieves the minimum element in the stack"""
        return self._minStack[-1]


if __name__ == "__main__":
    minStack = MinStack()

    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    run_tests(
        [GenericTestCase(input=(), expected=-3)],
        [minStack.getMin],
        label=__file__
    )

    minStack.pop()

    run_tests(
        [GenericTestCase(input=(), expected=0)],
        [minStack.top],
        label=__file__
    )

    run_tests(
        [GenericTestCase(input=(), expected=-2)],
        [minStack.getMin],
        label=__file__
    )
