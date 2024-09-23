import pytest

from pytest_parametrize import InvalidMarkDecorator, parametrize


@parametrize(
    {
        "test-case-1": {"a": 1, "b": 3, "expected": 3},
        "test-case-2": {"a": 5, "b": 1, "expected": 5},
        "test-case-3": [
            {"a": 1, "b": 12, "expected": 12},
            {"a": 2, "b": 6, "expected": 12},
            {"a": 3, "b": 4, "expected": 12},
        ],
        "test-case-4": {"a": 1, "b": 11, "expected": 11},
        "test-case-5": [
            {"a": 1, "b": 20, "expected": 20},
            {"a": 2, "b": 10, "expected": 20},
            {"a": 4, "b": 5, "expected": 20},
        ],
        "test-case-6": {"a": 0, "b": 11, "expected": 11, "marks": pytest.mark.xfail},
    }
)
def test_parametrize(a: int, b: int, expected: int):
    assert a * b == expected


@parametrize(
    {
        "single-value": {"marks_value": 10},
        "collection": [
            {"marks_value": [10]},
            {"marks_value": [pytest.mark.xfail, 10]},
            {"marks_value": [10, pytest.mark.xfail, pytest.mark.skip]},
        ],
    }
)
def test_parametrize__when_marks_invalid(marks_value):
    with pytest.raises(InvalidMarkDecorator):

        @parametrize(
            {
                "case": {"a": 1, "marks": marks_value},
            }
        )
        def test(a: int):
            pass
