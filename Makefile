.PHONY: tests

tests:
# Run all tests for this project
	@python -m unittest -v ./tests/test_version.py
