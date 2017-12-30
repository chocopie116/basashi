VIRTUALENV=$(shell which virtualenv)
PYTHON=python2

install: venv
	$</bin/pip install --upgrade setuptools pip

run:
	@source venv/bin/activate && source .env && python soundmeter.py

venv:
	$(MAKE) virtualenv

virtualenv:
	$(VIRTUALENV) venv -p $(PYTHON)
