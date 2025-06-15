run:
	poetry run python3 start.py

test:
	PYTHONPATH=src poetry run pytest tests/api -v 