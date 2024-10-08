[![image](https://img.shields.io/pypi/v/pytest-parametrize.svg)](https://pypi.org/project/pytest-parametrize/)
[![image](https://img.shields.io/pypi/pyversions/pytest-parametrize.svg)](https://pypi.org/project/pytest-parametrize/)
[![image](https://img.shields.io/pypi/status/pytest-parametrize.svg)](https://pypi.org/project/pytest-parametrize/)

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/MarcinSkrobczynski/pytest-parametrize/build_and_deploy.yml?label=build&logo=github&logoColor=white&style=flat-square)](https://github.com/MarcinSkrobczynski/pytest-parametrize/actions/workflows/build_and_deploy.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![image](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# pytest-parametrize

[pytest](https://pytest.org/) decorator for parametrizing test cases in a dict-way.
It is an alternative for the [pytest.mark.parametrize](https://docs.pytest.org/en/latest/how-to/parametrize.html).

## Usage
Decorate test function with test cases defined as a dictionary.

### Example:

#### Simple
```python
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

#### Or more complex one:
```python
from pytest_parametrize import parametrize

@parametrize(
    {
        "a=1": {"a": 1},
        "a=2": {"a": 2},
    }
)
@parametrize(
    {
        "b=1": {"b": 1},
        "b=2": {"b": 2},
    }
)
def test_parametrize__when_complex_structure(a: int, b: int):
    assert a * b > 0
```

### Description
Decorator takes dict, which:
- keys define names of the test cases, and
- values define named arguments in dict manner (or list of such dicts), which are passed to the decorated test function.

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
