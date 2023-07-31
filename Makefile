.PHONY: lint

PYTHON_FILES := $(shell git ls-files '*.py')

lint:
	pylint --rcfile=.pylintrc $(PYTHON_FILES)
test-unit:
	python -m unittest discover -s tests -p "test_*.py"
