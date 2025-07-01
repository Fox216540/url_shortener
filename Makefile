.PHONY: install run test readme mig

install:
	poetry install

run:
	$(MAKE) mig && poetry run python3 start.py

test:
	poetry run pytest

readme:
	poetry run python3 update_readme.py

mig:
	poetry run alembic upgrade head