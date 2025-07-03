make run-uv:
	uv run fastapi dev --host 0.0.0.0 --port 8000

make run-docker:
	docker compose up --build

make down-docker:
	docker compose down

make clean:
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf .cache
