.PHONY: help setup install test jupyter clean update-requirements check-env register-kernel

# Default Python version
PYTHON_VERSION := 3.11.3
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Available commands:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

setup: ## Set up the Python environment (pyenv, venv, install dependencies)
	@echo "$(BLUE)Setting up Python environment...$(NC)"
	@if ! command -v pyenv > /dev/null; then \
		echo "$(YELLOW)Error: pyenv not found. Please install pyenv first.$(NC)"; \
		echo "$(YELLOW)Visit: https://github.com/pyenv/pyenv#installation$(NC)"; \
		exit 1; \
	fi
	@echo "$(BLUE)Checking if Python $(PYTHON_VERSION) is installed...$(NC)"
	@if ! pyenv versions --bare | grep -q "^$(PYTHON_VERSION)$$"; then \
		echo "$(YELLOW)Python $(PYTHON_VERSION) is not installed in pyenv.$(NC)"; \
		echo "$(BLUE)Installing Python $(PYTHON_VERSION)...$(NC)"; \
		pyenv install $(PYTHON_VERSION) || ( \
			echo "$(YELLOW)Failed to install Python $(PYTHON_VERSION).$(NC)"; \
			echo "$(YELLOW)You can install it manually with: pyenv install $(PYTHON_VERSION)$(NC)"; \
			exit 1 \
		); \
	fi
	@echo "$(BLUE)Setting Python version to $(PYTHON_VERSION)...$(NC)"
	@pyenv local $(PYTHON_VERSION) || exit 1
	@echo "$(BLUE)Creating virtual environment...$(NC)"
	@python -m venv $(VENV)
	@echo "$(BLUE)Upgrading pip...$(NC)"
	@$(PIP) install --upgrade pip
	@echo "$(BLUE)Installing dependencies...$(NC)"
	@$(PIP) install -r requirements.txt
	@echo "$(BLUE)Registering Jupyter kernel...$(NC)"
	@$(PYTHON) -m ipykernel install --user --name=ds-eda-project --display-name="Python (ds-eda-project)"
	@echo "$(GREEN)✓ Environment setup complete!$(NC)"
	@echo "$(YELLOW)To activate the environment, run: source $(VENV)/bin/activate$(NC)"
	@echo "$(YELLOW)The kernel 'Python (ds-eda-project)' is now available in Jupyter Lab!$(NC)"

install: check-env ## Install dependencies from requirements.txt
	@echo "$(BLUE)Installing dependencies...$(NC)"
	@$(PIP) install -r requirements.txt
	@echo "$(GREEN)✓ Dependencies installed!$(NC)"

test: check-env ## Run unit tests with pytest
	@echo "$(BLUE)Running tests...$(NC)"
	@$(PYTHON) -m pytest -v
	@echo "$(GREEN)✓ Tests completed!$(NC)"

jupyter: check-env ## Start Jupyter Lab
	@echo "$(BLUE)Starting Jupyter Lab...$(NC)"
	@$(PYTHON) -m jupyterlab

notebook: jupyter ## Alias for jupyter command

clean: ## Remove virtual environment and cache files
	@echo "$(BLUE)Cleaning up...$(NC)"
	@rm -rf $(VENV)
	@find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -r {} + 2>/dev/null || true
	@find . -type d -name ".ipynb_checkpoints" -exec rm -r {} + 2>/dev/null || true
	@echo "$(GREEN)✓ Cleanup complete!$(NC)"

update-requirements: check-env ## Update requirements.txt with current packages
	@echo "$(BLUE)Updating requirements.txt...$(NC)"
	@$(PIP) freeze > requirements.txt
	@echo "$(GREEN)✓ requirements.txt updated!$(NC)"

check-env: ## Check if virtual environment exists
	@if [ ! -d "$(VENV)" ]; then \
		echo "$(YELLOW)Error: Virtual environment not found. Run 'make setup' first.$(NC)"; \
		exit 1; \
	fi

register-kernel: check-env ## Register the virtual environment as a Jupyter kernel
	@echo "$(BLUE)Registering Jupyter kernel...$(NC)"
	@$(PYTHON) -m ipykernel install --user --name=ds-eda-project --display-name="Python (ds-eda-project)"
	@echo "$(GREEN)✓ Kernel registered!$(NC)"
	@echo "$(YELLOW)The kernel 'Python (ds-eda-project)' is now available in Jupyter Lab.$(NC)"
	@echo "$(YELLOW)Select it from the kernel dropdown when opening a notebook.$(NC)"

