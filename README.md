# CLI Task Manager - Sample Python Project

A clean, modern command-line task manager application written in Python. It demonstrates project packaging, structured modules, unit testing, and JSON file storage.

## Features

- **Add** a task with a title.
- **List** all active and completed tasks.
- **Complete** tasks by their unique ID.
- **Delete** tasks.
- Persistent storage using a JSON file (`~/.todo_tasks.json` by default).

## Project Structure

```
├── pyproject.toml         # Package metadata and requirements
├── requirements.txt       # Development dependencies (pytest)
├── README.md              # Project documentation
├── src/
│   └── task_manager/      # Main application package
│       ├── __init__.py
│       ├── cli.py         # Entry point and argument parsing
│       ├── manager.py     # TaskManager core operations
│       ├── models.py      # Dataclasses (Task model)
│       └── storage.py     # JSON file load/save handling
└── tests/                 # Unit tests
    ├── __init__.py
    ├── test_manager.py
    └── test_storage.py
```

## Setup Instructions

### 1. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate
```

### 2. Install Development Dependencies

Install the package in editable mode with development dependencies:

```bash
pip install -e .[dev]
```

Or just install the test requirements:

```bash
pip install -r requirements.txt
```

## Usage

You can run the application directly using Python's module syntax:

```bash
# Add a new task
python -m src.task_manager.cli add "Buy groceries"

# Add another task
python -m src.task_manager.cli add "Read a book"

# List all tasks
python -m src.task_manager.cli list

# Complete a task (e.g. task ID 1)
python -m src.task_manager.cli complete 1

# Delete a task (e.g. task ID 2)
python -m src.task_manager.cli delete 2
```

If you installed the package via `pip install -e .`, you can use the CLI shortcut directly:

```bash
task-mgr list
task-mgr add "Explore pyproject.toml"
```

## Running Tests

Run the test suite using `pytest`:

```bash
pytest
```
