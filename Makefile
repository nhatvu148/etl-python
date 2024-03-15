include .env

ifeq ($(OS),Windows_NT) 
    detected_OS := Windows
	VENV_BIN_DIR = venv/Scripts
	PYTHON = "$(VENV_BIN_DIR)/python.exe"
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
	VENV_BIN_DIR = venv/bin
	PYTHON = "$(VENV_BIN_DIR)/python"
endif

CMD_FROM_VENV = ". $(VENV_BIN_DIR)/activate; which"
PIP = "$(VENV_BIN_DIR)/pip"
define create-venv
$(shell which python3) -m venv venv
endef
define create-venv-win
$(PYTHON_ROOT)/python.exe -m venv venv
endef

.PHONY: all
all: check-py run-py

check-py:
	$(PYTHON) -m autopep8 --in-place --aggressive --aggressive ollama.py
	$(PYTHON) -m flake8 ollama.py > error.txt

run-py:
	$(PYTHON) ollama.py

venv:
	@$(create-venv)
	@$(PIP) install -r requirements.txt

venv-win:
	@$(create-venv-win)
	@$(PIP) install -r requirements.txt

clean-venv:
	@rm -rf venv