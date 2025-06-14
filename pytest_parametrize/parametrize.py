from collections.abc import Collection, Sequence
from typing import Any, Union

import pytest

TestCase = dict[str, Any]
ListSubTestCases = list[TestCase]


class InvalidMarkDecorator(Exception):
    pass


def _assert_mark_decorator(marks: Union[pytest.MarkDecorator, Collection[pytest.MarkDecorator]]) -> None:
    """
    Raise exception if provided marks is/are invalid.

    :param marks: MarkDecorator or Collection of MarkDecorators
    :return: None
    :raises InvalidMarkDecorator if provided marks are invalid
    """
    _marks = (marks,) if not isinstance(marks, Sequence) else marks

    if not all(isinstance(m, pytest.MarkDecorator) for m in _marks):
        raise InvalidMarkDecorator


def parametrize(raw_test_cases: dict[str, Union[TestCase, ListSubTestCases]]) -> pytest.MarkDecorator:
    """
    Decorate test function with parametrized test cases, provided as a dictionary.

    :param raw_test_cases: dictionary with values as dictionary or list of dictionaries
    :return: pytest.MarkDecorator with parametrized test cases
    :raises ValueError if raw test case is neither dict nor list
    :raises ValueError if number of parameters differs

    Example:
    ```
    import pytest
    from pytest_parametrize import parametrize

    @parametrize(
        {
            "test-case-1": {"a": 1, "b": 2, "c": 3},
            "test-case-2": {"a": 2, "b": 3, "c": 5},
            "test-case-3": [
                {"a": 3, "b": 5, "c": 8},
                {"a": 5, "b": 8, "c": 13},
                {"a": 8, "b": 13, "c": 21},
                {"a": 0, "b": 0, "c": 1, "marks": pytest.mark.xfail},
            ],
        },
    )
    def test_something(a, b, c):
        assert a + b == c
    ```

    """
    arguments, test_cases = set(), []

    for identifier, cases in raw_test_cases.items():
        if isinstance(cases, dict):
            cases = [cases]
        elif isinstance(cases, list):
            identifier = f"{identifier}__subcase_"
        else:
            raise ValueError("raw test case should be a dict or list")

        for case in cases:
            sorted_case: dict = dict(sorted(case.items()))
            marks = sorted_case.pop("marks", ())
            _assert_mark_decorator(marks)
            arguments.add(tuple(sorted_case.keys()))
            test_cases.append(pytest.param(*sorted_case.values(), id=identifier, marks=marks))

    if len(arguments) != 1:
        raise ValueError(f"defined parameters should be the same for all raw test cases\n{arguments}")

    args = tuple(arguments.pop())

    return pytest.mark.parametrize(args, test_cases)
