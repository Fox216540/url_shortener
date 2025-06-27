.PHONY: install run test readme

install:
	poetry install

run:
	poetry run python3 start.py

test:
	poetry run pytest

readme:
	poetry run python3 update_readme.py