.PHONY: install run test

install:
	poetry install

run:
	poetry run python3 start.py

test:
	poetry run pytest
