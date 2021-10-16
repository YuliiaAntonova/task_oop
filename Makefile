.PHONY: all \
		setup \
		run

venv/bin/activate: ## alias for virtual environment
	python3 -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

run: venv/bin/activate ## Run
	. venv/bin/activate; python main.py
