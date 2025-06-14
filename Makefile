mypy:
	mypy --install-types --non-interactive pytest_parametrize

ruff-check:
	ruff check --fix pytest_parametrize

ruff-format:
	ruff format pytest_parametrize

lint: ruff-check ruff-format mypy
