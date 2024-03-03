include .env

ifeq ($(OS),Windows_NT) 
    detected_OS := Windows
	VENV_BIN_DIR = venv/Scripts
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
	VENV_BIN_DIR = venv/bin
endif

CMD_FROM_VENV = ". $(VENV_BIN_DIR)/activate; which"
PYTHON = "$(VENV_BIN_DIR)/python.exe"
PIP = "$(VENV_BIN_DIR)/pip"
define create-venv
./bin/linux/python -m venv venv
endef
define create-venv-win
$(PYTHON_ROOT)/python.exe -m venv venv
endef

.PHONY: all
all: check-py run-py

check-py:
	$(PYTHON) -m autopep8 --in-place --aggressive --aggressive main.py
	$(PYTHON) -m flake8 main.py > error.txt

run-py:
	$(PYTHON) main.py

venv:
	@$(create-venv)
	@$(PIP) install -r requirements.txt

venv-win:
	@$(create-venv-win)
	@$(PIP) install -r requirements.txt

clean-venv:
	@rm -rf venv