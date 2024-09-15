# pytest-parametrize

[pytest](https://pytest.org/) decorator for parametrizing test cases in a dict-way.
It is an alternative for the [pytest.mark.parametrize](https://docs.pytest.org/en/latest/how-to/parametrize.html).

## Usage
Decorate test function with test cases defined as a dictionary.

Example:
```python
from pytest_parametrize import parametrize

@parametrize(
    {
        "test-case-1": {"a": 1, "b": 2, "c": 3},
        "test-case-2": {"a": 2, "b": 3, "c": 5},
        "test-case-3": [
            {"a": 3, "b": 5, "c": 8},
            {"a": 5, "b": 8, "c": 13},
            {"a": 8, "b": 13, "c": 21},
        ],
    },
)
def test_something(a, b, c):
    assert a + b == c
```

## Installation

### pip
```shell
pip install pytest-parametrize
```

### poetry
```shell
poetry add pytest-parametrize
```

# Collaboration

## Test & coverage
```shell
pytest -vvv tests --cov=pytest_parametrize
```
