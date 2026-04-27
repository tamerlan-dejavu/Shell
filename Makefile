.PHONY: run test lint clean

run:
	python shell.py

test:
	pytest tests/ -v --cov=. --cov-report=term-missing

lint:
	flake8 . --max-line-length=100 --exclude=.git,__pycache__

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; \
	find . -name '*.pyc' -delete 2>/dev/null; \
	true
