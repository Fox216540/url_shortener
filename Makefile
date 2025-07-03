.PHONY: install run readme mig test-mig test

install:
	poetry install

run:
	$(MAKE) mig && poetry run python3 start.py

readme:
	poetry run python3 update_readme.py

mig:
	poetry run alembic upgrade head

test:
		@export \
		POSTGRES_PORT="8100" \
		POSTGRES_DB="test" \
		POSTGRES_USER="test" \
		POSTGRES_PASSWORD="test" \
		REDIS_PORT="8101" \
		PYTHONPATH=. ; \
		echo "🚀 Starting test environment..." ; \
		docker-compose --profile test up -d ; \
		docker-compose exec -T db sh -c 'until pg_isready -U test -d test; do sleep 1; done' ; \
		docker-compose exec -T redis sh -c 'until redis-cli ping | grep PONG; do sleep 1; done' ; \
		echo "\n🔄 Applying migrations..." ; \
		$(MAKE) mig ; \
		echo "\n🔧 Running tests..." ; \
		poetry run pytest test/e2e/pytest/ -v \
			-W ignore::sqlalchemy.exc.MovedIn20Warning \
			-W ignore::DeprecationWarning ; \
		echo "\n🧹 Cleaning up..."
		@docker-compose stop test-db test-redis && docker-compose rm -f -v test-db test-redis

