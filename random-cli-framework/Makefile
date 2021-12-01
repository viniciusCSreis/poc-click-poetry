install:
	poetry install

test:
	poetry run pytest --cov-report html:cov_html --cov=random_cli_framework tests/
	rm .coverage