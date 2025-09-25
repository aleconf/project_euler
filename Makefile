# Makefile for Python Project

setup:
	uv sync

tests: setup tests/*.py
	uv run pytest

linter:
	uvx ruff check

format:
	uvx ruff format

typecheck:
	uv run mypy src tests

run: setup src/*.py
	@echo ">>> Launching the application..."
	uv run src/main.py

