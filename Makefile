PKGNAME = scent
PYTEST = py.test
PYTEST_OPTIONS = -sv --cov=$(PKGNAME) --cov-report=term-missing

all:

test: unit-tests

unit-tests:
	$(PYTEST) $(PYTEST_OPTIONS) tests/unit_tests/

build:
	python setup.py bdist_wheel

clean:
	rm -rf build dist $(PKGNAME).egg-info

.PHONY: all clean test unit-tests
