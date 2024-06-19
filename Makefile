migrate:
	cd src/database/migrations && poetry run alembic upgrade head

setup:
	@if [ -e .env ] ; then \
		echo ".env already exists" \
	else  \
		cp .env.example .env; \
	fi

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

app-new-migration:
	docker compose exec app bash -c "cd src/database/migrations && poetry run alembic revision -m '${NAME}'"

