install:
	poetry remove random-cli-framework
	poetry add ../random-cli-framework
	poetry install

test:
	poetry run pytest --cov-report html:cov_html --cov=random_cli tests/
	rm .coverage

bin:
	poetry run pyinstaller  random_cli/cmd.py