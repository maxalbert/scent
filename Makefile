PKGNAME = scent

all:

build:
	python setup.py bdist_wheel

clean:
	rm -rf build dist $(PKGNAME).egg-info

.PHONY: all clean
