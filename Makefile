.PHONY: clean build test

clean:
	rm -rf dist build *.egg-info

build:
	python -m build

test:
	pytest
