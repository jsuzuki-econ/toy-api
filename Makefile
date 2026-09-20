run:
	uv run uvicorn app.main:app --reload

lint:
	uv run ruff check .

format:
	uv run ruff format .

test:
	uv run pytest

build:
	docker build -t toy-api .

docker-run:
	docker run --rm -p 8000:8000 toy-api
