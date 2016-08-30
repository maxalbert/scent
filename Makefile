PKGNAME = scent
PYTEST = py.test
PYTEST_OPTIONS = -sv --cov=$(PKGNAME) --cov-report=term-missing

all: test

test: unit-tests

unit-tests:
	$(PYTEST) $(PYTEST_OPTIONS) tests/unit_tests/

build:
	python setup.py bdist_wheel

clean:
	rm -rf build dist $(PKGNAME).egg-info

.PHONY: all build clean test unit-tests
