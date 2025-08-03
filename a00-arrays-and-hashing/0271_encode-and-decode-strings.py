from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    _d: str

    def __init__(self):
        self._d = "%"

    def encode(self, strs: list[str]) -> str:
        encoding = ""

        for s in strs:
            encoding += f"{len(s)}{self._d}{s}"

        return encoding

    def decode(self, encoding: str) -> list[str]:
        decoding = []
        k = 0
        temp = ""

        while k < len(encoding):
            if encoding[k] == self._d:
                word_length = int(temp)
                decoding.append(encoding[k + 1:k + 1 + word_length])
                k += word_length + 1
                temp = ""
            else:
                temp += encoding[k]
                k += 1

        return decoding


if __name__ == "__main__":
    solution = Solution()

    encode_test_cases = [
        GenericTestCase(input=([],), expected=""),
        GenericTestCase(input=(["hello", "world"],), expected="5%hello5%world"),
        GenericTestCase(input=([""],), expected="0%"),
        GenericTestCase(input=(["", ""],), expected="0%0%"),
        GenericTestCase(input=(["%"],), expected="1%%"),
        GenericTestCase(input=(["12%abc", "!!", ""],), expected="6%12%abc2%!!0%"),
    ]

    decode_test_cases = [
        GenericTestCase(input=("",), expected=[]),
        GenericTestCase(input=("5%hello5%world",), expected=["hello", "world"]),
        GenericTestCase(input=("0%",), expected=[""]),
        GenericTestCase(input=("0%0%",), expected=["", ""]),
        GenericTestCase(input=("1%%",), expected=["%"]),
        GenericTestCase(input=("6%12%abc2%!!0%",), expected=["12%abc", "!!", ""]),
    ]

    # run encoding tests
    run_tests(
        encode_test_cases,
        [solution.encode],
        label=f"{__file__}::Solution.encode"
    )

    # run decoding tests
    run_tests(
        decode_test_cases,
        [solution.decode],
        label=f"{__file__}::Solution.decode"
    )
