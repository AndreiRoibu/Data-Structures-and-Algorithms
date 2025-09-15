# The default recipe that runs when you just type 'just'. It lists all available recipes.
default:
    @just --list

# Install virtual environment and pre-commit hooks
install:
    echo "🚀 Creating virtual environment and syncing dependencies with uv"
    uv sync
    echo "🚀 Installing pre--commit hooks"
    uv run pre-commit install

# Create a virtual environment with uv
venv:
    echo "🚀 Creating virtual environment with uv in folder .venv"
    python3 -m venv .venv
    echo "🚀 Installing uv in the virtual environment"
    .venv/bin/pip install --upgrade uv