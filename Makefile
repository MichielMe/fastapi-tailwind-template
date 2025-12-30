.PHONY: run-uv run-docker down-docker clean test

run-uv:
	uv run fastapi dev --host 0.0.0.0 --port 8000

run-docker:
	docker compose up --build

down-docker:
	docker compose down

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf .cache

test:
	uv run pytest
