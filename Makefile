clean:
	@find . -iname '*.pyc' -delete
	@rm -rf *.egg-info dist

test: clean
	@coverage run --branch `which nosetests` -vv -s tests/
	@coverage report -m --fail-under=73
	@flake8 tornado_prometheus tests

setup:
	@pip install -U -e .\[tests\]
