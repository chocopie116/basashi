VIRTUALENV=$(shell which virtualenv)
PYTHON=python2

install: venv
	$</bin/pip install --upgrade setuptools pip
	$</bin/pip install requests

run:
	source venv/bin/activate && source mackerel/.env && python soundmeter.py

venv:
	$(MAKE) virtualenv

virtualenv:
	$(VIRTUALENV) venv -p $(PYTHON)
