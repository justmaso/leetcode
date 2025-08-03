from dataclasses import dataclass


@dataclass
class GenericTestCase:
    input: tuple
    expected: any


def run_tests(
    test_cases: list[GenericTestCase],
    solutions: list[callable],
    label: str = ""
):
    print(f"running tests for: {label}\n" + "-"*19)
    for idx, case in enumerate(test_cases):
        print(f"[case {idx + 1}/{len(test_cases)}]: input={case.input}, expected={case.expected}")
        for solution in solutions:
            try:
                result = solution(*case.input)
                passed = result == case.expected
                status = "🟩" if passed else "🟥"
                print(f"\t{status} {solution.__name__} {'(got ' + str(result) + ')' if not passed else ''}")
            except Exception as e:
                print(f"\t❓ {solution.__name__} raised an exception: {e}")
        print()
