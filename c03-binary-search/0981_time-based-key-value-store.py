from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class TimeMap:
    """
    A time-based key-value data structure that can store
    multiple values for the same key at different time stamps
    and retrieve the key's value at a certain timestamp.
    """
    store: dict[str, list[list]]

    def __init__(self) -> None:
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores a key-value pair at the given timestamp.
        """
        if key not in self.store:
            self.store[key] = []

        # no need to do any sorting as timestamps are strictly increasing
        # (i.e., appending new key-value pairs result in a sorted list no matter what)
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns a value that set was called previously, with
        timestamp_prev <= timestamp. If there are multiple such values,
        it returns the value associated with the largest timestamp_prev.
        If there are no values, it returns an empty string ("")
        """
        result = ""
        values = self.store.get(key, [])

        # perform binary search on the sorted list of (val, timestamp)
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2

            # mid timestamp is usable
            if values[mid][1] <= timestamp:
                result = values[mid][0]

                # however, exact timestamp could still exist
                # (so we continue the search rightwards)
                left = mid + 1
            # mid timestamp too large; search leftward
            else:
                right = mid - 1

        return result

if __name__ == "__main__":
    timeMap = TimeMap()

    timeMap.set("foo", "bar", 1)

    run_tests(
        [
            GenericTestCase(input=("foo", 1), expected="bar"),
            GenericTestCase(input=("foo", 3), expected="bar"),
        ],
        [timeMap.get],
        label=__file__
    )

    timeMap.set("foo", "bar2", 4)

    run_tests(
        [
            GenericTestCase(input=("foo", 4), expected="bar2"),
            GenericTestCase(input=("foo", 5), expected="bar2"),
        ],
        [timeMap.get],
        label=__file__
    )
