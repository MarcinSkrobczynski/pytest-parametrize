import pytest

from pytest_parametrize import parametrize


@pytest.mark.parametrize(
    "test_cases, exception, expected_arguments, expected_test_cases",
    [
        # no test cases
        ({}, ValueError, None, None),
        # different type of entry
        ({"name": "value"}, ValueError, None, None),
        # different params
        ({"1": {"a": 1}, "2": {"b": 1}}, ValueError, None, None),
        # one more param
        ({"1": {"a": 1}, "2": {"a": 1, "b": 2}}, ValueError, None, None),
        # only dicts
        ({"1": {"a": 1}, "2": {"a": 1}}, None, ("a",), [("1", (1,), ()), ("2", (1,), ())]),
        # only dicts with different order of params
        ({"1": {"a": 1, "b": 2}, "2": {"b": 1, "a": 2}}, None, ("a", "b"), [("1", (1, 2), ()), ("2", (2, 1), ())]),
        # dict and list of dicts
        (
            {"1": {"a": 1}, "2": [{"a": 1}, {"a": 2}, {"a": 3}]},
            None,
            ("a",),
            [("1", (1,), ()), ("2__subcase_", (1,), ()), ("2__subcase_", (2,), ()), ("2__subcase_", (3,), ())],
        ),
        # contains marks argument name
        (
            {"1": {"a": 1}, "2": {"a": 1, "marks": pytest.mark.xfail}},
            None,
            ("a",),
            [("1", (1,), ()), ("2", (1,), pytest.mark.xfail)],
        ),
    ],
)
def test_parametrize(mocker, test_cases, exception, expected_arguments, expected_test_cases):
    parametrize_mock = mocker.patch("pytest.mark.parametrize")
    param_mock = mocker.patch("pytest.param")

    if exception and issubclass(exception, Exception):
        with pytest.raises(exception):
            parametrize(test_cases)
        parametrize_mock.assert_not_called()
    else:
        result = parametrize(test_cases)
        assert result == parametrize_mock.return_value

        parametrize_mock.assert_called_once_with(
            expected_arguments, len(expected_test_cases) * [param_mock.return_value]
        )

        expected_param_calls = [mocker.call(*values, id=idx, marks=marks) for idx, values, marks in expected_test_cases]
        assert param_mock.mock_calls == expected_param_calls
